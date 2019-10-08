def get_num():
    i = 0
    while True:
        yield
        i+=2
        print(i)
o = get_num()
o.__next__()
o.__next__()
o.__next__()
o.__next__()