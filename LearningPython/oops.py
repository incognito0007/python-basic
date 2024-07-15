# class -- blueprint for an object
# object -- an instance of type class

# class Student:
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
# #
# student1 = Student()
# student1.set_name("Ankit Anand")
# print(student1.get_name())
#
# student2 = Student()
# student2.set_name("Sanskruti Mali")
# print(student2.name)

# class Rectangle:
#
#     def set_dimension(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# rect1 = Rectangle()
# h = int(input())
# w = int(input())
# rect1.set_dimension(w, h)
# print(rect1.area())
# print(rect1.perimeter())


# class cunstructor : special function that gets invoked every time an
#                     object is created for that class.

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def set_dimension(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# h = int(input())
# w = int(input())
# rect1 = Rectangle(w, h)
# # rect1.set_dimension(w, h)
# print(rect1.area())
# print(rect1.perimeter())



# access modifiers -- control the visibility/access of thr class attributes
#                     and functions.


# public modifier
# class ABC:
#     def __init__(self):
#         self.public_attribute = None
#
#     def public_function():
#         pass
#
# obj1 = ABC()
# obj1.public_attribute
# obj1.public_function()


# Private modifier
# class ABC:
#     def __init__(self):
#         self.__private_attribute = None
#
#     def __private_function():
#         pass



# Protected Modifier
# class ABC:
#     def __init__(self):
#         self._protected_attribute = None
#
#     def _protected_function():
#         pass

