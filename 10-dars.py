# For 
# for i in range(1, 100):
#     print(i)
#     print("Reklama bor")
#     print("Salom")

# for kalit in range(12, 50, 3):
#     print(kalit)

# for son in [1, -9, 88, 7.7, 6j]:
#     print(son)

# for ism in ("Doniyor", "Hamidullo", "Muzaffar", "Ikrom"):
#     print(ism)

# for name in {"Doniyor", "Hamidullo", "Muzaffar", "Ikrom", "Doniyor", "Muzaffar"}:
#     print(name)

# lugat1 = {"name": "Ikrom", "age": 44, "place": "Yunusobod"}
# for key, value in lugat1.items():
#     print(key, value)

# mehmonlar = ["Hamidullo", "Islom", "Ikrom", "Abdusattor", "Ilon Mask", "Eldor"]
# for m in mehmonlar:
#     print("Assalomu alaykum,", m,"sizni to'yga taklif qilamiz")

#     print(f"Assalomu alaykum, {m} sizni to'yga taklif qilamiz")

# kitoblar = []
# for i in range(1, 11):
#     kitob = input(f"{i}-kitobni nomlarini kirit: ")
#     kitoblar.append(kitob)
    
# print("Siz o'qigan kitoblar: ", kitoblar)

# Uyga vazifa
# 1
# qarindoshlar = ["Doniyor", "Yodgor", "Hamidullo"]
# for i in qarindoshlar:
#     print("Hurmatli", i, "sizni ertaga tug'ilgan kunimga taklif etaman")

# 2
# count = len(qarindoshlar)
# print("Ushbu sikl", count, "marta aylandi")

# 3
# for son in range(-10, 11):
#     print(son)


# 4
# kublar = []
# for son in range(5, 56):
#     kublar.append(son ** 3)

# print(kublar)

# 5
dostlar_soni = int(input("Nechta do'stiz bor: "))
my_friends = []
for dost in range(1, dostlar_soni+1):
    ism = input(f"{dost}-do'sting kim:")
    if ism.lower() == "doniyor":
        break
    my_friends.append(ism)
    

