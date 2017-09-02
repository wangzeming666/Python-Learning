import pygame, random, sys
from math import sqrt
import threading
# 从Game2048 和

# 出现随机数，创建新实例，调用位置函数为位置赋值，调用方块函数，调用文本函数
# 出现键盘事件，检测是否可以移动（溢出边界），为所有待移动实例建立线程，调用移动函数，移动结束释放线程，删除无用实例
# 为新出现的随机数和相加数的和创建新的类实例，调用位置函数，调用方块函数，递归调用文本函数为所有文本重新绘制

class Game2048(pygame):
    #游戏初始化
    def __init__(self):
        
        # 初始化字体模块
        self.font.init()
        # 设置字体、大小
        self.number = self.font.SysFont('arial', 50)
        # 是否加粗，是
        self.number.set_bold(True)
        # 位置
        self.Heng = 0
        self.Gao = 0
        # 数字
        self.text = ''
        # 方块颜色
        self.color = [255,0,0]
        # 移动方向， 向下向右为正，静止为零，其余负值
        self.way = (0,0)
        # 第一个为移动的方块坐标位置（0-3）
        # 第二个为静止等待被替换的方块坐标（0-3）
        self.fir = (0,0)
        self.sec = (3,3)

        
    def WeiZhi(self,x,y):
        if x == 0:
            self.Gao = 20
        if x == 1:
            self.Gao = 170
        if x == 2:
            self.Gao = 320
        if x == 3:
            self.Gao = 470
        if y == 0:
            self.Heng = 20
        if y == 1:
            self.Heng = 170
        if y == 2:
            self.Heng = 320
        if y == 3:
            self.Heng = 470
        

    def rectDisplay(self):
        #绘制矩形
        self.draw.rect(screen,self.color,[self.Heng,self.Gao,130,130],0)
#        rect01 = pygame.draw.rect(screen,[255,0,0],[JianJu*2+length,JianJu,130,130],0)
#        rect02 = pygame.draw.rect(screen,[255,0,0],[(JianJu*1.5+length)*2,JianJu,130,130],0)
#        rect03 = pygame.draw.rect(screen,[255,0,0],[JianJu*4+length*3,JianJu,130,130],0)
#        rect10 = pygame.draw.rect(screen,[255,0,0],[JianJu,JianJu*2+length,130,130],0)        
#        rect11 = pygame.draw.rect(screen,[255,0,0],[JianJu*2+length,JianJu*2+length,130,130],0)
#        rect12 = pygame.draw.rect(screen,[255,0,0],[JianJu*3+length*2,JianJu*2+length,130,130],0)
#        rect13 = pygame.draw.rect(screen,[255,0,0],[JianJu*4+length*3,JianJu*2+length,130,130],0)
#        rect20 = pygame.draw.rect(screen,[255,0,0],[JianJu,(JianJu*1.5+length)*2,130,130],0)
#        rect21 = pygame.draw.rect(screen,[255,0,0],[JianJu*2+length,(JianJu*1.5+length)*2,130,130],0)
#        rect22 = pygame.draw.rect(screen,[255,0,0],[(JianJu*1.5+length)*2,JianJu*3+length*2,130,130],0)
#        rect23 = pygame.draw.rect(screen,[255,0,0],[JianJu*4+length*3,JianJu*3+length*2,130,130],0)
#        rect30 = pygame.draw.rect(screen,[255,0,0],[JianJu,JianJu*4+length*3,130,130],0)
#        rect31 = pygame.draw.rect(screen,[255,0,0],[JianJu*2+length*1,JianJu*4+length*3,130,130],0)
#        rect32 = pygame.draw.rect(screen,[255,0,0],[JianJu*3+length*2,JianJu*4+length*3,130,130],0)
#        rect33 = pygame.draw.rect(screen,[255,0,0],[JianJu*4+length*3,JianJu*4+length*3,130,130],0)

    def numDisplay(self):




        
        # 设置文字内容， 颜色
        
        num = self.number.render(self.text, True, (255,255,255))
        
        # 检测文字大小
 

#    font = pygame.font.Font(None, 80)
#    text = 'Fonty'
#    size = font.size(text)
#    no AA, no transparancy, normal






    
              
        
        
        # 绘制文字

        if len(text) == 1:
            screen.blit(num,(self.Heng+50,self.Gao+35))
        if len(text) == 2:
            screen.blit(num1,(self.Heng+35,self.Gao+35))
        if len(text) == 3:
            screen.blit(num2,(self.Heng+20,self.Gao+35))
        if len(text) == 4:
            screen.blit(num3,(self.Heng+15,self.Gao+35))




# 随机出现一个数字，画一个方块，记录位置。相加后，记录结果位置。由此得到移动先后的两个位置

    def move(self):
        #'设置好两对数字坐标，和一对方向坐标，然后再调用move，向右向下为正值，无移动为零’
        self.WeiZhi(self.fir1[0],self.fir[1])
        x, y = self.Heng, self.Gao
        self.WeiZhi(sec[0], sec[1])
        a, b = self.Heng, self.Gao
        way = self.ways
        if way[0] > 0:
            start, end, length = x, a, 10
            for loop in range(start, end, length):
            # 延时，制造动画效果
                self.time.delay(200)
                self.draw.rect(screen, [105, 105, 105], [loop, b, 130, 130], 0)
                self.Heng += 10
                self.rectDisplay()
                self.numDisplay()
            
# self.numDisplay()    调用完移动函数以后，创建新数字的类和线程，覆盖上去
            

        elif way[1] > 0:
            start, end, length = y, b, 10
            for loop in range(start, end, length):
                # 延时，制造动画效果
                self.time.delay(200)
                self.draw.rect(screen, [105, 105, 105], [start, a, 130, 130], 0)
                self.Gao += 10
                self.rectDisplay()
                self.numDisplay()

        elif way[0] < 0:
            start, end, length = a, x, -10
            for loop in range(start, end+, length):
                # 延时，制造动画效果
                self.time.delay(200)
                self.draw.rect(screen,[105, 105, 105], [start, y, 130, 130], 0)
                self.Heng -= 10
                self.rectDisplay()
           ## # 如果根据坐标位置能查询结果，则运行如下代码
           ##self.numDisplay(find(a, b))

        elif way[1] < 0:
            start, end, length = b, y, -10
            for loop in range(start, end, length):    
                # 延时，制造动画效果
                self.time.delay(200)
                self.draw.rect(screen,[105, 105, 105], [start, x, 130, 130], 0)
                self.Gao -= 10
                self.rectDisplay()
            # #如果根据坐标位置能查询结果，则运行如下代码
            ##self.numDisplay()

        
    def color(self):
        for i in range(11):
            if 2**i == int(self.text):
                # 每增加2的多一次幂结果颜色加深
                self.color = [ -18, -18, -18]
        
            
               











# Pygame初始化
pygame.init()
screencaption=pygame.display.set_caption('Game2048')
screen = pygame.display.set_mode([620,620])
screen.fill([105,105,105])
G = Game2048()

clock = pygame.time.Clock()


while True:
    clock.tick(30)
    # 传递位置参数
    G.WeiZhi(0,0)
    # 根据位置参数绘制矩形
    G.rectDisplay()
    # 根据位置参数绘制数字 ， 另外我想创建一个数字类，可以初始化数字位置参数
    G.WeiZhi(0,0)
    G.numDisplay('1')
    # 传递数字num，位置进函数打印到屏幕
    #G.Display(str(num),20,20)


    # 检测事件，  如果前面程序太耗费时间，则需要上锁，在一定时间后解锁
        for event in pygame.event.get():
            if event == KEY_DOWN:
                    # 循环遍历移动对象
                    pass
                        # 移动事件，先删除不移动位置的方块，然后移动远距离的方块，传递两对坐标参数
                        G.way = (0,1)
                        G.move()

        



        # 设置叉号检测退出
        if event.type==pygame.QUIT:
            sys.exit()

    #刷新画面
    pygame.display.update()
















