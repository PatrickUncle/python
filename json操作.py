# coding=utf-8
import json



class abc(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

class www(object):

    def __init__(self,company_name):
        self.company_name = company_name
        self.manage=abc("pzy",20).__dict__


pzy = www("搬砖总公司")
a = json.dumps(pzy.__dict__,ensure_ascii=False)
print(a)