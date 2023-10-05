stroka = input().split(",")
elem = stroka[0]
smehenie = int(stroka[1])
n_k = (ord(elem)+smehenie)#номер k
if n_k >= 97 and n_k <= 122:
    print(chr(n_k))
elif n_k > 122:
    print(chr(n_k-122+96))
elif n_k < 97:
    print(chr(123 - (97 - n_k)))

