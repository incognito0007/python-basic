class Computer:

    def __init__(self, cpu, ram):
        print("in init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)



comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 3', 8)
comp1.config()
comp2.config()