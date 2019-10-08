
def zsq(func):
    def inner(strs,fuhao):
        print(fuhao * 30,end="")
        func(strs,fuhao)
        print(fuhao * 30,end="")
    return inner

@zsq
def needzs(strs,fuhao):
    print(strs,end="")

needzs("好","+")
