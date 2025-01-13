"""Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
 при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
"""

def all_variants(text):
    for k, i in enumerate(text, 0):
        for k2, j in enumerate(text, 1):
            if k >= k2 or k >= len(text):
                continue
            else:
                yield text[k:k2]


a = all_variants("abc")

for i in a:
    print(i)

b = all_variants("abcd")
for i in b:
    print(i)

