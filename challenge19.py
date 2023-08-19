class vehicles:
    def __init__(self,specs):
        self.specs=specs
    def getspecs(self):
        self.specs="Petrol Vehicles"
    def displayspecs(self):
        print("Vehicle specification :",self.specs)

class car(vehicles):
    def getcar(self):
        self.specs=input("Enter car specification :")
    def dispcar(self):
        print("Car specification :",self.specs)
class bike(vehicles):
    def getbike(self):
        self.specs=input("Enter Bike specification :")
    def dispbike(self):
        print("Bike specification :",self.specs)
obj=bike('')
obj.getspecs()
obj.displayspecs()
obj.getbike()
obj.dispbike()

obj1=car('')
obj1.getspecs()
obj1.displayspecs()
obj1.getcar()
obj1.dispcar()