
# coding: utf-8

global a
global b
global c
#global d
#global e
#global f

a = [True,True,True,True,False,False,False,False]

b = [True,True,False,False,True,True,False,False]

c = [True,False,True,False,True,False,True,False]

d = list()
e = list()
f = list()

def algoritmo1():
    
    for i in range(8):

        if a[i] and b[i]:
            d.append(True)
        else:
            d.append(False)

    for i in range(8):
        if not(a[i]) and c[i]:
            e.append(True)
        else:
            e.append(False)

    for i in range(8):
        if d[i] or e[i]:
            f.append(1)
        else:
            f.append(0)
    return f

#def algoritmo2():
#    for i in range(8):
        

print(algoritmo1())




