#what is a set in python and why do we use it
# set are used to store multiple  item in a single variable
# set is python built in data type in python used to store collection of data
#the remain three(3) list, tuple, dictionary

myset = {"victor", "mick", "huller", "linkon","lawyer", "court"}
print(myset)
print(type(myset))


print("================================")

list_set = {True, 1}
list0_set = {1, True}
print(list0_set)
print(list_set)
print("====================================")

list2_set = {False, 0}
list3_set = {0, False}
print(list3_set)
print(list2_set)


print("==================================")
cart_name = {"toyota", "mazad", "mercdecbenz", "bob"}
user_name = {"victor", "ejike", "nmesomma", "bob"}

flagg = user_name.intersection(cart_name)
print(flagg)


list_of_set = {"user1", "user2", "user3", "user4", "user5", "user6"}
print(list_of_set)
print("===== now i will add some item to the set that we currently have to see how to use the set()===")
list_of_set.add("user")
print(list_of_set)


print("=====================")

user_name1 = {"john", "searh", "doe", "mick", "wizdom"}
list2_set.update(user_name1)
print(list2_set)