# FOR I IN
# word = 'ТранЗакция'
# for i in word:
#     # if i == 'з' or i == 'З':
#     if i.lower() == 'з':
#         print("Буква 'з' найдена")
#     else:
#         print('не найдено')


# nums = [3, 5, 6, 7, 2, 6, 7, 8, 4, 6, 4, 6, 8, 2, 5]
# chet = []
# nechet = []

# for num in nums:
#     if num % 2 == 0:
#         chet.append(num)
#     else:
#         nechet.append(num)

# print(nums)
# print(chet)
# print(nechet)


# WHILE TRUE
# counter = 0
# while True:
#     print(counter)
#     counter += 5


# while True:
#     num = int(input())

#     if num == 0:
#         break

#     if num % 2 == 0:
#         print("Четное!")
#     else:
#         print("Нечетное!")

# while True:
#     s = int(input("Введите сумму в сомах: "))

#     if s == 0:
#         break

#     print(round(s / 84, 3))


# DEF
# def say_hello():
#     print("GeekCamp TOP!")

# say_hello()

# def s(x=2, y=2):
#     return x*y

# print(s(3,4))


# names = [
#     'Нурзада', "Нурбек", 'Акбермет', "Бектур", 'Эрмек', 'Жахонгир',
#     'Бекбол' , 'Нурсултан', "Айбек", 'Элина', 'Миртемир', "Бекзат",
#     'Эсенбек', "Тимабек"
#     ]

# names2 = [
#     'Кумарбек', 'Даниел', 'Байел', 'Жениш',
#     'Инсан', 'Аскар', 'Жаркын', 'Зайнап', 'Эсенбек',
#     "Нурдинбек", "Тимабек", "Адахан", "Бекболсун",
#     'оолобекаудлацдлцл'
#     ]

# def filter_bek(x=names):
#     beki = []
#     nebeki = []
#     for name in x:
#         if 'бек' in name.lower():
#             beki.append(name)
#         else:
#             nebeki.append(name)
#     print(beki)
#     print(nebeki)

# filter_bek()

# DICT

person = {
    'name': 'Ruslan',
    'age': 18,
    'city': 'Bishkek',
}

person['married'] = False
del person['city']
person.update(dict(height=180))
print(person)
