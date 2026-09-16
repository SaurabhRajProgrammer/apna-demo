#normal code

numbers=[1,2,3,4,5,6,7]
squares=[]

for num in numbers:
    squares.append(num**2)
print(squares)    

#   USING LIST-COMPREHENSIONS

numbers1=[1,2,3,4,5,6,7]
squares1 =[num**2 for num in numbers1]
print(squares1)
