class A:

    def __init__(self):
        print("Init in A")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):

    def __init__(self):
        super().__init__()
        print("Init in B")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C:
    def __init__(self):
        print("Init in C")

class D(C, A):
    def __init__(self):
        super().__init__()  #always call the leftmost or first class init and same will go for methods/functions
        print("Init in D")


    def feature(self):
        super().feature1()


a1 = A()

b1 = B()

c1 = C()

d1 = D()
d1.feature()