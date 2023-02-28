### my modules ###
import math
from math import pi as PI_VALUE
from module import sum, print_text
import module
print("___________Opción A de importar un modulo_______________")

module.sum(10, 15, 20)
module.sum(100, 5, 25)
module.print_text("hola", "python", "basico")

print("___________Opción B de importar un modulo_______________")
sum(100, 50, 28)
print_text("hola humano")

print("___________Importar modulo del sistema de python_______________")
print(math.exp(2))
print(math.PI_VALUE)
print(math.pow(2, 8))
