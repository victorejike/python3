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