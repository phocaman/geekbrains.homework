# 4. (не обязательно, но желательно) Из урока по комбинаторике повторите расчеты,
# сгенерировав возможные варианты перестановок для других значений n и k.


import itertools


for p in itertools.product('87', repeat=2):
    print(''.join(p))

count = 0
for p in itertools.product('8765', repeat=4):
    # print(''.join(p))
    count += 1
print(count)

#  перестановки

count = 0
for p in itertools.permutations('5432', 4):
    # print(''.join(str(x) for x in p))
    count += 1
print(count)

count = 0
for p in itertools.permutations('98765432', 8):
    # print(''.join(str(x) for x in p))
    count += 1
print(count)

count = 0
for p in itertools.permutations('abcdef', 4):
    # print(''.join(str(x) for x in p))
    count += 1
print(count)

# сочетания

count = 0
for p in itertools.combinations('987654', 2):
    # print(''.join(p))
    count += 1
print(count)

count = 0
for p in itertools.combinations('abcdefgh', 4):
    # print(''.join(p))
    count += 1
print(count)
