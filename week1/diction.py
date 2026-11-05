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

thisdic = {
    "company": ["toyota", "kia", "mazad", "mecardec-benze"],
    "type" : ["hellux", "sonata", "mazad", "c- class"],
    "year": [2012, 2022, 2019, 2025]
}
print(thisdic)

x = thisdic.keys()

print(x)

thisdic["name"] = "cars"

print(x)
y = thisdic.values()
print(y)
thisdic["coloor"] =  "red"
print(y)
thisdic.keys()
print(y)
#this is to get items in a dictionary 
# this is to test if will throughly understand  it or not 
# the item method will reture the item  on tuple
