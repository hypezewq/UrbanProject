first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = map(lambda x: len(x[0]) - len(x[1]), filter(lambda y: len(y[0]) != len(y[1]), zip(first, second)))
second_result = map(lambda x: len(first[x]) == len(second[x]), range(len(first)))

print(list(first_result))
print(list(second_result))
