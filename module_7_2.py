def custom_write(file_name, strings):
    f_write = open(file_name, "w" , encoding='utf-8')
    iterator = 1
    strings_positions = {}
    for string in strings:
        tup = iterator, f_write.tell()
        strings_positions[tup] = string
        f_write.write(string + "\n")
        iterator += 1

    f_write.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
