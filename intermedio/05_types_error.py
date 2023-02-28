## types error ##
# ModuleNotFoundError
# ImportError
import math as mt
from math import pi

# print(math.PI) ImportError: cannot import name 'PI' from 'math' (unknown location)

# import maths  # ModuleNotFoundError: No module named 'maths'
print(mt.pow(2, 8))
print(mt.pi)


### TODO: tipos de errores ###
# SyntaxError
# print "¡Hola mundo!" | SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print("¡Hola mundo!")

# NameError
# print(name) NameError: name 'name' is not defined
name = "Jorge Rafael"
print(name)

# IndexError
my_list = ["python", "swift", "javascript", "sql", "R"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
# print(my_list[5]) IndexError: list index out of range
# print(my_list[6]) IndexError: list index out of range
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
# print(my_list[-6]) IndexError: list index out of range


# AttributeError
# print(mt.PI) AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(mt.pi)


# KeyError
my_dict = {
    "nombre": "jorge",
    "apellido": "callejo",
    "edad": 45,
    1: "python"
}
print(my_dict)
print(my_dict["apellido"])
# print(my_dict["nombres"]) KeyError: 'nombres'


# TypeError
# print(my_list["indice 0"]) TypeError: list indices must be integers or slices, not str
print(my_list[0])


# ValueError
my_int = int("10")
print(type(my_int))
# print(type(my_int)+10) TypeError: unsupported operand type(s) for +: 'type' and 'int'

# my_int = int("10 años")
# print(type(my_int)) ValueError: invalid literal for int() with base 10: '10 a�os'


# ZeroDivisionError

print(10/2)
# print(10/0) ZeroDivisionError: division by zero
