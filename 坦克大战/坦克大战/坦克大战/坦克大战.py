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
    my_tank_missile_list=[]
#    enemy_list=[]
    enemy_list=pygame.sprite.Group()     #敌方坦克的组)
    explode_list =[]
    enemy_missile_list=pygame.sprite.Group()     #敌方坦克的组)
    wall=None
    my_tank = None
    # 坦克大战主窗口

    #开始游戏的方法
    def startGame(self):
        pygame.init() # pygame模块初始化,加载系统资源
        # 创建一个屏幕  屏幕地大小  窗口特性 0窗口不可拉伸 0  可拉伸 RESIZEBLE 全屏 FULLSCREEN
        #32位颜色
        screen = pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        #设置标题
        pygame.display.set_caption("坦克大战")
        TankMain.wall=Wall(screen, 65, 160, 30, 120)
        
        
        TankMain.my_tank = My_Tank(screen)
        if len(TankMain.enemy_list) == 0:
            
            for i in range(1,ENEMY_NUMBER): # 游戏开始初始化5个敌方坦克
               TankMain.enemy_list.add(Enemy_Tank(screen)) #把坦克放到坦克组中

        while True:
            if len(TankMain.enemy_list)<5:
                TankMain.enemy_list.add(Enemy_Tank(screen))
            #设置窗口颜色 RGB(0,100,200)
            screen.fill((0,0,0))
            pygame.draw.rect(screen, (0, 233, 9), Rect(400, 30, 100, 30),3)
            # 显示左上角文字
            for i, text in enumerate(self.write_text(), 0):
                screen.blit(text, (0,5+(i*20)))
            # 显示墙
            TankMain.wall.display()
            TankMain.wall.hit_other()
            self.get_event(TankMain.my_tank, screen) # 获取事件  做处理
            if TankMain.my_tank:
                TankMain.my_tank.hit_enemy_missile()# 我方的坦克和敌方的炮弹进行碰撞检测
            if TankMain.my_tank and TankMain.my_tank.live:
#                self.get_event(TankMain.my_tank) # 获取事件  做处理

                TankMain.my_tank.display()
                TankMain.my_tank.move()
            else:
#                del(TankMain.my_tank)
                TankMain.my_tank=None
#                print("GAME OVER")
#                sys.exit()
                




            for enemy in TankMain.enemy_list:
                enemy.display()
                enemy.random_move()
 #               ============================敌方开火=================================================
                enemy.random_fire()
            #显示所有的我方炮弹
            for m in TankMain.my_tank_missile_list:
                if m.live:
                    
                    m.display()
                    m.hit_tank()#炮弹打中敌方坦克
                    m.move()
                else:
                    TankMain.my_tank_missile_list.remove(m)
            #显示所有的敌方炮弹
            for m in TankMain.enemy_missile_list:
                if m.live:
                    
                    m.display()
#                    m.hit_tank()#炮弹打中我方坦克 
                    m.move()
                else:
                    TankMain.enemy_missile_list.remove(m)                    
                    
                    
                    
            for explode in TankMain.explode_list:
                explode.display()
            # 显示重置
            time.sleep(0.02)
            pygame.display.update()
    # 获取所有的时间(键盘,鼠标)
    def get_event(self,my_tank, screen):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame() # 程序退出
            if event.type ==KEYDOWN and not my_tank and event.key==K_n:
                TankMain.my_tank=My_Tank(screen)
            if event.type == KEYDOWN and my_tank:
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
                if event.key == K_SPACE:
                    m=my_tank.fire()
                    m.good=True#我方坦克的炮弹
                    TankMain.my_tank_missile_list.append(m)
                    
            if event.type==KEYUP and my_tank:
                if event.key==K_LEFT or event.key==K_RIGHT or event.key==K_UP or event.key==K_DOWN:
                    my_tank.stop=True

    def stopGame(self):
        sys.exit()
    # 屏幕上显示文字
    def write_text(self):
        font = pygame.font.SysFont('simsunnsimsun', 12) # 定义一个字体
        text_sf1 = font.render("敌方坦克数量为%d"%len(TankMain.enemy_list), True, (255,0,0)) # 根据字体创建文件图像
        text_sf2= font.render("我方炮弹数量为%d"%len(TankMain.my_tank_missile_list), True, (255,0,0)) # 根据字体创建文件图像
        
        return text_sf1, text_sf2
    #设置游戏窗口标题
    def set_title():
        pass

# 坦克大战游戏中所有对象的超级父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 所有对象的共同属性
        self.screen=screen
        
        # 把坦克图片显示在窗口上
    def display(self):
        if self.live:
            self.image=self.images[self.direction]
            self.screen.blit(self.image,self.rect)

class Tank(BaseItem):
    # 定义类属性.所有坦克对象高和宽都一样
    width=28
    height=28

    def __init__(self,screen,left,top):
        super().__init__(screen)
        # self.screen=screen # 坦克在移动或者显示过程中需要用到的屏幕窗口
        self.direction="下" #坦克方向
        self.speed=5 # 坦克速度
        self.stop=False
        self.images={} #坦克所有图片
        self.images["下"]=pygame.image.load("D:\scrapyProject\pic\坦克下.png") # load返回surface
        self.images["上"]=pygame.image.load("D:\scrapyProject\pic\坦克上.png")
        self.images["左"]=pygame.image.load("D:\scrapyProject\pic\坦克左.png")
        self.images["右"]=pygame.image.load("D:\scrapyProject\pic\坦克右.png")
        self.image=self.images[self.direction] # 坦克的图片由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        
        
        self.live = True # 坦克是否活着
        
        self.oldtop=self.rect.top
        self.oldleft=self.rect.left

    def stay(self):
        self.rect.top=self.oldtop
        self.rect.left=self.oldleft

    def move(self):
        if not self.stop: # 如果坦克不是停止状态
        
            self.oldleft=self.rect.left
            self.oldtop=self.rect.top
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
        m = Missile(self.screen,  self)
        return m

class My_Tank(Tank):
#    print("My_Tank MRO:", My_Tank.__mro__)
    def __init__(self,screen):
        super().__init__(screen,275,400)
        self.stop=True
        self.live=True


    def hit_enemy_missile(self):
        hit_list=pygame.sprite.spritecollide(self, TankMain.enemy_missile_list, False)
        for m in hit_list:#我方坦克中弹
            m.live=False
            TankMain.enemy_missile_list.remove(m)
            self.live=False
            explode=Explode(self.screen, self.rect)
            TankMain.explode_list.append(explode)
            




#        self.stop=True
    def move(self):
#        print("我方坦克状态", self.stop)
        if not self.stop: # 如果坦克不是停止状态
 #======================================坦克位置是否在变化===============================================           
            self.oldleft=self.rect.left
            self.oldtop=self.rect.top
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
        super().__init__(screen,randint(1,5)*100,200)
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


                
    def random_fire(self):
        r=randint(0, 50)
#        if r>45:
        if r==10 :
            m= self.fire()
            TankMain.enemy_missile_list.add(m)
        else:
            return
           
         

class Missile(BaseItem):
    width = 36
    height = 36
    
    def __init__(self,screen, tank):
        super().__init__(screen)  
        self.tank=tank
        self.direction=tank.direction #炮弹方向由坦克决定
        self.speed=12 # 炮弹速度
        self.images={} #炮弹所有图片
        self.images["下"]=pygame.image.load("D:\scrapyProject\pic\子弹下.png") # load返回surface
        self.images["上"]=pygame.image.load("D:\scrapyProject\pic\子弹上.png")
        self.images["左"]=pygame.image.load("D:\scrapyProject\pic\子弹左.png")
        self.images["右"]=pygame.image.load("D:\scrapyProject\pic\子弹右.png")
        self.image=self.images[self.direction] # 坦克的图片由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=tank.rect.left + (tank.width-self.width)/2
        self.rect.top=tank.rect.top + (tank.height - self.height)/2
        self.live = True # 炮弹是否活着
        self.good = False
        
        
    def move(self):
        if self.live: # 如果炮弹活着
            if self.direction =="左":
                if self.rect.left>0: # 判断坦克是否已经到边界
                    self.rect.left-=self.speed
                else:
                    self.live= False
            elif self.direction == "右":
                if self.rect.right<TankMain.width:
                    self.rect.right+=self.speed
                else:
                    self.live= False
            elif self.direction == "上":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.live= False
            elif self.direction == "下":
                if self.rect.bottom<TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.live= False
    #炮弹击中坦克 第一种 我方的炮弹几种敌方坦克   敌方炮弹击中我方坦克
    def hit_tank(self):
        if self.good:# 如果炮弹是我方的
            hit_list=pygame.sprite.spritecollide(self, TankMain.enemy_list, False)
            for e in hit_list:
                e.live=False
                TankMain.enemy_list.remove(e) # 如果敌方坦克被击中,就删除敌方
                self.live=False
                explode=Explode(self.screen, e.rect) #产生一个爆炸对象
                TankMain.explode_list.append(explode)
            
            
            
            
        
    
    
# 爆炸类
class Explode(BaseItem):
    
    
    def __init__(self, screen, rect): 
        super().__init__(screen)
        self.live=True
        self.images=[pygame.image.load(r"D:\scrapyProject\pic\0.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\1.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\2.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\3.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\4.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\5.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\6.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\7.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\8.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\9.png"), \
                     pygame.image.load(r"D:\scrapyProject\pic\10.png")]
        self.step=0
        self.rect=rect # 爆炸的位置和发生爆炸时,炮弹碰到的坦克位置一样
        #在构建爆炸的时候把坦克的rect传递进来
        
    def display(self):
        if self.live:
            if self.step==len(self.images):
                self.live = False
            else:
                self.image=self.images[self.step]
                self.screen.blit(self.image, self.rect)
                self.step+=1
        else:
            pass # 删除该对象
        

class Wall(BaseItem):
    def __init__(self, screen, left, top, width, height):
        super().__init__(screen)
        self.rect=Rect(left, top, width, height)
        self.color=(255, 0, 0)
        
#        self.left=left
#        self.top=top
#        self.width=width
#        self.height=height
        
    def display(self):
        self.screen.fill(self.color, self.rect)
   
    def hit_other(self):
        if TankMain.my_tank:
            
            is_hit=pygame.sprite.collide_rect(self, TankMain.my_tank)
            if is_hit:
                TankMain.my_tank.stop=True
                TankMain.my_tank.stay()
        if len(TankMain.enemy_list)!=0:
            hit_list=pygame.sprite.spritecollide(self, TankMain.enemy_list, False)
            for e in hit_list:
                e.stop=True
                e.stay()


def main():
    game=TankMain()
    game.startGame()

def prn_obj(obj): 
  print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


if __name__ == '__main__':
    ENEMY_NUMBER=10 # 敌方坦克数量
    main()
    
