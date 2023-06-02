# WHILE

# a = 2
# while a <= 10:
#     print(a)
#     # a = a + 1
#     # a += 1
#     # a -= 1
#     # a *= 2
#     # a /= 3
#     # a **= 2

# a = 2
# while True:
#     a += 1
#     print(a)
#     if a == 10:
#         break

# kitoblar = []
# while True:
#     kitob = input("Kitob nomini kiriting: ")
#     if kitob.lower() == "stop":
#         break
#     kitoblar.append(kitob)
# print(kitoblar)

# kitob = input("Kitob nomini kiriting: ")
# while kitob.lower() != "stop":
#     kitob = input("Kitob nomini kiriting: ")

# while True:
#     yosh = input("Yoshingiz: ")
#     if yosh.lower() == "exit" or yosh.lower() == "quit":
#         break
#     yosh_int = int(yosh)
#     if yosh_int < 7:
#         narx = 2000
#     elif yosh_int > 7 and yosh_int < 18:
#         narx = 3000
#     elif yosh_int >= 18 and yosh_int < 65:
#         narx = 10_000
#     else:
#         narx = "bepul"
#     print(narx)

# from dars12 import summa

# summa(7, 9)