#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02 13:56:34
# @Author  : Mr.Shj (shj4742@126.com)
# @Link    : ${link}
# @Version : $Id$

from game2048 import *


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
