mylist = ("apple",)
print(len(mylist))

def myfun():
    x = int(input("what's x ? "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def  is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

myfun()
