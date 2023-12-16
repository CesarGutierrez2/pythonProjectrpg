# inheritance is an is-a relationship between objects with additional characteristics

# superclass - general class
# subclass - the specialized class which inherit attributes from the general class
# but have their own specific attributes that are not inherited

# multiple inheritance - can inherit attributes and methods for more than one class.

# polymorphism - relates to an objects ability to take different forms.
# essentially a method or attribute in a subclass can have the same name as the method or
# attribute in the superclass, however the subclass will override the superclass when used this way.
# You can also choose which one to use, so if you want the superclass method, not the subclass method,
# you can.

# we can also determine if the object is an instance of the superclass

class Animal:

    def __init__(self, species, age):
        self.species = species
        self.age = age

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


class Dog(Animal):

    def __init__(self, species, age, name):
        Animal.__init__(self, species, age)
        self.name = name
        self.__species = "dog"

    def description(self):
        return f'{self.name} is a {self.__species} and is {self.age} years'

    def speak(self, sound):
        return f"{self.name} says {sound}"


def main():
    name = input("What is your dogs name?: ")
    age = int(input("What is your dogs age?: "))

    your_animal = Dog(0, age, name)
    print(your_animal.description())
    print(your_animal.speak("woof woof"))

    print(isinstance(your_animal, Dog))


if __name__ == '__main__':
    main()
    