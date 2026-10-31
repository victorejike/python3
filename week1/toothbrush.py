#this understanding how the union works in python 
#what is it use for and why is it so importance
set1 = {1, 2, 3, 4, 5}
set2 = {"apple", "mango", "orange", "banner", "piniple"}
set3 = set1.union(set2)
print(f" the data type: {type(set3)} , and the outcome {set3}")

# and i can use the | bitwise or that we will use in set

app = {1, 2, 3, 4, 5, 6, 7}
app2 = {"python", "is", "fun"}
app3 = app | app2
print(type(app3))
print(app3)