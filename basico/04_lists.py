### Lists ###
# una lista es similar a un arreglo o array 
my_list:list[int] = list() # con una lista podemos hacer operaciones
my_other_list:list[int, float, str] = [46, 1.76, "jorge", "callejo"] 
my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))
print(type(my_list))

print(my_other_list)
print(len(my_other_list))
print(type(my_other_list))

print("o_o_o_o_o_o_o_o_o_")
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_other_list.count("callejo"))
print(my_list.count(30)) # contar la cantidad de elementos que coinciden dentro de la lista 
# print(my_other_list[-4]) IndexError
# print(my_other_list[-5]) IndexError
# print(my_other_list.count()) Error 

age, height, name, lastname = my_other_list #TODO: al desestructurar debe tener el mismo largo que la lista inicial 
print(lastname, age)

name, height, age, lastname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # NADA RECOMENDABLE
print(age)

print(my_list + my_other_list) # !TODO concatenar dos listas

my_list = "hola mundo"
print(my_list)
print(type(my_list))

#___________________________________________________-
#añadir un elemento al final 
my_other_list.append("JR&comp.")
print(my_other_list)

#añadir un elemento con un indice
my_other_list.insert(2, "av. cañoto")
print(my_other_list)

#añadir un elemento con un indice
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

lista.insert(0, 0)
print(lista)

lista.remove(2)
print(lista)

lista[0] = 1200
print(lista)

lista.reverse()
print(lista)

my_new_list = lista.copy()
print(my_new_list)

my_new_list[-1] = 150
my_new_list[-2] = 450
my_new_list[-3] = 650

my_new_list.sort()
print(my_new_list)

del lista[5]
print(lista)

lista.pop()
print(lista)

lista.clear()
print(lista)

