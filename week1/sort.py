#what is list sorting in python
#python provide two primary ways to sort a list

numbers = [2, 1, 5 , 4, 3, 6, 8, 7]
print(numbers)
numbers.sort()
print(numbers)
print("=========================")
#this is to create a new list 

num = [5, 3, 4, 1, 2, 6]
print(num)
num = sorted(num)
print(num)
print("=============================")

word = ["victor", "Ejike", "nmesomma", "Khalifa", "james"]
print(word)
word.sort(key=str.capitalize)
print(word)
print("==========================")


thislist = ["orang", "apple", "mango"]
