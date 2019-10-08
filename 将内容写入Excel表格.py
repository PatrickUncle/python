import xlwt

newTable = "test.xls"
wb = xlwt.Workbook(encoding="utf-8")
ws = wb.add_sheet("sheet1")
headData = ["第一","第二","第三","第四"]
for colnum in range(0,4):
    ws.write(0,colnum,headData[colnum])
for num in range(1,101):
    for j in range(0,5):
        ws.write(num,j,num)
wb.save(r"C:\Users\ASUSPC\Desktop\aaaa.xls")

