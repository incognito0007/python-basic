

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Ankit", 1)
s2 = Student("Sanskruti", 2)

s1.show()
s2.show()

# lap1 = s1.lap
# lap2 = s2.lap



lap1 = Student.laptop()

lap1.show()