# _*_ codding: utf-8 _*_
from tabulate import tabulate
DB_FILE = "staff_table.db"
DATA_SET = {}
COLUMNS = []
query_data = []
def where_parse(code):
    operators = {
        '>': op_bigger,
        '<': op_smaller,
        '=': op_eq,
        'like': op_like
    }
    query_list = []
    if "where" in code:

        condition = code.split("where")[1]
        for key, op_func in operators.items():
            if key in condition:
                q_name, q_condition = condition.split(key)
                query_list = op_func(q_name.strip(), q_condition)
                break
    else:
        for index,val in enumerate(DATA_SET["id"]):
            record = []
            for column in COLUMNS:
                record.append(DATA_SET[column][index])
            query_list.append(record)
    return query_list
def save():
    content = ""
    for index,column in enumerate(COLUMNS):
        if index > 0:
            content += "," + column
        else:
            content += column
    for index, val in enumerate(DATA_SET["id"]):
        content += "\n"
        record = []
        for i,column in enumerate(COLUMNS):
            if i > 0:
                content += "," + DATA_SET[column][index]
            else:
                content += str(DATA_SET[column][index])
    with open(DB_FILE,"w") as f :
        f.write(content)
def select_func(code):
    query_list = where_parse(code)
    show_columns = [i.strip() for i in code.split("from")[0].split("select")[1].split(",")]
    records = []
    for q in query_list:
        record = []
        for column in show_columns:
            record.append(q[COLUMNS.index(column)])
        print(record)
        records.append(record)
    print(tabulate(records,headers=show_columns,tablefmt="grid"))
def op_bigger(q_name,q_condition):
    """
    大于的时候
    :param q_name:
    :param q_condition:
    :return:
    """
    records = []
    for index,col_val in enumerate(DATA_SET[q_name]):
        if col_val > q_condition:
            record = []
            for column in COLUMNS:
                record.append(DATA_SET[column][index])
            records.append(record)
    return records
def op_smaller(q_name,q_condition):
    records = []
    for index, col_val in enumerate(DATA_SET[q_name]):
        if col_val < q_condition:
            record = []
            for column in COLUMNS:
                record.append(DATA_SET[column][index])
            records.append(record)
    return records
def op_eq(q_name,q_condition):
    records = []
    for index, col_val in enumerate(DATA_SET[q_name]):
        if col_val == q_condition:
            record = []
            for column in COLUMNS:
                record.append(DATA_SET[column][index])
            records.append(record)
    return records
def op_like(q_name,q_condition):
    records = []
    for index, col_val in enumerate(DATA_SET[q_name]):
        if col_val in q_condition:
            record = []
            for column in COLUMNS:
                record.append(DATA_SET[column][index])
            records.append(record)
    return records
def insert_func(code):
    key_val = [i.strip() for i in code.split("(")[1].split(")")[0].split(",")]
    id = len(DATA_SET["id"]) + 1
    DATA_SET["id"].append(id)
    for kv in key_val:
        key,val = [i.strip() for i in kv.split("=")]
        DATA_SET[key].append(val)
    save()
def update_func(code):
    query_list = where_parse(code)
    if "where" in code:
        column,parameter = [i.strip() for i in code.split("where")[0].split("set")[1].split("=")]
    else:
        column,parameter = [i.strip() for i in code.split("set")[1].split("=")]
    for q in query_list:
        row_index = DATA_SET["id"].index(q[0])
        DATA_SET[column][row_index] = parameter
    save()
def delete_func(code):
    query_data = where_parse(code)
    for q in query_data:
        id = DATA_SET["id"].index(q[0])
        for column in COLUMNS:
            del DATA_SET[column][id]
    save()
def init():
    """
    将文件内容读入内存（字典类型）{'id': ['1', '2'], 'name': ['pzy', 'psh'], 'age': ['20', '20'], 'dept': ['IT', 'IT']}
    :return: None
    """
    with open(DB_FILE) as f:
        global COLUMNS
        COLUMNS = [i.strip() for i in f.readline().split(",")]
        for col_name in COLUMNS:
            DATA_SET[col_name] = []
        for row in f.readlines():
            col_data = [i.strip() for i in row.strip().split(",")]
            for index,col_name in enumerate(COLUMNS):
                DATA_SET[col_name].append(col_data[index])

def main():
    type_func = {
        "select": select_func,
        "insert": insert_func,
        "update": update_func,
        "delete": delete_func
    }
    init()  # 初始化
    code = input("<staff_table>:")
    type = code.split(" ")[0]
    type_func[type](code)

if __name__ == '__main__':
    main()