### clases ###
class MyEmptyPerson:
    pass # Cree un marcador de posición para código futuro:
print("__________________________________________")
print(MyEmptyPerson)
print(MyEmptyPerson())



class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastaname = lastname
        pass
print("__________________________________________")
my_person = Person("jorge", "callejo")
print(my_person)
print(my_person.name)


class NewPerson:
    def __init__(self, name, lastname, alias = "Sin alias"):
        self.full_name = f"{name} {lastname} ({alias})"
        self.__name = name #para hacerlo privado
        self.__lastname = lastname
        pass
    
    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando!!")
print("__________________________________________")
my_person_1 = NewPerson("rafael", "flores")
print(my_person_1)
print(my_person_1.get_name())
print(my_person_1.full_name)
my_person_1.walk()

print("__________________________________________")
my_person_2 = NewPerson("jorge", "rafael", "rambo")
print(my_person_2.full_name)
my_person_2.walk()
my_person_2.full_name = "Patroclo el amante de Aquiles"
print(my_person_2.full_name)