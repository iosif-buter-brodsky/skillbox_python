'''
try:
    a = int(input())
    if a < 0:
         print("ну и что ты ввел? Неверный ввод")
    else:
        print(bin(a)[2:]+", "+oct(a)[2:]+", "+hex(a)[2:])
except:
    print("ну и что ты ввел? Неверный ввод")
'''
def to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def to_octal(n):
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal

def to_hexadecimal(n):
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        n //= 16
    return hexadecimal

try:
    a = int(input())
    if a < 0:
         print("ну и что ты ввел? Неверный ввод")
    else:
        binary = to_binary(a)
        octal = to_octal(a)
        hexadecimal = to_hexadecimal(a)
        print(binary + ", " + octal + ", " + hexadecimal)
except ValueError:
    print("ну и что ты ввел? Неверный ввод")