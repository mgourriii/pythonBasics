

class  Car:
    def __init__(self, speed):
        self.speed = speed
        self.brand = "Audi"
        self.wheelsCount = 4

obj1 = Car(110) 
print(obj1.brand)
print(obj1.speed)
obj1.wheelsCount = 6
print(obj1.wheelsCount) 
obj1.speed = 90
print(obj1.speed)
print(obj1.brand)
obj1.brand = "Benz" 
print(obj1.brand)     
      
