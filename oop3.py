class Student:
    college = "SB COLLEGE ARA" #class variable

    def __init__(self,name:str,age:int,sem:int,email:str):
        self.name=name
        self.age=age                  #instance variable
        self.sem=sem
        self.email=email
s1=Student("Raj",22,4,"Saurabh123@gmail.com")
print(s1.name)
print(s1.age)
print(s1.sem)
print(s1.email)

print(s1.college)
print(Student.college)