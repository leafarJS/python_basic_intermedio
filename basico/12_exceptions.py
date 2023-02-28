# exceptions  Handling ### manejo de errores
num1, num2 = 5, 1
print(num1 + num2)
num2 = "1"

# try except
print("__________________try except________________________")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except:
    # se ejecuta si no se produce una excepción
    print("Se ha producido un error")

# try except else
print("_________________ try except else_________________________")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else:
    # se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")

# try except else finally
print("_______________try except else finally___________________________")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except:
    print("Se ha producido un error")
else:
    # se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally:  # opcional
    # se ejecuta siempre pase lo que pase
    print("La ejecución continúa")

print("_______________try except captura de excepciones_____________________")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except ValueError:
    print("Se ha producido un error ValueError")
except TypeError:  # se ejecuta solo si se ejecuta TypeError
    print("Se ha producido un error TypeError")

print("______try except captura de la información de la expeción______")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except ValueError as error:
    print(error)
print("______try except captura de la información del error y la excepción______")
try:
    print(num1 + num2)
    print("No se ha producido ningun error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
