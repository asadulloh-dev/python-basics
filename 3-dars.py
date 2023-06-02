# DATA types
# 3/05/2023

# 1. String
# name = "Ikrom"
# surname = 'Tohirov'
# patronimics = """Usmonovich
# Johongir
# Olimov"""
# # place = '''Uzbekistan'''

# print(surname)
# print(patronimics)

# Number: int, float, complex
# Int: 1, 888, -9
# float: 4.0, 4.333, 9.00001
# complex: 5j, 88J

# Boolean: True, False

# a, b, c = 2, 7, 9
# a=b=c=0
# a = 8
# b = 77
# print(a, b)

# a, b = b, a
# print(a, b)

# # 1
# n = float(input("Uzunlikni kirit: "))
# butun = int(n / 100)
# print(butun)

# # 2
# n = float(input("Og'irlikni kirit: "))
# butun = int(n / 1000)
# print(butun)

# a = int(input("Son kirit: "))
# a10 = int(a / 10)
# a1 = a % 10
# print(a10)
# print(a1)

# memory = int(input("Fayl hajmini baytlarda kiriting: "))
# memory_kb = int(memory / 1024)
# print(memory_kb)

# a = int(input("Son: "))
# a10 = int(a / 10)
# a1 = a % 10
# x = a10 + a1
# print(a10)
# print(a1)
# print(a1, a10)

# a = int(input("Son: "))
# a100 = int(a / 100)
# a1 = a % 10
# a10 = int(a / 10) % 10
# # a10 = int((a % 100) / 10)
# print(a100, a10, a1)

a = int(input("Son: "))
x = int(a / 100) % 10
print(x)

y = int((a % 1000) / 100)
print(y)