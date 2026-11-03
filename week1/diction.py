car = {
    "brand" : ["ford", "toyota", "kia"],
    "model" : ["avenges", "hellux", "sonata"],
    "year" : ["2026", "2018"]
}

print(len(car["year"]))
x = car.get("model")
print(x)
print("===================================")
y = car.keys()
print(y)