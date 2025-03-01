class BMW():
    def max_speed(self):
        print("My max speedis 200mph")
    def fuel_type(self):
        print("My fuel type is diesel")

    
        
class Mercedes:
    def max_speed(self):
        print("My max speedis 210mph")
    def fuel_type(self):
        print("My fuel type is petrol")
obj=BMW()
obj1=Mercedes()
for i in (obj,obj1):
    i.max_speed()
    i.fuel_type()


    