class Animals:
    def __init__(self):
        return
    
    def eat(self):
        print('eat')
        
    def talk(self):
        print('talk')
        
class Cat(Animals):
    def talk(self):
        print('Meows')
        
    def move(self):
        print('Jump')
        
class Dog(Animals):
    def talk(self):
        print('Won')
        
muffin = Cat()
muffin.talk()
muffin.move()
muffin.eat()

tom = Dog()
tom.talk()
tom.eat()