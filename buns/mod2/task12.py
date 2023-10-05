#Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы. Уберите их из ввода.
nomer = input()#+7 (812) 134-12-324
nomer_clean = ''
for i in range(len(nomer)):
    if nomer[i] != " " and nomer[i] != "-" and nomer[i] != ")" and nomer[i] != "(":
        nomer_clean = nomer_clean + nomer[i]
print(nomer_clean)