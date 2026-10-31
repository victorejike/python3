element_of_item = ("user", "name", "password", "phone", "number", "address")
print(element_of_item)
word = element_of_item.count("name")
print(word)

total = element_of_item
print(len(total))

animal = ("dog", "bird", "goat", "cow")
if "pig" in animal:
    print(animal.index("dog"))
else:
    print(f"{animal} not found")



number = (10, 20, 30, 20, 40,)
print(number.index(20))
print(number.index(20, 2))
print(number.index(20,2))

print("=======================================================")
fruits = ("pawpaw", "mango", "apple","kiwi", "melon", "bannana")
print(fruits[2:5])