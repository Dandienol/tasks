# 1 Импорт библиотеки
import re, math

# 2 Вводим строку
str = input("\nВведите строку: ")

# 3 Разделение строк на текстовую и числовую
numbers = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
numbers = [int(i) for i in numbers]
print("\nТекстовая строка:\n", str)
print("\nСтрока чисел:\n", numbers)

# 4 Запись первых и последних букв слов - большими
def caps(str):
    str, result = str.title(), " "
    for words in str.split():	
        result += words[:-1] + words[-1].upper() + " "
    return result[:-1]
print("\nНовая текстовая строка:", caps(str),sep='')

# 5 Поиск наибольшего числа
max_n = max(numbers)
print("\nМаксимальное число в массиве:", max_n)

# 6 Подносим числа к степени , согласно их индекса
vals = []
for i in range(len(numbers)):
    if i != numbers.index(max_n):
        temp = math.pow(numbers[i], 2)
        vals.insert(i, temp)
print("Массив чисел в степени их индекса: \n", vals)
