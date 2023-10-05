a = input()
count_1 = 0
count_0 = 0
for i in range(len(a)):
    if a[i] == "1":
        count_1 += 1
    else:
        count_0 += 1

if count_0 == count_1:
    print("yes")
else:
    print("no")

    