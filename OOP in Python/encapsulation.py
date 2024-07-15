# Access Modifiers ----- Encapsulation

# Encapsulation ------ fundamental principle in OOP that focuses on
# bundling data and the methods that operate on that data into a single unit
# called a class. It allows you to control the access and visibility
# of the data and methods, providing a way to protect and
# organize your code

# private -- methods which are only accessible within a class

class Person:
    # Cunstructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print("person name is ", self.__name)
        print("person age is ", self.__age)


person = Person("Ankit", 22)
person.display_info()

# Protected --

class PersonOne:
    # Cunstructor
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Student(PersonOne):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print("person name is ", self._name)
        print("person age is ", self._age)

Student1 = Student("Ankit", 22)
Student1.display_info()

class PersonTwo:
    # Cunstructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("person name is ", self.name)
        print("person age is ", self.age)

a = PersonTwo("sanu", 22)
a.display_info()