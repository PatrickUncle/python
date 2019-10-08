import pymysql
import random

class database:

    def __init__(self):

        self.conn = pymysql.connect(host='localhost', user='root',password='123456',database='rfid',charset='utf8')
        self.cursor = self.conn.cursor()

    def query(self,rfidNum):
        self.cursor.execute("SELECT * FROM FILE WHERE rfidNum='%s'"%(rfidNum))
        result = self.cursor.fetchone()
        return result

    #获取状态0：下架，1：已存在
    def getStatus(self,rfidNum):
        return self.query(rfidNum=rfidNum)[2]

    # 上架
    def upload(self,window,rfidNum):
        try:
            position = random.randint(1,100)
            self.cursor.execute("UPDATE FILE SET status='1',position='%s' WHERE rfidNum='%s'"%(position,rfidNum))
            self.conn.commit()
            #print(rfidNum,"档案进库成功，使用的位置为：",position)
            window.showSysMsg(msg=str(rfidNum)+"档案进库成功，使用的位置为："+str(position))
        except:
            #print("改变档案状态有误，请重试")
            window.showSysMsg("改变档案状态有误，请重试")
            self.conn.rollback()

    # 下架
    def down(self,window,rfidNum):
        try:
            position = self.query(rfidNum=rfidNum)[3]
            self.cursor.execute("UPDATE FILE SET status='0',position='0' WHERE rfidNum='%s'" % (rfidNum))
            self.conn.commit()
            #print(rfidNum,"档案出库成功，释放位置",position)
            window.showSysMsg(msg=str(rfidNum) + "档案出库成功，释放位置" + str(position))
        except:
            #print("改变档案状态有误，请重试")
            window.showSysMsg("改变档案状态有误，请重试")
            self.conn.rollback()

    # 检查rfidNum是否存在
    def rfidNumExist(self,rfidNum):

        print(rfidNum,'档案不存在，请联系管理员添加')

    def add(self,window,rfidNum,fileName):
        try:
            position = random.randint(0,100)
            self.cursor.execute(
                "INSERT INTO file (rfidNum,fileName,STATUS,position) VALUES ('%s','%s',1,%s)" % (rfidNum, fileName,position))
            self.conn.commit()
            # print(rfidNum,"档案进库成功，使用的位置为：",position)
            window.showSysMsg(msg=str(rfidNum) + "档案已添加成功，请重新刷卡")
        except Exception as e:
            print(str(e))
            # print("改变档案状态有误，请重试")
            window.showSysMsg("档案添加有误，请重试")
            self.conn.rollback()