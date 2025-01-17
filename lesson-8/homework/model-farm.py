class Animal:
    def __init__(self, name, age, sound):
        self._name = name
        self._age = age
        self._sound = sound
    
    def eat(self, food):
        print(f'{self._name} eating {food}')
    
    def sleep(self):
        print(f'{self._name} eating')

    def sound(self):
        print(f'{self._name} says {self._sound}')

class Cow(Animal):
    def __init__(self, name,age):
        super().__init__(name,age,"MOO")

    def milk(self):
        print(f'{self._name} giving milk')

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "bi bi")
    
    def fly(self):
        print(f'{self._name} is flying')


def farm_demo():
    cow = Cow("barnie",1)
    bird = Bird("sava",2)

    cow.sound()
    cow.eat("grass")
    cow.milk()
    cow.sleep()
    bird.sound()
    bird.eat("seeds")
    bird.fly()
    bird.sleep()

farm_demo()