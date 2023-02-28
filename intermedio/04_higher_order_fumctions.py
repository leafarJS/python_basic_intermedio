### funciones de orden superior ###
from functools import reduce


def sum_one(value):
    return value + 1


def sum_two_values_and_one(first_value, second_value):
    return sum_one(first_value + second_value)


print(sum_two_values_and_one(5, 2))


def sum_two(value):
    return value + 2


def sum_five(value):
    return value + 5


def sum_two_values_and_function(first_value, second_value, func):
    return func(first_value + second_value)


print(sum_two_values_and_function(5, 3, sum_two))
print(sum_two_values_and_function(5, 3, sum_five))

### closures ###


def sum_ten():
    def add(value):
        return value + 10
    return add


add_clouser = sum_ten()
print(add_clouser(15))


def sum_sixten(original_value):
    def add(value):
        return value + 10 + original_value + original_value
    return add


# dos fases
add_clouser_1 = sum_sixten(5)
print(add_clouser_1(25))
# una fase
print(sum_sixten(12)(8))

## funciones de orden superior que existen en el propio lenguaje ##
## built_in higher order function ##

# TODO: MAP
numbers = [2, 3, 5, 7, 11, 13, 21, 27]


def multiply_two(number):
    return number * 2


print(map(multiply_two, numbers))
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 8, numbers)))


# TODO: FILTER

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False


print(filter(filter_greater_that_ten, numbers))
print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 5, numbers)))

# TODO: REDUCE
# from functools import reduce


def sum_two_values_reduce(first_value, second_value):
    print(f"{first_value} : {second_value}")
    return first_value + second_value


print(reduce(sum_two_values_reduce, numbers))
