import pymysql
import random

class database:

    def __init__(self):

        self.conn = pymysql.connect(host='localhost', user='root',password='123456',database='pig',charset='utf8')
        self.cursor = self.conn.cursor()

    def query(self,rfidNum):
        self.cursor.execute("SELECT * FROM pigmsg WHERE rfid='%s'"%(rfidNum))
        result = self.cursor.fetchone()
        return result

    #获取状态0：下架，1：已存在
    def getStatus(self,rfidNum):
        return self.query(rfidNum=rfidNum)[2]

    # 上架
    def sell(self,window,rfidNum,talk,score):
        try:
            self.cursor.execute("UPDATE pigmsg SET talk='%s',score='%s' WHERE rfid='%s'"%(talk,score,rfidNum))
            self.conn.commit()
            #print(rfidNum,"档案进库成功，使用的位置为：",position)
            window.showSysMsg(msg=str(rfidNum)+"评论评分成功,请重新刷卡")
        except Exception as e:
            print(str(e))
            #print("改变档案状态有误，请重试")
            window.showSysMsg("评论评分失败，请重试")
            self.conn.rollback()

    def add(self,window,rfid,place):
        try:
            self.cursor.execute("INSERT INTO pigmsg (rfid,place,STATUS,sellplace) VALUES ('%s','%s','饲养中','还没卖出')"%(rfid,place))
            self.conn.commit()
            #print(rfidNum,"档案进库成功，使用的位置为：",position)
            window.showSysMsg(msg=str(rfid)+"生猪已添加成功，请重新刷卡")
        except Exception as e:
            print(str(e))
            #print("改变档案状态有误，请重试")
            window.showSysMsg("生猪添加有误，请重试")
            self.conn.rollback()