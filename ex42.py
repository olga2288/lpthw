

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make class named Dog that is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## set name1 attribute of self and set it to name
        # Dog has-a name1 = name
        self.name1 = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## get name1 attribute of self and set it to name
        self.name = name

## make class named Person that is-a object
class Person(object):

    def __init__(self, name):
        ## get name2 attribute of self and set it to name
        self.name2 = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## object satan is-a Cat with "Satan" parameter
satan = Cat("Satan")

## ??
mary = Person("Mary")


## From object mary get pet attribute and set it to satan
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
