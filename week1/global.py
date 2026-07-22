x = "awesome"

def myfun():
    global x
    x = "?"
    print("hello world" + x)

myfun()
print("victor" + x)