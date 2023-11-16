def get_armstrong_numbers():
    n = 10
    while True:
        num_str = str(n)
        power = len(num_str)
        armstrong_sum = sum(int(digit) ** power for digit in num_str)
        if armstrong_sum == n:
            yield n
        n += 1

armstrong_gen = get_armstrong_numbers()
for i in range(100):
    print(next(armstrong_gen), end=' ')
