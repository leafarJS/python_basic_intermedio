### string ###

my_string:str = "Mi cadena"
my_other_string:str = "Mi otra cadena"
my_string_line:str = "Mi cadena\ncon salto de linea"
my_string_tab:str = "\tMi cadena con tabulación"

print(len(my_string))
print(len(my_other_string))
print(my_string_line)
print(my_string_tab)

## Formateo 

name, lastname, age = "jorge", "callejo", 46

#opción A
print(my_string + " " + my_other_string)
#opción B
print("Mi nombre es %s %s y mi edad es %d años" %(name, lastname, age))
#opción C
print("Mi nombre es {} {} y mi edad es {} años".format(name, lastname, age))
#opción D
print(f"Mi nombre es {name} {lastname} y mi edad es {age} años")

# Desempaquetado de caracteres
language:str = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)

# División
language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-3]
print(language_slice)

#reverse
reversed_lenguage = language[::-1]
print(reversed_lenguage)

language_slice = language[0:6:2]
print(language_slice)

# Metodos o funciones del sistema 
print(len(language))
print(language.capitalize())
print(language.casefold())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.lower())
print(language.startswith("py"))
