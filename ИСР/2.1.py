"""
    Разработать прототип программы "Калькулятор", позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.  [ без использования '@' ]
    Шеховцова Е. Г.
"""

def jr(calc):
    def wrapperr():
        string = calc()
        if string:
            try:
                with open('journal.txt', 'a+') as j:
                    j.write(string)
            except FileNotFoundError:
                print('Файл не найден')
    return wrapperr

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
            print("Деление на ноль!")
            return False
        res = x/y            
    else:
        print("Неверный знак операции!")
        return False
    return (str(x) + s + str(y) + '=' + str(res) + '\n')

while True:
    k = jr(calc)
    k()
