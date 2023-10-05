stroka = input().split(" ")
a = int(stroka[0])
b = int(stroka[1])
c = int(stroka[2])
sum_abc = a + b + c
sr_abc = sum_abc - min(a,b,c) - max(a,b,c)
print(sr_abc)
