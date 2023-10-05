#Дан список слов. Составить из последних букв каждого слова новое.
stroka = input()
new_str = ''
for i in range(len(stroka)):
    if stroka[i] == ' ':
        new_str = new_str + stroka[i-1]
    
print(new_str + stroka[-1])
