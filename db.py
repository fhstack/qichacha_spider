#!/usr/bin/python3
# coding=utf-8
import pymysql
import base

class Db(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = base.db_host, user = base.db_user, 
                    passwd = base.db_passwd, db = base.db_name, port = base.db_port)
        except Exception as e:
            print("FAILED: " + "connect mysql failed, error: " + str(e))
        self.cursor = self.conn.cursor()

    def _help(self):
        str = ""
        for i in range(13): #number of filed
            if(i == 12):
                str = str + "'%s'"
                return str
            str = str + "'%s', "
        return str

    def insert_all_info(self, info_dicts_list):
        print("insert into")
        template = '''INSERT INTO info (legal_person,  official_website, registration_code, 
                        credit_code, establishment_date, type, address, term, name, 
                        employee_number, status, business_scope, shareholders) values(%s)'''%self._help()
        for info_dict in info_dicts_list:
            sql = template%(info_dict["legal_person"], info_dict["official_website"], info_dict["registration_code"], 
                    info_dict["credit_code"], info_dict["establishment_date"], info_dict["type"], 
                    info_dict["address"], info_dict["term"], info_dict["name"], 
                    info_dict["employee_number"],  info_dict["status"], info_dict["business_scope"], info_dict["shareholders"])
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print("ROLLBACK: INSERT failed: " + str(e))
