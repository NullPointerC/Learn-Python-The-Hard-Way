# 对象,类及从属关系

## Animal is-a object(yes, sort of confusing) look at the eatra credit
class Animal(object):
    pass


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## 把Dog类name变量设置为传入的name变量
        self.name = name


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        self.name = name


## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        # Person has a pet of some kind
        self.pet = None


## ??
class Empolyee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Empolyee, self).__init__(name)
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

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Empolyee("Frank", 120000)

## ??
frank.pet = rover

## ???
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
