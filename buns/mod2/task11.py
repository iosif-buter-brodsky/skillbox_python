stroka = input()
flag = False
stroka_new = ''

for i in range(len(stroka)):
    if stroka[i] != " ":
        stroka_new = stroka_new + stroka[i]

for j in range(len(stroka_new)):
    if stroka_new.find(stroka_new[j],j + 1,len(stroka_new)) != -1:
        flag = True
print(flag)
    