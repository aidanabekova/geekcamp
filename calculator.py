first_number = int(input('Введите первое число: '))
oper = input('выберите операцию над числами: +, -, *, /, **, //: ')
second_number = int(input('Введите второе число: '))

if oper == '+':
    answear1 = first_number + second_number
    print(answear1)
elif oper == '-':
    answear2 = first_number - second_number
    print(answear2)
elif oper == '*':
    answear3 = first_number * second_number
    print(answear3)
elif oper == '/' and second_number == 0:
    print('Делить на 0 нельзя!!!')
elif oper == '/':
    answear4 = first_number / second_number
    print(answear4)
elif oper == '**':
    answear5 = first_number ** second_number
    print(answear5)
elif oper == '//':
    answear6 = first_number // second_number
    print(answear6)
else:
    print('Нельзя вводить такое!')



