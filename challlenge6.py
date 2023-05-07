# To print 12 months based on thier coresponding numbers
Month=["1.January","2.February","3.March","4.April","5.May","6.June","7.July","8.August","9.September","10.october","11.November","12.December"]
for i in Month:
    print(i)

Choice=int(input("Enter your choice"))
if Choice==1:
    print("January")
elif Choice==2:
    print("February")
elif Choice==3:
    print("March")
elif Choice==4:
    print("April")
elif Choice==5:
    print("May")
elif Choice==6:
    print("June")
elif Choice==7:
    print("July")
elif Choice==8:
    print("August")
elif Choice==9:
    print("September")
elif Choice==10:
    print("October")
elif Choice==11:
    print("November")
elif Choice==12:
    print("December")
else:
    print("You Choice a invalid Month ")