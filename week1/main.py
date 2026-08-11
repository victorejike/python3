#list in python

ListName = ["apple", "orange", "mango", "cashew", "pawpaw"]
ListNameInt = [1, 2, 10, 30, 40, 50, 60, 70]
ListNameBool = [True, False, True, False]
print(ListName, len(ListName))
print(ListNameInt, len(ListNameInt))
print(ListNameBool, len(ListNameBool))

List1 = ["orange", 6, True, "apple"]

print([type(item) for item in List1])

Constructor = list(["apple", 65, "langauge", True])
print([type(fruit) for fruit in Constructor])

Fruit = ['mango', 'orange', 'cashew', 'pawpaw', 'apple']
print(Fruit, "the first example :")
Fruit[0] = "kawki"
print(Fruit)
Fruit[1:3] = ["pinnple", "game" ]
print(Fruit)
