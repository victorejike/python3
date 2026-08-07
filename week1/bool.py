x = "hello"
y = "victor"
print(bool(x))
print(bool(y))

class myclass():
    def _len_(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myfunction():
    return False

if myfunction():
    print("Yes")
else:
    print("No!")


j = 200
print(isinstance(x, int))

print(10 > 7)
print(10 == 9)

x = 20 
y = 10 
print(x // y)

