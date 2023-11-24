import re

def check_password(password):
    if len(password) < 8:
        return False

    if re.search('[,.!?]', password):
        return False

    if len(re.findall('[a-z]', password)) < 2:
        return False

    if not re.search('\d', password):
        return False

    if len(set(re.findall('[^\w\s]', password))) < 3:
        return False

    if not re.fullmatch('[a-zA-Z0-9^$%@#&*]*', password):
        return False

    return True

passwords_to_check = [
    'rtG&3FG#Tr^e',
    'a^A1@*@1Aa',
    'oF^a1D@y5%e6',
    'enroi#$*rkdeR#$*092uwedchf34tguv394h',
    'пароль',
    'password',
    'qwerty',
    'lOngPa$$W0Rd'
]

for password in passwords_to_check:
    if check_password(password):
        print(f'Пароль "{password}" корректный')
    else:
        print(f'Пароль "{password}" некорректный')
