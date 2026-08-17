#"' printalphabet
#Instructions
#Write a program that prints the Latin alphabet in lowercase on a single line.

#A line is a sequence of characters preceding the end of line character ('\n').

#Usage
#$ go run .
#abcdefghijklmnopqrstuvwxyz
#$
#Notions
#01-edu/z01 

for i in range(ord('a'), ord('z') + 1):
	print(chr(i), end="")
print()
