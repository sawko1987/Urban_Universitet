first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

result_first = [len(x) for x in first_strings if len(x)>5]
print(result_first)

second_result = [(x,y) for x in first_strings for y in second_strings if len(x)==len(y)]
print(second_result)

third_result = {(str(f"{x}-{len(x)}")):len(x) for x in first_strings + second_strings if not (len(x)%2)}
print(third_result)