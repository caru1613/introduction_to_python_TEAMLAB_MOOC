class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof!'

Animals = [Cat('A'), Cat('B'), Dog('C')]

for animal in Animals:
    print(animal.name + ": " + animal.talk())