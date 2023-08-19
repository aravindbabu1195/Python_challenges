class hospital:
    def __init__(self,name,):
        self.name=name
    def admin(self):
        self.adminname=input("Enter Admin name :")
        self.doctorname=input("Enter Doctor name :")
        self.nursename = input("Enter Nurse name :")
        self.departmentname = input("Enter Department name :")

class department(hospital):
    def get(self):
        print("Admin Name :",self.adminname)
        print("Doctor Name :",self.doctorname)
        print("Nurse Name :",self.nursename)
        print("Department Name :",self.departmentname)

class paitentward(department):
    def getpaite(self):
        self.name=input("Enter Paitent name :")
        self.age=int(input("Enter age :"))
    def dippaite(self):
        print("Paitent Name :",self.name)
        print("Paitent Age :",self.age)
obj=paitentward('')
obj.admin()
obj.get()
obj.getpaite()
obj.dippaite()