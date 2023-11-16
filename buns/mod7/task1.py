"""
1.Должен быть передан ровно один аргумента. Если передано меньшее количество, декоратор должен вернуть строку: «Not enough arguments»
2.Если передано больше аргументов, то возвращаем строку: «Too many arguments»
3.Аргумент должен быть целым числом. Если нет, то возвращаем строку: «Wrong types»
4.Аргумент не должен быть отрицательным, иначе – «Negative argument»

"""
def example_decorator(func):
    def wrapper(*args,):
        arg = args[0]
        if len(args) != 1:
            if len(args) > 1:
                return "Too many arguments"
            else:
                return "Not enough arguments"
        
        if not(isinstance(arg, int)):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"
        
        return func(*args)
    return wrapper

@example_decorator
def example_function(x):
    return x*2

result1 = example_function(5)
print("Результат:", result1)

result2 = example_function(10, 20)
print("Результат:", result2)  

result3 = example_function(-3)
print("Результат:", result3)

result4 = example_function("z")
print("Результат:", result4)  