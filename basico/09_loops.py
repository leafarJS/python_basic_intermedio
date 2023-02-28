## bucles o loops ##

my_condition:int = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1

# TODO un else se puede concaternar con el ciclo while si queremos mandar un mensaje cuando se cumple este ciclo
if my_condition == 10:
    print("Mi condición es igual a 10")    
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")



while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print(f"Mi condición es {my_condition}")
        break

    print(f"mi condición es ahora {my_condition}")


    # For

my_list = [35,24,62,52,60,60,17]
for i in my_list:
  print(f"iterando con el bucle for {i}")

my_tuple = (46,1.78,"jorge", "callejo", "jorge")
for i in my_tuple:
  print(f"iterando con el bucle for {i}")

my_other_set_2 = {"python", "javascript", "R"}
for i in my_other_set_2:
  print(f"iterando con el bucle for {i}")

my_dict = {
    "nombre": "rafael",
    "apellido": "flores",
    "edad": 46,
    "lenguajes": {"python", "javascript", "sql"},
    1:1.78
}
for i in my_dict:
  print(f"iterando con el bucle for {i}")