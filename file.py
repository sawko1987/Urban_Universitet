def custom_write(file_name, strings):
    file_name = 'text.txt'
    file = open(file_name, 'w', encoding='utf-8')
    positions = {}
    str_ = 0
    for i in strings:
        str_ += 1
        tell_ = file.tell()
        file.write(f'{i}\n')
        positions[(str_, tell_)] = i
    file.close()
    return positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)