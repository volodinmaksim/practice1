def calculate_structure_sum(*args):
    summ = 0

    for argument in args:

        if isinstance(argument, (list, set, tuple)):
            summ += calculate_structure_sum(*argument)

        elif isinstance(argument, dict):
            summ += calculate_structure_sum(*argument.keys())
            summ += calculate_structure_sum(*argument.values())

        elif isinstance(argument, int) or isinstance(argument, float):
            summ += argument

        elif isinstance(argument, str):
            summ += len(argument)

    return summ


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

