# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_evens_odds(n):
    evens_count = 0
    odds_count = 0
    while n > 0:
        remainder = n % 10
        if remainder % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1
        n = int(n / 10)
    return f'Чётных цифр: {evens_count}. Нечётных цифр: {odds_count}.'

print(count_evens_odds(123456789))
