#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-31 22:26:54
# @Author  : Mr.Shj (shj4742@126.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
import random


def get_map(rule):
    gred = rule
    dis = [[0 for x in range(gred)] for y in range(gred)]
    return dis

def init(dis):
    cnt = len(dis[0])
    dis[random.randint(0, cnt-1)][random.randint(0, cnt-1)] = 2
def add_a_random(dis):
    cnt = len(dis[0])
    col = random.randint(0, cnt-1)
    row = random.randint(0, cnt-1)
    if dis[col][row] == 0:
        dis[col][row] = random.choice([0, 0, 0, 2, 2, 2, 2, 2])

def display(dis):
    os.system('cls')
    for x in dis:
        for y in x:
            if y == 0:
                y = '_'
            print(str(y).center(4),end=' ')
        print()
        print()

def display_score(dis):
    score = get_score(dis)
    print("-----------------------------------total score:%s" % score)

def move_one(disList, direction):
    cnt = disList.count(0)
    for x in range(cnt):
        disList.remove(0)
    kong = [0 for x in range(cnt)]
    if direction == 'L':
        disList.extend(kong)
    else:
        for x in kong:
            disList.insert(0, x)

def add_same(disList, direction):
    last = []
    if direction == 'L':
        move_one(disList, 'L')
        for i in range(len(disList) - 1):
            if disList[i] == disList[i + 1] != 0:
                disList[i] *= 2
                disList[i + 1] = 0
        move_one(disList, 'L')
    else:
        disList.reverse()
        move_one(disList, 'R')
        for i in range(len(disList) - 1):
            if disList[i] == disList[i + 1] != 0:
                disList[i] *= 2
                disList[i + 1] = 0
        disList.reverse()
        move_one(disList, 'R')

def left_and_right(dis, direction):
    for x in dis:
        add_same(x, direction)


def row_2_col(dis):
    n_row = []
    n_all = []
    cnt = len(dis[0])
    for x in range(cnt):
        for y in dis:
            n_row.append(y[x])
        n_all.append(n_row)
        n_row = []
    for x in range(cnt):  
        dis[x] = n_all[x]


def up_and_down(dis, direction):
    row_2_col(dis)
    left_and_right(dis, direction)
    row_2_col(dis)
    


def scan_direction():
    while True:
        # display(dis)
        direction = input('\n plz inpur move direction:(A,S,D,W,q(exit)):\n---->')
        if direction in ['a', 'A']:
            return "a"
        elif direction in ['s', 'S']:
            return 's'
        elif direction in ['d', 'D']:
            return 'd'
        elif direction in ['w', 'W']:
            return 'w'
        elif direction in ['q', 'Q']:
            sys.exit()
        else:
            print('input error: just input (A,S,D,W)or (Q)!')
            # os.system('clear')
def get_num_zero(dis):
    cnt_zero = 0
    for y in dis:
        cnt_zero += y.count(0)
    return cnt_zero
def get_score(dis):
    s = 0
    for x in dis:
        s += sum(x)
    return s
def check_row(dis):
     if get_num_zero(dis) == 0:
        res_row = []
        res_col = []
        for disList in dis:
            for i in range(len(disList) - 1):
                if disList[i] != disList[i + 1]:
                    res_row.append(1)
                else:
                    res_row.append(0)
            if 0 in res_row:
                res_col.append(0)
            else:
                res_col.append(1)
        if 0 not in res_col:
            return True
def check_col(dis):
    row_2_col(dis)
    res = check_row(dis)
    row_2_col(dis)
    return res
def check_exit(dis):
    if check_row(dis) and check_col(dis):
        mid = get_score(dis)
        print('the end your score is :%d'%mid)
        print('game over')
        sys.exit()
def process_direction(res, dis):
    if res == 'a':
        left_and_right(dis, 'L')
    elif res == 's':
        up_and_down(dis, 'R')
    elif res == 'd':
        left_and_right(dis, "R")
    elif res == 'w':
        up_and_down(dis, 'L')

def main():
    # 设置规格"2"-> 2*2 "4"->4*4 "8"->8*8
    dis = get_map(2)
    init(dis)
    while True:
        add_a_random(dis)
        # 显示和求和在一起
        display(dis)
        # 只需替换扫描方向函数
        check_exit(dis)
        display_score(dis)
        res = scan_direction()
        process_direction(res, dis)

        print()


if __name__ == '__main__':
    main()
