file = open("dubodata.txt",mode="r",encoding="utf-8")

weizhi = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
}
first_data = file.readline().replace("\n","").split("-")[0]
count = 0
while True:
    data = file.readline().replace("\n","")
    if data == "1":
        break
    data_list = data.split("-")
    weizhi[str(data_list.index(first_data)+1)] = weizhi[str(data_list.index(first_data)+1)] +1
    first_data = data.split("-")[0]
    count+=1

print(weizhi,count)