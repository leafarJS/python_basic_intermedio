### funciones ###
def my_fuction():
    print("this is my first function")

my_fuction()

def sum_two_values(a, b):
    print(a + b)

sum_two_values(10,100)
sum_two_values(15000,187946)
sum_two_values(int("5"), int("7"))

def sum_three_values(a:int, b:int, c:int):
    print(a + b + c)

sum_three_values("12", "34", "56") # no convierte string en int,cuando se coloca en los parametros el tipo de dato

def sum_four_values(a:int, b, c, d:int):
    print(a / b + c / d)

sum_four_values(5.1, 5.3, 5.9, 5.7)


def sum_with_return(x, y):
    return x + y

print(sum_with_return(10,15))

result = sum_with_return(100,150)
print(result)

def my_sum(x , y):
    elevado = (f"la operación de: {10^x} y {5^y} da como resultado: {10^x + 5^y}")
    return elevado

result = my_sum(2,3)
print(result)

def print_name(name, lastname):
    print(f"{name} {lastname}")

print_name(lastname="callejo", name="jorge")


def print_name_default(name, lastname, alias="loco"):
    return(f"{name} {lastname}, {alias}")

resultado = print_name_default("jorge", "callejo")
print(f"el resultado es: {resultado}")


def print_texts(*text): # con el asterisco podemos pasar varios argumentos
    for t in text:
      print(t.upper())

print_texts("Python", "javascript", "R", "sql")