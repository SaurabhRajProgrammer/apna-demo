#using list-comprehensions:=

names = ["saurabh","raj","nayra","anshika"]

upper= [name.upper() for name in names]

val = [len(name) for name in names]

print(upper)

print(val)