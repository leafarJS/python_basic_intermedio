### Expresiones Regulares ###
import re

# TODO: Match
my_string = "Está es la lección número: 7 del curso,\nlección: Expresiones Regulares"
my_string_new = "Está es la lección número: 6 del curso,\nlección: Manejo de Ficheros"
print("_________________match_____________________")

print(re.match("Está es la lección", my_string))
print(re.match("Está es la lección", my_string, re.I))
print(re.match("Esta es la lección", my_string_new))
print(re.match("Expresiones Regulares", my_string))
# empieza a buscar desde el principio por lo que no lo encuentra y da como resultado None

match = re.match("Está es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match_new = re.match("Manejo de Ficheros", my_string_new, re.I)
if not (match_new == None):  # is not | != | not
    print(match_new)
    start, end = match_new.span()
    print(my_string_new[start:end])

# TODO: search
print("________________search______________________")
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# TODO: findall
print("________________find all______________________")
findall = re.findall("lección", my_string, re.I)
print(findall)


# TODO: split
print("________________split______________________")
print(re.split(",", my_string))
print(re.split("\n", my_string))
print(re.split(":", my_string))

# TODO: sub
print("________________sub______________________")
substitucion = re.sub("Expresiones", "EXPRESIONES", my_string, re.I)
print(substitucion)
substitucion = re.sub("lección", "LECCIÓN", my_string_new, re.I)
print(substitucion)
substitucion = re.sub("[L|l]ección", "LECCIÓN", my_string_new, re.I)
print(substitucion)

# TODO: Patterns
print("________________patterns______________________")

my_string = "Está es la lección número: 1 del curso,\nLección: Expresiones Regulares"
my_string_new = "Está es la lección número: 0 del curso,\nLección: Manejo de Ficheros"


pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[Ll]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[aeiou]"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# email validation regular expresion


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    return re.match(pattern, email)


print(is_valid_email("efpyi@example.com"))
print(is_valid_email("efpyi_1977+-@example.com.bo"))

# https://regex101.com/
