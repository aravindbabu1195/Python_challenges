li=[10,20,30,40,50]
newstring="my numbers :{0} , {1} ,{2}".format(li[2],li[0],li[1])
print(newstring)

list1=[1,2,3,4,5,6,7,8]
print(list1[2:7])


tuple1=(10,20,30,40,50,60,70)
y=list(tuple1)
print(y)
y.insert(2,90)
print(y)
y.append(100)
print(y)
print(y[-2])