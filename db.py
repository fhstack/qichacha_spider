#!/usr/bin/python3
# coding=utf-8
import pymysql
import base

class Db(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = base.db_host, user = base.db_user, passwd = base.db_passwd, db = base.db_name, port = base.db_port)
        except Exception as e:
            print("FAILED: " + "connect mysql failed, error: " + str(e))
        self.cursor = self.conn.cursor()

    def _help(self):
        str = ""
        for i in range(12):
            if(i == 11):
                str = str + "'%s'"
                return str
            str = str + "'%s', "
        return str

    def insert_all_info(self, info_dicts_list):
        print("insert into")
        template = "INSERT INTO info (legal_person,  official_website, registration_code, credit_code, establishment_date, type, address, term, name, employee_number, status, business_scope) values(%s)"%self._help()
        for info_dicts in info_dicts_list:
            sql = template%(info_dicts["legal_person"], info_dicts["official_website"], info_dicts["registration_code"], info_dicts["credit_code"], info_dicts["establishment_date"], info_dicts["type"], info_dicts["address"], info_dicts["term"], info_dicts["name"], info_dicts["employee_number"],  info_dicts["status"], info_dicts["business_scope"])
#            print(sql)
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("FAILEd: INSERT failed: " + str(e))
