def power(a, b):
    if b == 0:
        return a
    else:
        return power(b, a % b)


a = int(input())
b = int(input())

print(power(a, b))
