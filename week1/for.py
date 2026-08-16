#what i want to create is comprehension

fruits =['apple', 'mango', 'banana', 'cherry', 'kiwi', 'cashaw']
print(fruits)
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = ["apple", "mango", "cashew", "johe"]
new = [x for x in newlist if x != True]
print(new)
newlist = [new.upper() for new in newlist ]
print(newlist)