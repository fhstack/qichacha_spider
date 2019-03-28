#!/usr/bin/python3
# coding=utf-8
import base
import db
import requests
from lxml import etree


class company_info_spider(object):
    def __init__(self, company_name):
        self._company_name = company_name
        self._company_urls = []
        self.info_dicts_list = []
        
    def get_company_urls(self):
        print("parsing the company url")
        url = base.SEARCH_PAGE % self._company_name
        html = requests.get(url, headers = base.HEADER).content.decode()
        try:
            href = etree.HTML(html).xpath('//*[@id="search-result"]/tr/td[3]/a/@href')
        except Exception as e:
            print( "FAILED:" + "parsing company urls failed, " + str(e))
        for value in href:
            print(base.HOST + value)
            self._company_urls.append(base.HOST + value)

    def extract_company_info(self):
        print("extracting the company info")
        for url in self._company_urls:
            html = requests.get(url, headers = base.HEADER).content.decode()
            info_dict = self._parse(html)
            if len(info_dict) != 0:
                self.info_dicts_list.append(info_dict)

    def _parse(self, html):
        print("_parsing")
        info_dict = {}
        selector = etree.HTML(html)
        for key_word in base.KEY_WORDS:
            print("parsing key_word: " + key_word)
            info = ""
            try:
                result = selector.xpath(base.PATH[key_word])
                if len(result) == 1:
                    info = result[0].strip()
                elif len(result) > 1:   #now only for shareholders
                    for one in result:
                        one = one.strip()
                        info = info + one + " "
                info_dict[key_word] = info
            except Exception as e:
                print("FAILED: " + key_word + " parse failed: " + str(e))
                if(key_word != "official_website"): #one failed drop all
                    return {}
                else:
                    if len(info_dict) != 0: #some company doesn't have own website but the other info is ok
                        info_dict["official_website"] = "暂无"

#        for (key, value) in info_dict.items()
#            print('****************%s******************'%key)
#            print(value)
        return info_dict

    def save_result(self):
        mysql = db.Db()
        print("saving result, please wait")
        mysql.insert_all_info(self.info_dicts_list)


def main():
    company_name = input('please input the name of the company which you want to get -_-!: ')
    spd = company_info_spider(company_name)
    spd.get_company_urls()
    spd.extract_company_info()
    spd.save_result()
    print("finished!")

    
if __name__ == '__main__':
    main()

