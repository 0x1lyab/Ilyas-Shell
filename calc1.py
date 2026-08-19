
# аддон к ilyascmd_main.py

# calc1.py
class clr: # цвета такие
    r = '\033[91m'
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[94m'
    c = '\033[96m'
    v = '\033[95m'
    o = '\033[93m'
    w = '\033[0m'
    bd = '\033[1m'

ncalc1 = f"{clr.y}{clr.bd}calc1.py: {clr.w}"

oprtlist = ['+','-','*','/','//','**']
def calcdotpy():
    def execalc(a, oprt, b):
        if oprt == '*':
            return a * b
        elif oprt == '/':
            return a / b
        elif oprt == '+':
            return a + b
        elif oprt == '-':
            return a - b
        elif oprt == '**':
            return a ** b
        elif oprt == '//':
            return a // b
        else:
            print(f'{ncalc1}Операция не найдена, доступные операции: +, -, /, //, *, **. Для вычисления корня: [число] ** 0,5')


    while True:
        try:
            problem = input(f'{clr.y}{clr.bd}calc1.py > {clr.w}').split()
            num1 = float(problem[0])
            oprt = str(problem[1])
            num2 = float(problem[2])
            if oprt in oprtlist:
                try:
                    print(f"{ncalc1}Ответ: {execalc(num1, oprt, num2)}.")
                except ValueError:
                    print(f"{ncalc1}Неправильное значение чисел или операции.")
                except ZeroDivisionError:
                    print(f"{ncalc1} Ответ: дибил на ноль делить незя")
            else: 
                print(f'{ncalc1}Неверная операция.')
        except ValueError:
            print(f"{ncalc1}Неправильное значение чисел или операции.")
        except KeyboardInterrupt:
            print(f'\n{ncalc1}Сессия calc1.py завершенна.')
            break
        except IndexError:
            continue