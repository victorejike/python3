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