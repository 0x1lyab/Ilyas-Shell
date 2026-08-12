class col:
    r = '\033[91m' # красный
    g = '\033[92m' # зелёный
    y = '\033[93m' # желтый
    b = '\033[94m' # синий
    c = '\033[96m' # голубой
    v = '\033[95m' # фиолетовый
    o = '\033[93m' # оранжевый(на самом деле жёлтый)
    w = '\033[37m' # белый
    rs = '\033[0m' # ресет
    bd = '\033[1m' # жирный
    rbd = '\033[1;91m' # жирный красный

PROMPT = f'{col.g}{col.bd}Ilya\'s{col.c}:Shell{col.rs}'
DEAD_LIST = []
COMMAND_NOT_FOUND = f'{col.rbd}Илья: Команда не найдена!{col.rs}'
KILL_BLACK_LIST = []


# -- Пользовательские команды --
class USER_COMMANDS:
    enabled = False # заменить на True чтобы включить
    # -- Команды --
    def hello():
        print('hello')
    def chizhik_says(arg):
        text = ' '.join(arg)
        print(f"Чижик говорит: {text}")
    # -- Ссылки на команды --
    list_with_args = {
        'chizhik_says': chizhik_says
    }
    list_ = {
        # пример:
        # 'слово вызова команды':ссылка на функцию
        'hello':hello
    }
