import random
import string

#генерация данных в файл input.txt
def generate_random_letters(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def write_random_letters_to_file(filename, num_letters):
    with open(filename, 'w') as file:
        for _ in range(num_letters):
            random_letters = generate_random_letters(1)
            file.write(random_letters)


filename = 'input.txt'
num_letters = 1000

write_random_letters_to_file(filename, num_letters)
