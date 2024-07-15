

# ---------------------------- CLASS AND OBJECT ----------------------------------

class Student:
    def __init__(self, name, PRN):
        self.name = name
        self.PRN = PRN

    def info(self):
        print("NAME:", self.name, "PRN:", self.PRN)

s1 = Student("Ankit Anand", 22010787)
s2 = Student("Sanskruti Mali", 22010083)

s1.info()
s2.info()



# ------------------------------CUNSTRUCTOR-------------------

class Car:

    def __init__(self):
        self.model = "BMW"
        self.milage = 15

    def update(self):
        self.model = "Nisaan"

    def compare(self, other):
        if self.model == other.model:
            return True
        else:
            return False


c1 = Car()
c2 = Car()

print(c1.model, c1.milage)
print(c2.model, c2.milage)

# c2.model = "Skoda"
#
# print(c1.model, c1.milage)
# print(c2.model, c2.milage)
#
# c2.update()
#
# print(c2.model, c2.milage)

if c1.compare(c2):
    print("Both car are same")
else:
    print("Both car are not same")


# ----------------------------------- METHODS --------------------------------

class School:

    university = "SPPU"

    def __init__(self):
        self.name = "VIIT"
        self.grade = "A"

    @classmethod
    def getUni(cls):
        return cls.university

    @staticmethod
    def revision():
        print("this is a static method")

s1 = School()

print(s1.name, s1.grade)
print(s1.getUni())

School.revision()


# ---------------------------- INNER CLASS --------------------------------

class Employee:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    class Laptop:

        def __init__(self, name, cpu):
            self.name = name
            self.cpu = cpu

e1 = Employee("Ankit", 43)
l1 = Employee.Laptop("Lenove", "Ryzen")

print(e1.name, e1.ID, l1.name, l1.cpu)