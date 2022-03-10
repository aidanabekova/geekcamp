# # # ЛИСТЫ - LIST
# # list = [10, 2, 13, 4, 1, 6, 6, 6, 6, 9, 12, 45, 3]
# # names = ['Beka', 'Aidana', 'Aidana', 'Aisuluu', 'Saltanat', 'Muhtar', 'Adil']
# # # методы LIST
# # names.append('Alina')  # добавляет в конец списка новое значение
# # names.insert(4, 'Islam')
# # names.insert(-2, 'Alisa')  # добаляет новое значение по индексу
# # names.extend(list)  # расширяет один список другим списком
# # names.remove('Beka')  # удаляет по значение
# # list.sort()  #просто сортирует по возрастанию
# # print(list.count(2))  #выводит кол-во какого-то значения
# # # list.clear() #очищает полностью список
# # list.reverse() #сортирует от большего к меньшему
# # print(list)
# # print(list)
# # print(names)
# #
# # #КОРТЕЖИ - TUPLE
# # names = ('Beka', 'Aidana', 'Aidana', 'Aisuluu', 'Saltanat', 'Muhtar', 'Adil')
# # print(names)


# # ЦИКЛЫ: WHILE, FOR
# # FOR
# word = 'транЗакция'
# for letter in word:
#     if letter == 'з':
#         print("буква 'з' найдена")
#     elif letter == 'З':
#         print("буква 'З' найдена")
#     else:
#         print('not found')
#
# nums = [2, 4, 13, 24, 56, 5, 7, 8, 9, 34, 5, 6, 0]
# chetnye = []
# nechetnye = []
# for number in nums:
#     if number % 2 == 0:
#         chetnye.append(number)
#     elif number % 2 != 0:
#         nechetnye.append(number)
# print(nums)
# print(chetnye)
# print(nechetnye)
#
#
# # WHILE
# # count = 0
# # while True:
# #     print(count)
# #     count += 3
# #
# # while 1:
# #     num = int(input('введите любое число: '))
# #     if num == 0:
# #         print('GoodBye!')
# #         break
# #     elif num % 2 == 0:
# #         print('Четное!')
# #     elif num % 2 != 0:
# #         print('Нечетное!')
#
# # while 1:
# #     money = int(input('введите сумму в сомах: '))
# #     if money == 0:
# #         print('Пока')
# #         break
# #     print(round(money / 98.45))
#
# # DEF
# def say_hello():
#     print('GeekCamp-08 TOP!')
#
#
# say_hello()
#
#
# def algebra(x, y):
#     return x * y
#
#
# print(algebra(6, 6))
#
# # DICT
#
# person = {
#     'name': "Aidana",
#     "age": 19,
#     "region": "Chui",
# }
#
# person2 = {
#     'height': 170
# }
# person['married'] = False
# del person['region']
# person.update(person2)
# print(person)
#
# # names = ['Nur', 'FGHJ', 'yvfiy', 'tteyy']
#
# names2 = ['Kumarber', 'Kochkorbek', 'Islambek', 'Adilbek',
#          'Muhtarber', 'Bek', 'bektursun','Aidarbek', 'Alina', 'Aisuluu', 'Saltanat', 'Aidana']
#
# def filter_bek(x=names2):
#     beki = []
#     nebeki = []
#     for name in x:
#         if 'bek' in name.lower():
#             beki.append(name)
#         else:
#             nebeki.append(name)
#         print(beki)
#         print(nebeki)
#
# filter_bek()

names = [
    'Нурзада', "Нурбек", 'Акбермет', "Бектур", 'Эрмек', 'Жахонгир',
    'Бекбол', 'Нурсултан', "Айбек", 'Элина', 'Миртемир', "Бекзат",
    'Эсенбек', "Тимабек"
]

names2 = [
    'Кумарбек', 'Даниел', 'Байел', 'Жениш',
    'Инсан', 'Аскар', 'Жаркын', 'Зайнап', 'Эсенбек',
    "Нурдинбек", "Тимабек", "Адахан", "Бекболсун",
    'оолобекаудлацдлцл'
]


def filter_bek(x=names):
    beki = []
    nebeki = []
    for name in x:
        if 'бек' in name.lower():
            beki.append(name)
        else:
            nebeki.append(name)
    print(beki)
    print(nebeki)


filter_bek()
