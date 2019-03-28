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
    "offcial_website":'//a[@data-original-title="进入官网"]/text()',
    "shareholders":'//*[@class="seo font-14"]/text()'
}
KEY_WORDS = ["name", "legal_person", "status", "credit_code", "registration_code", "employee_number", "address", "type", "term", "establishment_date", "business_scope", "official_website", "shareholders"]

#mysql
#fill yours
db_host = "127.0.0.1"
db_port = 3306
db_user = "root"
db_passwd = ""
db_name = "company_info"
