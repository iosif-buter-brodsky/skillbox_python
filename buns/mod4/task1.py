stroka = input().split()
z = []
for i in range(len(stroka)):
    z.append(stroka.count(stroka[i]))

if len(set(stroka)) == 1:
    print("Все числа равны")
elif z.count(1) == len(stroka):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")