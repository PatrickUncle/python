#操作代码字典
dir_action = {
    'find' : 1,
    'add' : 2,
    'delete' : 3,
    'update' : 4
}

#查询
def find(where,table,*what):
    print("查询")

#增加
def add(table,*person):
    print("add")

#删除
def delete(table,id):
    print("delete")

#更新
def update(table,set,where):
    print("update")

#逻辑控制与语句识别
def main():
    global dir_action
    print("请输入你的语句：\n")
    sql = input()
    sql_list = sql.split(" ")
    print(sql_list)

    action = dir_action.get(sql_list[0])
    what = []
    print(sql_list.index('from'))
    table = dir_action.get(sql_list[sql_list.index('from') + 1])
    where = dir_action.get(sql_list[sql_list.index('where') + 1])
    set = []

    if action == 1:
        find(where,table,what)
    elif action == 2:
        add(table)
    elif action == 3:
        delete(table,id)
    elif action == 4 :
        update(table,set,where)


#主程序执行时，执行mian函数
if __name__ == '__main__':
    main()