class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

class Korean(Person):
    pass

first_korean = Korean("BY", 39)
print(first_korean.name)