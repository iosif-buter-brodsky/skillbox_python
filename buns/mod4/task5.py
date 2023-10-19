"""
На вход подается строка – имя файла. Напишите программу, которая подсчитывает статистику по буквам в файле и выводит результат в файл.
Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию). Регистр символов имеет значение.
"""
#2 массива, зип, сортировка по второму и вывод

#считывание данных из файла input.txt
with open('input.txt', 'r') as file:
    data = file.read()

arr_latin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr_count = [0] * 52
data_sort = sorted(data)

for i in range(52):
    arr_count[i] = data_sort.count(arr_latin[i])
data_zip = list(zip(arr_count,arr_latin,))

#вывод в файл output.txt
data_output = str(sorted(data_zip)[::-1])
with open('output.txt', 'w') as file:
    file.write(data_output)