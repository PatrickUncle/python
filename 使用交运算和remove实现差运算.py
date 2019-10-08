s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

jiaoji = s1 & s2
print(jiaoji)

its = iter(jiaoji)

for it in its:
    s1.remove(it)
print(s1)