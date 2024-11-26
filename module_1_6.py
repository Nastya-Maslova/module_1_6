my_dict = {"Nastya":2006 , "Ben": 1972, "Britney": 1981}
print(my_dict)
print(my_dict["Nastya"])
print(my_dict.get("Katy"))
my_dict.update({"Pole": 2001,"Alex":1999 })
a= my_dict.pop("Ben")
print(a)
print(my_dict)
my_set = {1,2,1,2,"a","b",True,"a",(1,2),(1,2)}
print(my_set)
my_set.update({"c",7})
my_set.remove(1)
print(my_set)