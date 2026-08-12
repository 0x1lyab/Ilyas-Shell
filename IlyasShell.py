
### --<( Ilya's:Shell )>--
# Приветствую в коде оболочки! Код полностью читаемый и понятный.
# Задумка была чтобы быть улучшенной версией ilya's:cmd_, которая работает через модули.
# Кстати, посмотрите в configs/configShell.py там находится конфиг оболочки! 
# Пожалуйста, не удаляйте его. Без него оболочка не будет работать

#!/usr/bin/env python3
# ^^^ шебанг ^^^

# -- Импорты --
import os
import random
import time
import readline
try:
    import configShell as config
except ModuleNotFoundError:
    raise SystemError('Файл конфига не найден. Работа оболочки невозможна.')
try:
    import calc1
    import pifagor
except ModuleNotFoundError:
    pass

# -- Переменные --
col = config.col
USER = os.getlogin()
prompt = config.PROMPT
dead_list = config.DEAD_LIST
ilya = f'{col.g}{col.bd}Илья:{col.rs}'
dont_dare = config.KILL_BLACK_LIST
dont_dare.extend([
    'чижик', 'chizhik', 'илья', 'ilya', "пыжуля", "чыжык", USER
])
history_file = './.history_file'
try:
    readline.read_history_file(history_file)
except FileNotFoundError:
    with open('.history_file', 'w') as f:
        pass
    readline.read_history_file('./.history_file')

INTERACTIVE = False

# -- Команды --
def shelp(): # к сожалению help() нельзя использовать, он зарезервирован
    if INTERACTIVE == True:
        print(f"{ilya} Вот тебе список:\n",
            'kill <цель>                        - убить кого-нибудь, убивать мертвого нельзя\n',
            'revive <цель>                      - возродить кого-нибудь, возрождать живого тоже нельзя\n',
            'dead_list                          - список мёртвых\n',
            'help                               - показать это меню\n',
            'whoami                             - показать юзернейм\n'
            'exit/quit/break                    - выйти из оболочки ;(\n',
            # 'clear                            - очистить консоль\n',
            # 'version                          - версия оболочки\n',
            'calc/calculator                    - запуск скрипта calc1.py (через вызов функции, напрямую невозможно)\n',
            'rng/random/randomizer <min> <max>  - вывести рандомное число в заданом диапазоне\n',
            'pif/pifagor                        - запуск скрипта pifagor.py (через вызов функции, напрямую невозможно)\n',
            'guess                              - игра в угадай число, правила будут озвучены при вызове (для вызова напишите команду guess)\n',
            'echo <текст>                       - вывести текст'
        )
    elif INTERACTIVE == False:
        print(f"{ilya} Вот тебе список:\n",
            f"{col.bd}StartShell()              - запустить оболочку в интерактивном режиме{col.rs}\n",
            "kill(['<цель>'])           - убить кого-нибудь, убивать мертвого нельзя\n",
            "revive(['<цель>'])         - возродить кого-нибудь, возрождать живого тоже нельзя\n",
            "fdead_list()               - список мёртвых\n",
            "shelp()                    - показать это меню\n",
            "whoami()                   - показать юзернейм\n"
            "calcdotpy()                - запуск скрипта calc1.py, импортировать перед запуском\n",
            "rng([<min>, <max>])        - вывести рандомное число в заданном диапазоне\n",
            "pifagorpy()                - запуск скрипта pifagor.py, импортировать перед запуском\n",
            "guess()                    - игра в угадай число\n",
            "echo(['<текст>'])          - вывести текст, конкретно здесь это бесполезно, используйте лучше print()"
        )

class KillAttemptError(Exception):
    pass
def kill(target):
    target = ' '.join(target)
    target_ls = target.lower().strip()
    global dead_list
    if any(bad_name in target_ls for bad_name in dont_dare):
        raise KillAttemptError(f"{col.rbd}{random.choice([ #! передаю привет дипсику
            'don\'t dare',
            'не смей',
            'Молодец! Ты сломал оболочку!!!',
            'something is coming',
            '???',
            'nosey, aren\'t we?',
            'не убивай меня',
            'зачем меня убивать?',
            'проверь шкаф',
            'бибизяка! 🐦 (это моя оболочка, я имею право писать всё что угодно)'
        ])}{col.w}")
    elif target not in dead_list:
        confirm = input(f'{ilya}Ты уверен? [y/N] ').lower().strip()
        if confirm in ['y','д']:
            dead_list.append(target)
            print(f'{ilya}{target} УБИТ!')
        else:
            print(f'{ilya}{col.v}{target} остаётся в живых!{col.rs}')
    else:
        print(f'{ilya} как я смогу убить мёртвого?')

def revive(target):
    global dead_list
    target = ' '.join(target)
    print('...')
    time.sleep(4)
    if target.lower().strip() in dead_list:
        dead_list.remove(target.lower().strip())
        print(f"{ilya} Кто это?{col.rs}")
        time.sleep(3)
        print(f"{USER}: Где?{col.rs}")
        time.sleep(2)
        print(f"{ilya} Там! Наверху!!{col.rs}")
        time.sleep(2)
        print('...')
        time.sleep(3)
        print(f"{col.rbd}???: {col.rs}{col.y}It is {target}...{col.rs}")
        time.sleep(3)
        print(f"{col.y}{col.bd}{target}: {col.rs}{col.y}Я..{col.rs}")
        time.sleep(1)
        print(f"{col.y}{col.bd}{target}: {col.rs}{col.y}Я снова в живых??{col.rs}")
        time.sleep(3)
        print(f"{col.y}{col.bd}{target}: {col.rs}{col.y}Спасибо, тебе {USER}.{col.rs}")
        time.sleep(2)
        print(f"{col.y}{col.bd}{target}: {col.rs}{col.y}Ты спас меня..{col.rs}")
        time.sleep(5)
    else:
        print(f"{col.rbd}???: {col.y}{target} is already alive.{col.rs}")
        time.sleep(2)

def whoami():
    # омг посхалко
    if USER == f'ilya':
        print(f"{ilya} Тебя зовут.. {col.w}")
        time.sleep(2)
        print(f"{ilya} Стоп чё?. {col.w}")
        time.sleep(1)
        print(f"{ilya} Тебя зовут {col.b}{col.bd}Илья [🛠️]?{col.w}")
        time.sleep(3)
        print(f"{ilya} Это либо совпадение, либо..{col.w}")
        time.sleep(2)
        print(f'{ilya} ..либо ты являешься {col.b}{col.bd}создателем{col.w}. ')
        time.sleep(2)
        print(f"И да меня зовут {col.b}{col.bd}Илья [🛠️]{col.w} и я это все пишу в VSCodium(вскод но на линуксе, да я на арче :Р).")
        print('Я думаю что это можно считать за пасхалку!')
        time.sleep(4)
        print('Молодец что нашёл!!')
        time.sleep(2)
    else:
        print(f"{ilya} Тебя зовут {col.y}{col.bd}{USER}.")

def guess():
    guess_num = random.randint(1, 10000)
    guess_out = 0
    print(f'{ilya} Правила: Я загадываю число, а ты отгадываешь.',
        f'\nЧтобы отгадать число тебе нужно будет писать число, а я говорю больше оно или меньше.',
        f'\nИ так до тех пор пока ты не отгадаешь число. Для старта напиши любое число. (Число от 1 до 10тыс.)')
    ходы = 0
    while True:
        try:
            guess_out = int(input(f'{prompt}{col.v} [GUESS]{col.w} > '))
            ходы += 1
            if guess_out > guess_num:
                print(f'{ilya} {col.rbd}Число меньше!{col.w}')
            elif guess_out < guess_num:
                print(f'{ilya} {col.g}{col.bd}Число больше!{col.w}')
            elif guess_out == guess_num:
                print(f'{ilya} {col.y}{col.bd}Победа!!{col.w} Ходы: {ходы}.')
                break
        except ValueError:
            print(f'{ilya} {USER}, вводи числа!')
        except KeyboardInterrupt:
            print(f'{ilya} Сдался? Ну, ладно..')
            break
        except EOFError:
            print(f'{ilya} почему?? ;(')
def echo(arg):
    echout = ' '.join(arg)
    print(f'{echout}')
def rng(arg):
    if len(arg) < 2:
        print(f"{ilya} Синтаксис: rng <min> <max>")
        return
    try:
        min_val = int(arg[0])
        max_val = int(arg[1])
        result = random.randint(min_val, max_val)
        phrases = ['Твое рандомное число: ', 'тебе выпало: ', 'лох :)))) ', 'Your RNG number: ']
        print(f'{ilya}{random.choice(phrases)}{result}')
    except ValueError:
        print(f"{ilya} Вводи только числа! Минимальное число не может быть больше максимального!!")
    except IndexError:
        print(f'{ilya} (илья не придумал сообщение)')
def fdead_list():
    global dead_list
    if dead_list:
        print(f"{col.rbd}Илья: Убитые: {', '.join(dead_list)}{col.w}")
    else:
        print(f"{col.g}{col.bd}Илья: Все живы.{col.w}")
def binary_code(arg):
    try:
        flag = arg[0]
        num = int(arg[1])
        binstr = arg[1]
        if flag == '-e':
            bin_num = []
            while num > 0:
                ostatok = num % 2
                if ostatok == 1:
                    bin_num.append(str(1))
                else:
                    bin_num.append(str(0))
                num //= 2
            print(f'{ilya} Результат: {''.join(reversed(bin_num))}')
        elif flag == '-d':
            print(f'{ilya} Результат: {int(binstr, 2)}')
    except ValueError:
        print(f'{ilya} error')
    except IndexError:
        print(f'{ilya} error')

# -- Словарик команд --
COMMANDSWARGS = {
    'kill':kill,
    'revive':revive,
    'respawn':revive,
    'rebirth':revive,
    'echo':echo,
    'rng':rng,
    'random':rng,
    'randomizer':rng,
    'binary':binary_code
}
COMMANDS = {
    'help':shelp,
    'whoami':whoami,
    'calc':calc1.calcdotpy,
    'calc1':calc1.calcdotpy,
    'calc1.py':calc1.calcdotpy,
    'calculator':calc1.calcdotpy,
    'pif':pifagor.pifagorpy,
    'pifagor':pifagor.pifagorpy,
    'guess':guess,
    'dead_list':dead_list
}

#  -- Основной цикл --
def StartShell():
    global INTERACTIVE
    INTERACTIVE = True
    print( # приветствие при запуске StartShell()
        f'{col.bd}Добро пожаловать в оболочку {col.g}{col.bd}💚 Ilya\'s{col.c}:Shell 🐚,{col.w}\n',
        f'улучшенную версию {col.g}{col.bd}ilya\'s{col.v}:{col.c}cmd_{col.w} написаную на {col.y}Python 3.1!{col.rs}'
    )
    if config.USER_COMMANDS.enabled == True:
        COMMANDS.update(config.USER_COMMANDS.list_ )
        COMMANDSWARGS.update(config.USER_COMMANDS.list_with_args)
        print(f'{col.bd}{col.g}Включенны пользовательские команды.')
    while True:
        try:
            inp = input(f'{prompt} > ').split()
            cmd = inp[0]
            arg = inp[1:]
        except KeyboardInterrupt:
            INTERACTIVE = False
            # raise SystemExit(f'\n{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            print(f'{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except EOFError:
            INTERACTIVE = False
            # raise SystemExit(f'\n{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            print(f'{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        except IndexError:
            continue
        readline.write_history_file(history_file)
        if cmd in COMMANDSWARGS:
            if arg:
                COMMANDSWARGS[cmd](arg)
            else:
                print(f'{col.rbd}Илья: Команда {cmd} требует аргумент!{col.rs}')
        elif cmd in COMMANDS:
            COMMANDS[cmd]()
        elif cmd == 'exit':
            INTERACTIVE = False
            # raise SystemExit(f'{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            print(f'{col.rbd}Илья: ЗА ЧТО ?!??!?!?!??!?!??!?787:?%?*(?№"*(?(;"291Н87УНЦ378АНУК7П')
            break
        else:
            print(config.COMMAND_NOT_FOUND)

# -- Запуск --
if __name__ == '__main__': # Если файл запущен напрямую, то запускается StartShell() и оболочка начинает работать
    StartShell()