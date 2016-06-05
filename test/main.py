# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql

#URL
url = u'http://www.shixiseng.com/interns'

#param
# k -- kind
# p -- page
page1 = 1
kind1 = 'java'
kind2 = '前端'




class interview(object):
    def __init__(self):
        pass

    # def __init__(self,job_name,company,place,money,work_time,publish_time):
    #     self.job_name = job_name
    #     self.company = company
    #     self.money = money
    #     self.place = place
    #     self.work_time = work_time
    #     self.publish_time = publish_time

    def print_int(self):
        print ('%s%s%s%s%s%s' % (self.job_name,self.company,self.money,self.place,self.work_time,self.publish_time))

##parse url ,get html
def __getHtml(page,kind):
    param = {'k':kind,'p':str(page)}
    #require the html
    html = requests.get(url,param)
    #test html
    print  (page)
    return html.text

#parse html
def __parseHtml(html):
    soup = BeautifulSoup(html,'lxml')
    job_node = soup.select('.job_inf_inf ')
    return job_node


rs = []
#parse node
def __parseNode(nodes):
    for node in nodes:
        inte = interview()
        inte.job_name = node.select('.job_head h3')[0].string
        inte.company = node.select('.job_head .company_name')[0]['title']
        inte.place = node.select('.addr_box span')[0].string
        inte.money = node.select('.money_box ')[0].text[2:].strip()
        inte.work_time = node.select('.day_box')[0].text[2:].strip()
        inte.publish_time = node.select('.time_box')[0].text[2:].strip()
        rs.append(inte)
    return rs

def MySQL_Connect(rs):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = pymysql.connect(host='localhost', user='root', passwd='root', db='interview', port=3306, charset='utf8')
        cur = conn.cursor()  # 获取一个游标
        i = 0
        for s in rs:
            # 注意int类型需要使用str函数转义
            sql = 'insert into interview values ("%s","%s","%s","%s","%s","%s","%s")' % (str(i),s.job_name,s.company,s.money,s.place,s.work_time,s.publish_time)
            print ('sql:'+sql)
            cur.execute('insert into interview values (NULL,"%s","%s","%s","%s","%s","%s")' % (s.job_name,s.company,s.money,s.place,s.work_time,s.publish_time))
            i+=1
        cur.close()  # 关闭游标
        conn.commit()
        conn.close()  # 释放数据库资源
    except  Exception as e:
        print (e)

for i in range(100):
    __parseNode(__parseHtml(__getHtml(i,kind1)))
for i in rs:
    i.print_int()
MySQL_Connect(rs)
