text = "S1A2R3T4I5P9K4E4E86EJ378YRWN"

digits = [ch for ch in text if ch.isdigit()]

print(digits)

numbers = range(1,20)

result = [ n**2 for n in numbers if n % 2 == 0]

print("Even_Squares_num=",result)

print("hello")