# 游戏主界面
# 坦克  我方  敌方
# 炮弹
# 隔离墙
# 爆炸

from random import randint

import sys,time

import pygame
from pygame.locals import *


class TankMain(object):
    width=800
    height=500
    # 坦克大战主窗口

    #开始游戏的方法
    def startGame(self):
        pygame.init() # pygame模块初始化,加载系统资源
        # 创建一个屏幕  屏幕地大小  窗口特性 0窗口不可拉伸 0  可拉伸 RESIZEBLE 全屏 FULLSCREEN
        #32位颜色
        screen = pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        #设置标题
        pygame.display.set_caption("坦克大战")
        my_tank = My_Tank(screen)
        enemy_list=[]

        for i in range(1,6):
            enemy_list.append(Enemy_Tank(screen))


        while True:
            #设置窗口颜色 RGB(0,100,200)
            screen.fill((0,0,0))
            # 显示左上角文字
            screen.blit(self.write_text(), (0,5))
            self.get_event(my_tank) # 获取时间  做处理
            my_tank.display()
            my_tank.move()




            for enemy in enemy_list:
                enemy.display()
                enemy.random_move()
            # 显示重置
            time.sleep(0.02)
            pygame.display.update()
    # 获取所有的时间(键盘,鼠标)
    def get_event(self,my_tank):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame() # 程序退出
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    my_tank.direction="左"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_RIGHT:
                    my_tank.direction="右"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_UP:
                    my_tank.direction="上"
                    my_tank.stop=False
                    
                    # my_tank.move()
                if event.key == K_DOWN:
                    my_tank.direction="下"
                    my_tank.stop=False

                    # my_tank.move()
                if event.key == K_ESCAPE: # 敲击ESC 退出游戏
                    self.stopGame()
            if event.type==KEYUP:
                if event.key==K_LEFT or event.key==K_RIGHT or event.key==K_UP or event.key==K_DOWN:
                    my_tank.stop=True

    def stopGame(self):
        sys.exit()
    # 屏幕上显示文字
    def write_text(self):
        font = pygame.font.SysFont('simsunnsimsun', 20) # 定义一个字体
        text_sf = font.render("敌方坦克数量为5", True, (255,0,0)) # 根据字体创建文件图像
        return text_sf
    #设置游戏窗口标题
    def set_title():
        pass

# 坦克大战游戏中所有对象的超级父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 所有对象的共同属性
        self.screen=screen
class Tank(BaseItem):
    # 定义类属性.所有坦克对象高和宽都一样
    width=28
    height=28

    def __init__(self,screen,left,top):
        super().__init__(self,screen)
        # self.screen=screen # 坦克在移动或者显示过程中需要用到的屏幕窗口
        self.direction="下" #坦克方向
        self.speed=5 # 坦克速度
        self.stop=False
        self.images={} #坦克所有图片
        self.images["下"]=pygame.image.load("pic/坦克下.jpg") # load返回surface
        self.images["上"]=pygame.image.load("pic/坦克上.jpg")
        self.images["左"]=pygame.image.load("pic/坦克左.jpg")
        self.images["右"]=pygame.image.load("pic/坦克右.jpg")
        self.image=self.images[self.direction] # 坦克的图片由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        
        
        self.live = True # 坦克是否活着

    # 把坦克图片显示在窗口上
    def display(self):
        self.image=self.images[self.direction]
        self.screen.blit(self.image,self.rect)

    def move(self):
        if not self.stop: # 如果坦克不是停止状态
            if self.direction =="左":
                if self.rect.left>0: # 判断坦克是否已经到边界
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            elif self.direction == "右":
                if self.rect.right<TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.rect.right=TankMain.width
            elif self.direction == "上":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top=0
            elif self.direction == "下":
                if self.rect.bottom<TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.rect.bottom=TankMain.height


    def fire(self):
        pass

class My_Tank(Tank):
    print "MRO:", [x.__name__ for x in Tank.__mro__]
    def __init__(self,screen):
        super().__init__(self, screen,275,400)








        self.stop=True
    def move(self):
        if not self.stop: # 如果坦克不是停止状态
            if self.direction =="左":
                if self.rect.left>0: # 判断坦克是否已经到边界
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            elif self.direction == "右":
                if self.rect.right<TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.rect.right=TankMain.width
            elif self.direction == "上":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top=0
            elif self.direction == "下":
                if self.rect.bottom<TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.rect.bottom=TankMain.height


class Enemy_Tank(Tank):
    def __init__(self,screen):
        super().__init__(self,screen,randint(1,5)*100,200)
        self.speed=3
        self.step=10
        self.get_random_direction()

    def get_random_direction(self):
        r = randint(0,4) # 坦克移动方向和停止的随机数
        if r == 4:
            self.stop=True
        elif r == 1:
            self.direction = "左"
            self.stop=False
        elif r == 2:
            self.direction = "右"
            self.stop=False
        elif r == 3:
            self.direction = "下"
            self.stop=False
        elif r == 0:
            self.direction = "上"
            self.stop=False

    def random_move(self):
        if self.live:
            if self.step==0:
                self.get_random_direction()
                self.step=10
            else:
                self.move()
                self.step-=1

class Missile(BaseItem):
    def __init__(self,screen):
        super().__init__(self,screen)  

        super().__init__(self.screen)





def main():
    game=TankMain()
    game.startGame()

def prn_obj(obj): 
  print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


if __name__ == '__main__':
    main()
    
