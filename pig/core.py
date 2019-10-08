from pig import db
import serial
import threading
import time
import tkinter

conn = db.database()

class win:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_sys)
        self.root.title('生猪养殖售后管理系统')
        self.root.geometry('500x300')
        self.rfidTip = tkinter.Label(self.root,text='生猪编号')
        self.rfidEntry = tkinter.Entry(self.root,width=20)
        self.pigLabel = tkinter.Label(self.root,text='评论')
        self.pigEntry = tkinter.Entry(self.root,width=20)
        self.show = tkinter.Text(self.root,width=25,height=10)

        self.sell = tkinter.Button(self.root,text='确认评论',command=self.savePig)
        self.pigMsg = tkinter.Text(self.root,width=20,height=6)
        self.scoreLabel = tkinter.Label(self.root, text='评分')
        self.placeEntry = tkinter.Entry(self.root,width=20)


        threading.Thread(target=rfidMsg,args={self,}).start()

    def place(self):
        self.rfidTip.place(x=20,y=50)
        self.rfidEntry.place(x=100,y=50)

        self.pigEntry.place(x=100,y=100)
        self.pigLabel.place(x=20,y=100)
        self.show.place(x=300,y=160)

        self.sell.place(x=180,y=200)
        self.pigMsg.place(x=300,y=30)

        self.scoreLabel.place(x=20,y=150)
        self.placeEntry.place(x=100,y=150)
        self.root.mainloop()

    def delete(self):

        self.placeEntry.delete(0,tkinter.END)
        self.pigEntry.delete(0,tkinter.END)
        self.rfidEntry.delete(0,tkinter.END)
        self.pigMsg.delete(0.0,tkinter.END)

    def addPig(self):

        addPig(window=self,rfid=self.rfidEntry.get(),place=self.placeEntry.get())

    def savePig(self):
        saveSell(window=self,rfid=self.rfidEntry.get(),talk=self.pigEntry.get(),score=self.placeEntry.get())

        self.rfidEntry.delete(0,tkinter.END)
        self.placeEntry.delete(0,tkinter.END)
        self.pigMsg.delete(0.0,tkinter.END)
        self.pigEntry.delete(0,tkinter.END)
    def setRfid(self,rfidNum):
        self.rfidEntry.delete(0,tkinter.END)
        self.rfidEntry.insert(0,rfidNum)

    def setPigMsg(self,result):
        self.pigMsg.delete(0.0,tkinter.END)
        self.pigMsg.insert(tkinter.END,'生猪编号:' + result[0] + "\n")
        self.pigMsg.insert(tkinter.END, '源产地:' + result[1] + "\n")
        self.pigMsg.insert(tkinter.END, '目前状态:' + result[2] + "\n")
        self.pigMsg.insert(tkinter.END, '售出去向:' + result[3] + "\n")
        self.pigMsg.insert(tkinter.END, '评论:' + result[4] + "\n")
        self.pigMsg.insert(tkinter.END, '评分:' + result[5] + "\n")

    def showSysMsg(self,msg):
        str_time = time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
        self.show.insert(tkinter.END, str_time + msg + "\n")
        self.show.see(tkinter.END)

    def setNone(self,msg):
        self.pigMsg.delete(0.0, tkinter.END)
        self.pigMsg.insert(tkinter.END, msg)
    def exit_sys(self):
        self.root.destroy()

def addPig(window,rfid,place):

    conn.add(window=window,rfid=rfid,place=place)

def saveSell(window,rfid,talk,score):
    conn.sell(window=window,rfidNum=rfid,talk=talk,score=score)

def rfidMsg(window):
    global rfidList

    try:
        # 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
        portx = "COM4"
        # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = 115200
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        timex = 5
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex, bytesize=8)
        while True:
            msg = str(ser.readline())
            msg = msg.replace("b'", "").replace("'", "")
            print(msg)
            rfid = ''
            try:
                rfid = msg.split(">>>")[1][0:8:]
            except :
                continue
            window.showSysMsg(msg='刷卡成功')
            window.setRfid(rfidNum=rfid)
            window.showSysMsg(msg='卡号为：%s'%(rfid))
            # print(conn.query(rfidNum=rfid))
            if conn.query(rfidNum=rfid) :
                window.setPigMsg(result=conn.query(rfidNum=rfid))
            else:
                window.setNone(msg='仓库内还没有该猪的编号，请联系卖猪的友仔')
            window.showSysMsg(msg='操作结束。。。请等待2s')
        ser.close()  # 关闭串口
    except Exception as e:
        print("---异常---：", e)
def main():
    window = win()
    window.place()
if __name__ == '__main__':
    main()