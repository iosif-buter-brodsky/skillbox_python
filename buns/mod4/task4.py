#Если из слова можно составить палиндром, то составить его и вывести на экран.
#отсортировать, убрать лишнее и добавить
slovo = list(input())
slovo_new = [0] * (len(slovo)//2)
#slovo_new_nechet = [0] * (1 + len(slovo)//2)
slovo_new_nechet = [0] * len(slovo)
slovo_sotr = sorted(slovo)
#создвем массив убрав каждое втрое повторение
slovo_bez_povtorov = []
for i in range(0, len(slovo_sotr), 2):
    slovo_bez_povtorov.append(slovo_sotr[i])


#если четное, о просто добаляем в слева и дублируем в конце
if len(slovo) % 2 == 0:
    for i in range(len(slovo_bez_povtorov)):
        slovo_new[i] = slovo_bez_povtorov[i]
        #slovo_new[-i] = slovo_bez_povtorov[i]
        
#если не четное
bukva_cr = ''
if len(slovo) % 2 != 0:
#else:
    """
    for i in range(len(slovo_bez_povtorov)):
        if slovo_bez_povtorov.count(slovo_bez_povtorov[i]) % 2 == 0:
            slovo_new_nechet[i] = slovo_bez_povtorov[i]
        else:
            bukva_cr += slovo_bez_povtorov[i]
    """
    for i in range(len(slovo_sotr)):
        if slovo_sotr.count(slovo_sotr[i]) % 2 == 0:
            slovo_new_nechet[i] = slovo_sotr[i]
        else:
            bukva_cr += slovo_sotr[i]
#чет делаем с slovo_sotr(убираем нули и сокращаем количество символов в2 раза)
filtered_array = list(filter(lambda x: x != 0, slovo_new_nechet))
#соращаем количествло
vvv = []
for i in range(0, len(filtered_array), 2):
    vvv.append(filtered_array[i])

z = [0] * len(bukva_cr)
for i in range(len(bukva_cr)):
    z[i] = bukva_cr[i]

zov = vvv + (z) + vvv[::-1]
#вывод 
if (slovo_new + slovo_new[::-1])[0] == 0:
    print("".join(zov))
else:
    print("".join(slovo_new + slovo_new[::-1]))

    