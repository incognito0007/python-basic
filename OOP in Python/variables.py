

class Cars:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Cars()
c2 = Cars()

c1.mil = 8   #to change a instance variable

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

Cars.wheels = 5   #to change a class variable

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)