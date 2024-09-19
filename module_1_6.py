my_dist={"Maksim": 2005, "Roman": 2008}
print(my_dist)
print(my_dist["Maksim"])
my_dist["Arsenie"] = 2010
print(my_dist["Arsenie"])
my_dist.update({"Alex": 1999,
                "Dima" : 1987})
print(my_dist.pop("Roman"))
print(my_dist)

my_set={3,3,True, "str", True}
print(my_set)
my_set.add(6)
my_set.add("maksim")
my_set.discard("maksim")
print(my_set)