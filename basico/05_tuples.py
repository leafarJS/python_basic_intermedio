## tuples ##
my_tuple:tuple = tuple()
my_other_tuple = (30,15,26)
print(type(my_tuple))
print(type(my_other_tuple))

my_tuple = (46,1.78,"jorge", "callejo", "jorge")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-6]) IndexError


print("------------------------------")
print(my_tuple.count("jorge"))
print(my_tuple.index("callejo"))

# TODO: las tuplas son inmutables ya no se puede adicionar o eliminar SON VALORES CONSTANTES
# my_tuple[0]= 147
# print(my_tuple)

new_tuple = my_tuple + my_other_tuple

print(new_tuple[3:6])