import this

#python update list  what are python update list 
#why do we use them and why are they importance

# tuple are unchangeable meaning that when you have created it you you can not 
#chang them again

# what i did here was to  first  create tuple 
x = ("apple", "bannana", "orange", "mango")
print(x)
print(type(x))
#now i conveted that tuple to a list
y = list(x)
print(y)
print(type(y))
y[1] = "pinanipple"
x = tuple(y)
print(x)
print(type(x))

# i want  unpack a tuple in python lets say i just want to unpack 100 items 
# and i i want to use just three veriable that i assign to the remain job

hundred_numbers = list(range(1,101))

fist, second, *third = hundred_numbers

print(fist)
print(second)
print(third)