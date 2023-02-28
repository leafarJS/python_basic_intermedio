## Condicionales ##
my_condition = False

if my_condition:
    print("Cierto")
else:
    print("Falso") 

print("Se ejecuta fuera de la condición")

my_condition =  5 * 2

if my_condition >= 8:
    print("No Se ejecuta como condición como verdadera")
else:
    print(f"La condicion es mayor")


my_condition = 10 * 100

if my_condition < 100:
    print("Falso 1")
elif my_condition <=100:
    print("Cierto 1")
else:
    print("Falso 2")


my_condition = 19
if my_condition > 10 and my_condition <= 20:
    print("cierto se encuentra entre los parametros")

my_string = "holas"

if not my_string:
    print("Mi cadena de texto no esta vacia")
else:
    print("Cadena de texto vacia")