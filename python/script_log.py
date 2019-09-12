
# coding: utf-8

import os


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

def algoritmo2():
    for i in range(8):
        if a[i] and c[i]:
            d.append(True)
        else:
            d.append(False)

    for i in range(8):
        if b[i] and (not c[i]):
            e.append(True)
        else:
            e.append(False)
    
    for i in range(8):
        if d[i] or e[i]:

            f.append(1)

        else:
            f.append(0)
            
    return f

        

print("\t\tMenu principal\n")
print("Elija el algoritmo a resolver: ")
print("1.- Algoritmo 1\n2.- Algoritmo 2")
opcion = int(input())

if opcion == 1:
    print("El resultado es: ")
    print(algoritmo1())

elif opcion == 2:
    print("El resultado es: ")
    print(algoritmo2())
else:
    print("Opción no válida.\n\n")

print("Continuar? S/N")
cnt = input()

while cnt.upper() != 'N':
    os.system("clear")
    d.clear()
    e.clear()
    f.clear()
    print("\t\tMenu principal\n")
    print("Elija el algoritmo a resolver: ")
    print("1.- Algoritmo 1\n2.- Algoritmo 2")
    opcion = int(input())

    if opcion == 1:
        print("El resultado es: ")
        print(algoritmo1())

    elif opcion == 2:
        print("El resultado es: ")
        print(algoritmo2())
    else:
        print("Opción no válida.\n\n")

    print("Continuar? S/N")
    cnt = input()




