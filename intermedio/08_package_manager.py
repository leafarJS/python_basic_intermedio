### Manejo de paquetes python ###

# pip install https://pypi.org/
from my_package import aritmethics as at  # modulo creado por nosotros mismos
import requests
import pandas as pd
import numpy as np

print(pd.__version__)
print(np.version.version)

arreglo = np.array([35, 24, 62, 52, 30, 30, 17])

print(arreglo)
print(type(arreglo))

print(arreglo * 12)

# TODO: pip list | para ver lista de programas instalados
# TODO: pip uninstall | para desinstalr programs instalados
# TODO: pip show | para obtener información de un programa
# TODO: pip --version | para obtener información de la version instalada

res = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(res)
print(res.status_code)
print(res.json())

print(at.sum_two_values(15, 25))
