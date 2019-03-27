#!/usr/bin/python3
# coding=utf-8
import requests
from lxml import etree
import os

SEARCH_PAGE = "https://www.qichacha.com/search?key=%s"
HOST = "https://www.qichacha.com"
#The cookie is a timer cookie?Think about adding a GetANewCookieMoudle
HEADER = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Host": "www.qichacha.com",
"Referer": "https://www.qichacha.com/",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400",
"Upgrade-Insecure-Requests": "1",
"cookie": "zg_did=%7B%22did%22%3A%20%22169b9f33e8d280-06e13f312ee046-345c487f-144000-169b9f33e8f8bc%22%7D; acw_tc=dacb70ce15536029195901731e3fb01600a1f44bd663f26c616e4e3d24; _uab_collina=155360293330394392221136; QCCSESSID=k37k32bjdc2h9d9ke1getp8c16; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1553663077; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1553667155; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201553666765030%2C%22updated%22%3A%201553667372735%2C%22info%22%3A%201553602920085%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%7D"
}

PATH = {
    "name":'//*[@id="company-top"]/div[2]/div[2]/div[1]/h1/text()',
    "legal_person":'//*[@id="Cominfo"]/table[1]/tr[2]/td[1]/div/div[1]/div[2]/a/h2/text()',
    "status":'//*[@id="Cominfo"]/table[2]/tr[2]/td[2]/text()',
    "credit_code":'//*[@id="Cominfo"]/table[2]/tr[3]/td[2]/text()',
    "registration_code":'//*[@id="Cominfo"]/table[2]/tr[4]/td[2]/text()',
    "employee_number":'//*[@id="Cominfo"]/table[2]/tr[4]/td[2]/text()',
    "address":'//*[@id="Cominfo"]/table[2]/tr[10]/td[2]/text()',
    "type":'//*[@id="Cominfo"]/table[2]/tr[5]/td[2]/text()',
    "term":'//*[@id="Cominfo"]/table[2]/tr[9]/td[4]/text()',
    "establishment_date":'//*[@id="Cominfo"]/table[2]/tr[2]/td[4]/text()',
    "business_scope":'//*[@id="Cominfo"]/table[2]/tr[11]/td[2]/text()',
    "offcial_website":'//*[@id="company-top"]/div[2]/div[2]/div[3]/div[1]/span[3]/a/text()'
}

KEY_WORDS = ["name", "legal_person", "status", "credit_code", "registration_code", "employee_number", "address", "type", "term", "establishment_date", "business_scope", "offcial_website"]

class company_info_spider(object):
    def __init__(self, company_name):
        self._company_name = company_name
        self._company_urls = []
        self._result = []
        self._total = 0
        self._failed = 0

    def get_company_urls(self):
        print("parsing the company url")
        url = SEARCH_PAGE % self._company_name
        html = requests.get(url, headers = HEADER).content.decode()
        try:
            href = etree.HTML(html).xpath('//*[@id="search-result"]/tr/td[3]/a/@href')
        except Exception as e:
            print( "FAILED:" + "parsing company urls failed, " + str(e))
        self._total = len(href) * len(KEY_WORDS)
        for value in href:
            print(HOST + value)
            self._company_urls.append(HOST + value)

    def extract_company_info(self):
        print("extracting the company info")
        for url in self._company_urls:
            html = requests.get(url, headers = HEADER).content.decode()
            info_dict = self._parse(html)
            if(len(info_dict) != 0):
                self._result.append(info_dict)

    def _parse(self, html):
        print("_parsing")
        info_dict = {}
        selector = etree.HTML(html)
        for key_word in KEY_WORDS:
            print("parsing key_word: " + key_word)
            try:
                result = selector.xpath(PATH[key_word])[0]
                result = result.strip()
                info_dict[key_word] = result
            except Exception as e:
                print("FAILED: " + key_word + " parse failed: " + str(e))
                return {}
        for (key, value) in info_dict.items():
            print('****************%s******************'%key)
            print(value)
        return info_dict

    def save_result(self):
        print("saving result, please wait")


def main():
    company_name = input('please input the name of the company which you want to get -_-!: ')
    spd = company_info_spider(company_name)
    spd.get_company_urls()
    spd.extract_company_info()
    spd.save_result()
    print("finished!")

    
if __name__ == '__main__':
    main()

