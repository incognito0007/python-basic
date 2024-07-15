# Types of polymorphism
#
#     1. Duck Typing
#     2. Operator Overloading
#     3. Method overloading
#     4. Method Overriding

# ----------------------- DUCK TYPING -----------------------

# class PyCharm:
#     def execute(self):
#         print("compiling")
#         print("running")
#
# class MyEditor:
#     def execute(self):
#         print("spell Check")
#         print("Convention Check")
#         print("compiling")
#         print("running")
#
#
# class Laptop:
#     def code(self, ide):
#         ide.execute()
#
#
# ide = PyCharm()
#
# lap1 = Laptop()
# lap1.code(ide)
#
# ide = MyEditor()
# lap1.code(ide)




# ----------------------- OPERATOR OVERLOADING -----------------------


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2

print(s3.m1)