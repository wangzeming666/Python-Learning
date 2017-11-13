
# file: console2048.py


# 主模块，用来显示2048界面和相应操作

import game2048


clr = {
    0: '\033[0;30;47m',
    2: '\033[0;30;43m',
    4: '\033[0;30;42m',
    8: '\033[0;30;46m',
    16: '\033[0;30;45m',
    32: '\033[0;30;41m',
    64: '\033[0;30;44m',
    128: '\033[1;37;43m',
    256: '\033[1;37;42m',
    512: '\033[1;37;46m',
    1024: '\033[1;37;45m',
    2048: '\033[1;37;47m',
}


def show_map():
    for r in game2048.map2048:
        for c in r:
            print(clr[c] + '      ', end=' ')
        print('\033[0m')  # 重置控制台终端

        for c in r:
            text = str(c) if c else ''
            print(clr[c] + text.center(6), end=' ')
        print('\033[0m')  # 重置控制台终端

        for c in r:
            print(clr[c] + '      ', end=' ')
        print('\033[0m')  # 重置控制台终端


while not game2048.is_gameover():  # 如果游戏没有gameover将继续
    show_map()
    key = input("请输入操作:")
    if 'a' == key:
        if game2048.left():  # 左操作
            game2048.fill_to_zero(2)
    elif 'd' == key:
        if game2048.right():  # 右操作
            game2048.fill_to_zero(2)
    elif 'w' == key:
        if game2048.up():  # 上操作
            game2048.fill_to_zero(2)
    elif 's' == key:
        if game2048.down():  # 下操作
            game2048.fill_to_zero(2)
    elif 'q' == key:
        exit()
