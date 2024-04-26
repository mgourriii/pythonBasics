
     
from abc import ABC, abstractmethod 
# abstract base class
#from Calculator import subtract, multiply
 
 
# 1. inherit ABC 
# 2. add abstractmethod as decorator for at least one member function
 
# at least one abstract-method should be present
 
 
# e-commerce website 
# imageUrl, price, rating, reviews
 
class Product(ABC):
    @abstractmethod
    def getImageURL(self):
        pass
 
    @abstractmethod
    def getRatings(self):
        pass
 
    @abstractmethod
    def getReviews(self):
        pass
 
class Car(ABC):
    @abstractmethod
    def getCarBrand(self):
        pass 
 
    @abstractmethod
    def getPrice(self):
        pass
 
    @abstractmethod
    def getColour(self):
        pass
 
    def getNumberOfWheels(self):
        return 4 
 
 
class Audi(Car):
 
    def getCarBrand(self):
        return "Audi"
 
    def getPrice(self):
        return 1800000
 
    def getColour(self):
        return "Black"
 
class Benz(Car):
 
    def getCarBrand(self):
        return "Benz"
 
    def getPrice(self):
        return 2800000
 
    def getColour(self):
        return "White"
 
obj = Audi()
print("Colour:", obj.getColour())
print("Price:", obj.getPrice())
print("Brand name:", obj.getCarBrand())
print("Number of wheels are:", obj.getNumberOfWheels())
 
obj2 = Benz()
print("Colour:", obj2.getColour())
print("Price:", obj2.getPrice())
print("Brand name:", obj2.getCarBrand())
print("Number of wheels are:", obj2.getNumberOfWheels())
 
