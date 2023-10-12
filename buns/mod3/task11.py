arr = []
i = 0
#ввод двумерного массива 
while True:
    input_z = input().split(" ")
    arr.append(input_z)
    i += 1
    if i == len(input_z):
        break

len_arr = len(arr)
flag = False #флаг для определения была ли победа
win = '' #кто победил

#переворачиваем матрицу 
trans_arr= [[0 for i in range(len_arr)] for j in range(len_arr)]
for i in range(len_arr):
    for j in range(len_arr):
        trans_arr[j][i] = arr[i][j]
        

#проверка горизонтали
for x in range(len_arr):
    if arr[x].count(arr[x][0]) == len_arr:
        #print("norm")
        flag = True
        win += arr[x][0]
        break

#проверка вертикали, которая теперь горизонталь 
for x in range(len_arr):
    if trans_arr[x].count(trans_arr[x][0]) == len_arr:
        #print("norm")
        flag = True
        win += trans_arr[x][0]
        break

#проверка первой диагонали
diagonals_1 = ''
for x in range(len_arr):
    for y in range(len_arr):
        if x == y:
            diagonals_1 += arr[x][y]
if diagonals_1.count(diagonals_1[0]) == len_arr:
    #print("norm")
    flag = True
    win += diagonals_1[0]

#прорверка второй диагонали
diagonals_2 = ''
for x in range(len_arr):
    for y in range(len_arr):
        if (x + y) == (len_arr - 1):
            diagonals_2 += arr[x][y]
if diagonals_2.count(diagonals_2[0]) == len_arr:
    #print("norm")
    flag = True
    win += diagonals_2[0]

#вывод
if win != "":
    print(win[0])
else:
    print("_")