# challengers ###
### retos de codigo ###
"""
escribe un programa que muestro consola con un print, los numeros del 1 al 100 ) ambos incluidos y con un saldo de linea
entre cada impresión , sustituyendo lo :
- Multiplos de 3 con la impresión "fizz"
- Multiplos de 5 con la impresión "buzz"
- Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz"
"""
# !TODO ALTERNATIVA 1 solución parcial
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# !TODO ALTERNATIVA 1 solución correcta


def fizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzBuzz()


"""
Escribe una función que reciba dos palabras (string) y retorne verdadero o falso (bool)
segun sean o no anagramas
- un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial
- No hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagramas
"""


def anagrama(a, b):
    if a.lower() == b.lower():
        return False
    return sorted(a.lower()) == sorted(b.lower())


print(anagrama("hola", "laho"))
print(anagrama("hola", "lahooooolkjdf"))
print(anagrama("holadfafaefa", "laho000lkjdf"))


"""
Escribe un programa que imprima los 50 primeros numeros de la sucesión de fibonacci empezando en 0.
- la serie fibonacci se compone por una sucesión de numeros en la que el siguiente siempre es la suma de los dos anteriores
0,1,1,2,3,5,13,...
"""


def fibonacci():
    prev = 0
    next = 1
    for i in range(1, 51):
        print(f"posición: {i}")
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()

"""
¿Es un numero primo?
escribe un programa que se encargue de comprobar si un número es o no primo.
hecho esto imprelos numeros primos entre 1 y 100
"""


def num_primos():
    for i in range(1, 101):
        if i >= 2:
            es_divisible = False
            for idx in range(2, i):
                if i % idx == 0:
                    es_divisible = True
                    break
            if not es_divisible:
                print(i)


num_primos()


"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje
que lo hagan de forma automatica.
- si le pasamos "hola mundo" nos retornaria "odnum aloh"
"""


def texto_reverso(text):
    text_len = len(text) - 1
    text_reverso = ""
    for i in range(0, text_len + 1):
        text_reverso += text[text_len - i]
    return text_reverso


print(texto_reverso("paralelepipedo"))
