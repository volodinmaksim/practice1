def get_multiplied_digits(number):
    string_num = str(number)
    first = int(string_num[0])
    if len(string_num) == 1:
        return first
    if len(string_num) > 1:
        return first * get_multiplied_digits(int(string_num[1:]))

result = get_multiplied_digits(403)
print(result)