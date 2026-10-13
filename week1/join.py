#what is join lists
"""
in python  the phrase join list  usally refers to one of two 
different concept depending on what  you  want 
to achieve
1 converting a list  of single string using .join() method
2 combining multple list togther into one larger list (concatenation)
 """

words = ["victor", "is", "awesome"]

Result_space = " " .join(words)
print(Result_space)

print("==================this is the first result ================================")

Result_comma = "," .join(words)
print(Result_comma)


# now lets add for numbers  the list  must contain only string if your list contain  integers
# you must convert them to string first using a list comprehension or map()
# 



numbers = [1, 2, 3, 4, 5]

result = "-".join(map(str, numbers))
print(result)


list_a = [1, 2, 3]
list_b = [10, 20, 30]

summed = map(lambda x, y: x + y, list_a + list_b)
print(list(summed))