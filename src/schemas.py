import uuid

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())
 
# условная база данных - набор объектов Person
people = [Person("Tom", 38), Person("Bob", 42), Person("Sam", 28)]