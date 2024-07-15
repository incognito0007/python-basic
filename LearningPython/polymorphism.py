# it allows object of different classes to behave as object of the same super class

# run time poly -- method overriding
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("bark")

class Cat(Animal):
    def speak(self):
        print("meow")

class Cow(Animal):
    def speak(self):
        print("mooo")


cat = Cat()
dog = Dog()
cow = Cow()

cat.speak()
dog.speak()
cow.speak()



# Compile time polymorphism - achieved through -----
#                         method overloading -- same method with different parameters
#                         operator overloading --

