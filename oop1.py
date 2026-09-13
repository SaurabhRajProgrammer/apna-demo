class Student:
    def __init__(self,name,age,email,is_student):
        self.name=name
        self.age=age
        self.email=email
        self.is_student=is_student

s1=Student("Saurabh",21,"Saurabhraj1540@gmail.com","True")

print(s1.name)
print(s1.age)
print(s1.email)
print(s1.is_student)