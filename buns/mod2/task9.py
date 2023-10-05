stroka = input()
glass = 0
space = 0
for i in range(len(stroka)):
    if stroka[i] == "а" or stroka[i] == "я" or stroka[i] == "у" or stroka[i] == "ю" or stroka[i] == "о" or stroka[i] == "е" or stroka[i] == "ё" or stroka[i] == "э" or stroka[i] == "и" or stroka[i] == "ы":
        glass += 1
    elif stroka[i] == " ":
        space += 1
print(glass , (len(stroka) - glass - space))
    
        