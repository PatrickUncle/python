from rfid import mysqldb as db
import serial
import threading
import time
import tkinter

rfidList = []
conn = db.database()

class win:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.exit_sys)
        self.root.title('图书档案管理系统')
        self.root.geometry('500x300')
        self.rfidTip = tkinter.Label(self.root,text='rfid卡号')
        self.rfidEntry = tkinter.Entry(self.root,width=20)
        self.fileLabel = tkinter.Label(self.root,text='档案名称')
        self.fileEntry = tkinter.Entry(self.root,width=20)
        self.show = tkinter.Text(self.root,width=40,height=10)

        self.add = tkinter.Button(self.root, text='添加档案', command=self.add)
        self.upload = tkinter.Button(self.root,text='入档',command=self.upload)

        self.down = tkinter.Button(self.root,text='出档',command=self.down)

        self.fileMsg = tkinter.Text(self.root,width=15,height=10)

        threading.Thread(target=rfidMsg,args={self,}).start()

    def place(self):
        self.rfidTip.place(x=100,y=180)
        self.rfidEntry.place(x=150,y=180)

        self.fileEntry.place(x=150,y=230)
        self.fileLabel.place(x=100,y=230)
        self.show.place(x=180,y=10)

        self.upload.place(x=400,y=180)
        self.down.place(x=400, y=220)
        self.add.place(x=320,y=180)
        self.fileMsg.place(x=50,y=10)
        self.root.mainloop()

    def setRfid(self,rfidNum):
        self.rfidEntry.delete(0,tkinter.END)
        self.rfidEntry.insert(0,rfidNum)

    def setFileName(self,fileName):
        self.fileEntry.delete(0,tkinter.END)
        self.fileEntry.insert(0,fileName)

    def showSysMsg(self,msg):
        # str_time = time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
        # self.show.insert(tkinter.END, str_time + msg + "\n")
        self.show.insert(tkinter.END, msg + "\n")
        self.show.see(tkinter.END)

    def upload(self):

        conn.upload(window=self, rfidNum=self.rfidEntry.get())

    def add(self):
        conn.add(window=self,rfidNum=self.rfidEntry.get(),fileName=self.fileEntry.get())

    def down(self):

        conn.down(window=self,rfidNum=self.rfidEntry.get())

    def showFileMsg(self,result):
        self.fileMsg.delete(0.0, tkinter.END)
        self.fileMsg.insert(tkinter.END, '档案编号:' + result[0] + "\n")
        self.fileMsg.insert(tkinter.END, '档案名称:' + result[1] + "\n")
        self.fileMsg.insert(tkinter.END, '目前状态:' + str(result[2]) + "\n")
        self.fileMsg.insert(tkinter.END, '目前位置:' + str(result[3]) + "\n")

    def setFileMsg(self,msg):
        self.fileMsg.delete(0.0, tkinter.END)
        self.fileMsg.insert(tkinter.END, msg)

    def exit_sys(self):
        self.root.destroy()

# def databaseControl(window,conn,rfidNum):
#     if conn.getStatus(rfidNum=rfidNum) == 0:#表示不在仓库内
#         conn.upload(window=window,rfidNum=rfidNum)
#     else:
#         conn.down(window=window,rfidNum=rfidNum)

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
            # print("正在接受刷卡。。。")
            # window.showSysMsg(msg='正在接受刷卡')
            msg = str(ser.readline())
            msg = msg.replace("b'", "").replace("'", "")
            control = ''
            try:
                control = msg.split(">>>")[1][0:8:]
            except:
                continue
            # print("刷卡成功")
            window.showSysMsg(msg='刷卡成功')
            # print('卡号为：', control)

            window.setRfid(rfidNum=control)
            window.showSysMsg(msg='卡号为：%s'%(control))
            if conn.query(rfidNum=control) :
                window.showFileMsg(result=conn.query(rfidNum=control))
                fileName = conn.query(rfidNum=control)[1]
                window.setFileName(fileName=fileName)
            else:
                window.setFileMsg(msg='该档案还未入档，请输入档案名入档')
            # databaseControl(window=window,conn=conn,rfidNum=control)
            # print('操作结束。。。请等待2s')
            window.showSysMsg(msg='操作结束。。。请等待2s')

        ser.close()  # 关闭串口
    except Exception as e:
        print("---异常---：", e)
def main():
    window = win()
    window.place()
if __name__ == '__main__':
    main()