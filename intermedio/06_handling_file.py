### Manejo de ficheros ###
import xlrd
import csv
import os
import json
import xml
# File Handling

# .TXT FILE
# open("my_file.txt") FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
# open("./my_file.txt") FileNotFoundError: [Errno 2] No such file or directory: './my_file.txt'
# txt_file = open("intermedio/my_file.txt", "w")
# print(txt_file.read()) io.UnsupportedOperation: not readable
# txt_file = open("intermedio/my_file.txt", "r")
# print(txt_file.read())
# txt_file = open("../python_cero/my_file.txt", "r+")  # leer y escribir
# print(txt_file.read())
# print(txt_file.read(20))

# print(txt_file.readline())
# print(txt_file.readline())

# print(txt_file.readlines())

# txt_file.write("\nEscrito desde visual studio code")

# for i in txt_file.readlines():
#     print(i)

# txt_file_1 = open("../python_cero/my_file_1.txt", "w+")
# txt_file_1.write(
#     "Primer mensaje\nSegundo mensaje\nTercer mensaje\nCuarto mensaje\n")
# txt_file_1.write("\nEl mejor lenguaje es javaScript")
# print(txt_file_1.readline())
# txt_file_1.close()


# with open("../python_cero/my_file.txt", "a") as my_other_file:
#     my_other_file.write("\nY Swift")

# os.remove("../python_cero/my_file.txt")

# .json file
json_file = open("../python_cero/my_file.json", "w+")
json_test = [
    {"name": "jorge",
     "lastname": "callejo",
     "age": 45,
     "language": "python",
     "city": "La Paz"},
    {"name": "rafael",
     "lastname": "flores",
     "age": 46,
     "language": "javaScript",
     "city": "Santa Cruz"},
    {"name": "armando",
     "lastname": "catres",
     "age": 44,
     "language": "javaScript",
     "city": ["Santa Cruz", "Oruro", "Potosi"]
     }
]
json.dump(json_test, json_file, indent=4)

json_file.close()

with open("../python_cero/my_file.json") as my_json_file:
    for i in my_json_file.readlines():
        print(i)

# parsear json a list
json_list = json.load(open("../python_cero/my_file.json"))
print(json_list)
print(type(json_list))
print(json_list[0])


# .csv file
csv_file = open("../python_cero/MSFT.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(
    ["2023-02-27", "100.000000", "100.000000", "100.000000",
        "100.000000", "100.000000", "100000000"])
csv_writer.writerow(
    ["2023-02-27", "101.000000", "101.000000", "101.000000",
        "101.000000", "101.000000", "101000000"])
csv_file.close()

with open("../python_cero/MSFT.csv") as my_other_file_csv:
    for i in my_other_file_csv.readlines():
        print(i)
# .xlsx file

# .xml file
