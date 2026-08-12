# решалка теоремы пифагора
def pifagorpy():
    print('^C для выхода.')
    while True:
        try:
            input1 = input('>>> ').split()
            if len(input1) != 2:
                print('Пожалуйста, напишите ДВА ЦЕЛЫХ числа. Ctrl + C для выхода.')
            num1 = int(input1[0])
            num2 = int(input1[1])
            root = float(( num1 ** 2  +  num2 ** 2 ))
            result = root ** 0.5
            print(f'{result} Квадрат = {root}')
        except KeyboardInterrupt:
            break
        except ValueError:
            print('Неизвестное значение.')
        except IndexError:
            continue