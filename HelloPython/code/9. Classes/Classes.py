class Person:
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name
        self.display()
    
    def display(self):
        print('You are a', self.gender)
        print('Your name is:', self.name)
        return
    
    def setAge(self,age):
        self.age = age
        
    def displayAge(self):
        print('Age is:', self.age)
        

people = Person('Male', 'Alex')
people.display()

people.setAge(35)
people.displayAge()