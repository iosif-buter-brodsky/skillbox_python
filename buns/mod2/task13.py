#сумма всех цифр на нечетных позициях и утроенная сумма цифр на четных делилась на 10.
nomer = input()
chet = 0
ne_chet = 0
for i in range(len(nomer)):
    if i % 2 != 0:
        ne_chet += int(nomer[i])
    if i % 2 == 0:
        chet += int(nomer[i])
        
if (chet + (ne_chet * 3)) % 10 == 0:
    print("yes")
else:
    print("no")