# variables 
MyVariable = "My String variable"
print(MyVariable)

# ! TODO: recomendación escribir las variables en minusculas y en snakecase

my_str_variable = "String"
print(my_str_variable)

my_int_variable = 500
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# concatenación de variables en un print 
print(my_str_variable, str(my_int_variable), my_bool_variable)

print(type(print(my_str_variable, str(my_int_variable), my_bool_variable)))

#funciones precargadas en sistema 
tupla = [0,1,2,3,4,5,6,7,8,9]
print(len(tupla))
print(len(my_str_variable))

print("Este es el valor de mi variable boolenana: ", my_bool_variable)

# variables en un sola linea
name, surname, alias, age = "jorge", "callejo", "Mers", 46

print("Mi alias es:", alias, "y tengo", age, "años")


# inputs
first_name = input('what is your name: ')
age = input('How old are you?')

print("Mi nombre es: ",first_name)
print("Mi edad es de: ", age, "años")


# volver una variable de python , con tipiado fuerte
name:str = "jorge"
year:int = 46

print(name, year)

print(type(year))

year = "jorge"
print(year)

print(type(year))