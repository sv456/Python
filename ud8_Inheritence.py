class Parent():
    def __init__(self,last_name,eye_color):
        print "parent constructor called"
        self.lastname=last_name
        self.eyecolor=eye_color

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print "child constructor called"
        Parent.__init__(self,last_name,eye_color)
        self.numberoftoys=number_of_toys

sold=Child('Mysrus','blue',5)
print sold.numberoftoys
