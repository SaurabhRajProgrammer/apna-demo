class Student:
    def __init__(self,fullname):
        self.name=fullname
#Create the method(function):        
    def hello(self):
            print("Welcome",self.name)
s1=Student("Surabh Raj")
s1.hello()   #call the method        