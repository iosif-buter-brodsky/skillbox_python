size = int(input())
arr = [[0 for j in range(size)] for i in range(size)]
arr_1 = [[0 for j in range(size)] for i in range(size)]

# Обычная матрица 
for x in range(size):
    for y in range(size):
        arr[x][y] += y + 1

# Вывод массива 
for i in range(size):
    for j in range(size - 1):
        print(arr[i][j], end=", ")
    print(arr[i][size - 1]) 


# Транспонируемая матрица
for x in range(size):
    for y in range(size):
        arr_1[x][y] += x + 1
print()

# Вывод массива 
for i in range(size):
    for j in range(size - 1):
        print(arr_1[i][j], end=", ")
    print(arr_1[i][size - 1]) 