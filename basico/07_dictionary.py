## Diccionarios ##

my_dict:dict = dict()
my_other_dict:dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "nombre": "jorge",
    "apellido": "callejo",
    "edad": 46,
    "lenguaje": "python",
    100: "clave"
} # relación clave valor | key:value

my_dict = {
    "nombre": "rafael",
    "apellido": "flores",
    "edad": 46,
    "lenguajes": {"python", "javascript", "sql"},
    1:1.78
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["lenguajes"])

my_other_dict["nombre"] = "Fernando Marcelo"
my_other_dict["calle"] = "Av. insurgentes de America"

print(my_other_dict)

del my_other_dict[100] # eliminar un solo elemento de un diccionario

print(my_other_dict)

print("nombre" in my_other_dict) # true porque busca por key
print("jorge" in my_other_dict) # false porque no busca por value

print("_____________________________________")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys("nombre", "apellido")) # sintaxis incorrecta
print(my_dict.fromkeys(("nombre", "apellido")))  # crear un diccionario nuevo sin valores 

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)