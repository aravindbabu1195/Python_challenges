#simple Interest
def simple_interest(p,n,r):
    s=p*n*r
    sp=s/100
    return (sp)
x=int(input("Enter value of p :"))
y=int(input("Enter value of n :"))
z=int(input("Enter value of r :"))
print(simple_interest(x,y,z))