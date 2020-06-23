"""
    Рефакторинг (модификация) программы с декоратором модулем functools и использование его функционала.
    Шеховцова Е. Г.
"""
import functools

def jr(calc):
    @functools.wraps(calc)
    def wrapperr():
        string = calc()
        if string:
            try:
                with open('journal.txt', 'a+') as j:
                    j.write(string)
            except FileNotFoundError:
                print('Файл не найден')
    return wrapperr

@jr
def calc():
    s = input("Введите одно из следующих операции: +,-,*,/,^: ")
    try:
        x = float(input("x="))
    except ValueError:
        print('Неверно введен x')
    try:
        y = float(input("y="))
    except ValueError:
        print('Неверно введен y')
    if s == '+':
        res = x+y
    elif s == '-':
        res = x-y
    elif s == '*':
        res = x*y
    elif s == '^':
        res = pow(x, y)
    elif s == '/':
        if not y:
            print("Деление на ноль")
            return False
        res = x/y            
    else:
        print("Неверный знак операции!")
        return False
    return (str(x) + s + str(y) + '=' + str(res) + '\n')

while True:
    calc()
