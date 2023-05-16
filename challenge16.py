def fun1(p):
    d=p-p*10/100
    return d
def fun2(p):
    c=p-p*5/100
    return c


p=int(input("Enter product price :"))

result=print(fun2(fun1(p)))


