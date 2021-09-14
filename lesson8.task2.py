# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from heapq import heapify, heappop, heappush
from collections import defaultdict

def encode_string(freq):
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapify(heap)
    while len(heap) > 1:
        low = heappop(heap)
        high = heappop(heap)
        for val in low[1:]:
            val[1] = '0' + val[1]
        for val in high[1:]:
            val[1] = '1' + val[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

user_str = input('Введите строку: ')

freq = defaultdict(int)

for char in user_str:
    freq[char] += 1
huffman_code = encode_string(freq)

print('Символ'.ljust(10) + 'Частота'.ljust(10) + 'Код Хаффмана')

for i in huffman_code:
    print(i[0].ljust(10) + str(freq[i[0]]).ljust(10) + i[1])