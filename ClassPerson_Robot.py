
class Person:
    name = ''
    personility = ''
    isSitting = bool()
    robotOwned = ''

    def __init__(self, n, p, i):
        self.name = n
        self.personility = p
        self.isSitting = i
    
    def sitDown(self):
        self.isSitting = True
        
    def standUp(self):
        self.isSitting = False

class Robot:
    name = ''
    color = ''
    weight = 0

    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    
    def introduceSelf(self):
        print('I am a robot '+ self.name)


r1 = Robot('Tom', 'Red', 30)
r2 = Robot('Jerry', 'Blue', 40)



r1.introduceSelf()
r2.introduceSelf()

p1 = Person("Alice", "Smart", False)
p2 = Person("Divya", "Kind", True)

#setting robot owners
p1.robotOwned = r2
p2.robotOwned = r1


#Calling robot class functoins with person object
p1.robotOwned.introduceSelf()
p2.robotOwned.introduceSelf()