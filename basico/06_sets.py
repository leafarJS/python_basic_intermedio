### SETS ###
my_set:set = set()
my_other_set:set = {}
print(type(my_set))
print(type(my_other_set)) # class dict

my_other_set = {"jorge", "callejo", 45}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("rafael")
print(my_other_set) # TODO un set no es una estructura ordenada

my_other_set.add("rafael")
print(my_other_set) # TODO un set no admite elementos repetidos 

my_other_set.add("Rafael")
print(my_other_set)

print("Moure" in my_other_set)
print("rafael" in my_other_set)

my_other_set.remove("Rafael")
print(my_other_set)

my_other_set.clear() # limpia los elementos del set 
print(my_other_set)
print(len(my_other_set))


my_other_set = {"jorge", "callejo", 45}
my_other_set.update()
print(my_other_set)

del my_other_set # elimina todo el set
print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"jorge", "callejo", 45}
my_list = list(my_set)
print(my_list)
print(my_list[2])


my_other_set_1 = {"css", "html", "sql"} 
my_other_set_2 = {"python", "javascript", "R"}

new_set = my_other_set_1.union(my_other_set_2)
print(new_set)

new_set.union({"hanaDB"})
print(new_set)

print(my_set.difference(my_other_set_1))