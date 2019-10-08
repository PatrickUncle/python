
def hello2():
    a = "a"
    if a == "c":
        print("hello")
    else:
        raise Exception("error2")
def hello():
    a = "a"
    if a == 'C':
        print("hello")
    else:
        hello2()
if __name__ == '__main__':
    # try:
    hello()
    # except Exception as e:
    #     print(e.__str__())

