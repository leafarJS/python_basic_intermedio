### lambdas ###
# son como funciones, funciones anonimas o callbacks, funciones sin nombre
def sum_two_values(num1, num2): return num1 + num2


print(sum_two_values(10, 15))


def multiply_values(
    first_Value, second_value): return first_Value * second_value - 100


print(multiply_values(125, 25))


def sum_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_values(100)(2, 4))
