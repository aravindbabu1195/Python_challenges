n=int(input("Enter the index numeber for fibonacci :"))
a=0
b=1
s=0

for x in range(n):
    print(s,end=" ")
    s=a+b
    b=a
    a=s
# fibonacci
