class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
    def display(self):
        print(self.name, self.age)
p1 = Person("John", 36)
p1.display()
# print(p1.name)
# print(p1.age)
