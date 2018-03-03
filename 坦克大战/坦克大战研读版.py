#目标 坦克大战
#语言python3.6
#日期:2018.03.02

#游戏中出现的对象
#屏幕    screen
#坦克    tank
#障碍物   wall
#炮弹    cannonball
#爆炸    bomb
#            print("*"*50)
import pygame
from pygame.locals import *
import sys
import time
from random import randint

class Game():
    enemy_list=pygame.sprite.Group()
    my_tank_cannonball_list=[]
    bomb_list=[]
    def start(self):
        print('游戏开始')
        ENEMY_NUMBER=30
        my_tank_left=400
        my_tank_top=300
        screen=Screen().create_screen()
        my_tank=MyTank(screen,my_tank_left, my_tank_top)
        for i in range(1, ENEMY_NUMBER):
            self.enemy_list.add(EnemyTank(screen))
        while True:
            screen.fill((0,0,0))
            #战斗信息
            for i , text in enumerate(self.write_text(), 0):
                screen.blit(text, (0, 5+(i*20)))
            self.get_event(my_tank)
            my_tank.display()
            my_tank.move()
#            =========================================================================
            for enemy in self.enemy_list:
                enemy.display()
                enemy.random_move()
            for c in self.my_tank_cannonball_list:
                if c.live:
                    c.display()
                    collide_tank_list=c.collide_tank(self.enemy_list)
                    # 我方炮弹和敌方坦克同归于尽,新生一个爆炸对象
                    for collide_tank in collide_tank_list:
                        collide_tank.live=False
                        self.enemy_list.remove(collide_tank)
                        c.live=False
                        bomb=Bomb(screen, c)
                        self.bomb_list.append(bomb)
                    c.move()
                else:
                    self.my_tank_cannonball_list.remove(c)
            
            for b in self.bomb_list:
                b.display()
            time.sleep(0.01)
            pygame.display.update()
    def write_text(self):
        pygame.font.init()
        font=pygame.font.SysFont('simsunnsimsun', 12)
        ememy_number=font.render('敌方坦克数量: %d'%len(self.enemy_list), True, (253, 198, 11))
        my_cannonball=font.render('我方加农炮数量: %d'%len(self.my_tank_cannonball_list), True, (253, 198, 11))
        return ememy_number, my_cannonball
    def stop(self):
        sys.exit()
        print("游戏结束")
        pass
    def get_event(self, tank):
        event_list=pygame.event.get()   
        for e in event_list:
            if e.type==QUIT:
                self.stop()
            if e.type==KEYDOWN:
                if e.key==K_LEFT:
                    tank.direction="左"
                    tank.stop=False
                if e.key==K_RIGHT:
                    tank.direction="右"
                    tank.stop=False
                if e.key==K_UP:
                    tank.direction="上"
                    tank.stop=False
                if e.key==K_DOWN:
                    tank.direction="下"
                    tank.stop=False
                if e.key==K_s:
                    tank.stop=True                 
                if e.key==K_ESCAPE:
                    self.stop()
                if e.key==K_SPACE:
                    for i in range(10):
                        c=tank.attack()
                        c.good=True
                        self.my_tank_cannonball_list.append(c)
                
            
                    

class Screen():
    def __init__(self):
        self.width=800
        self.height=600
        pygame.display.init()
        
    def create_screen(self):
        pygame.display.set_caption("坦克大战")
        game_screen=pygame.display.set_mode((self.width,self.height))
        return game_screen
        
class BaseObject(pygame.sprite.Sprite):    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
#        self.rect=self.image.get_rect()
    def display(self):
        if self.live:
            self.image=self.images[self.direction]
            self.screen.blit(self.image, self.rect)
        
class Tank(BaseObject):
    def __init__(self, screen, left, top):
        super().__init__(screen)
        self.stop=True
        self.speed=5
        self.direction="上"
        self.images={}
        self.images["上"]=pygame.image.load(r"D:\test\pic\坦克上.png")
        self.images["下"]=pygame.image.load(r"D:\test\pic\坦克下.png")
        self.images["左"]=pygame.image.load(r"D:\test\pic\坦克左.png")
        self.images["右"]=pygame.image.load(r"D:\test\pic\坦克右.png")
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.screen_width=screen.get_size()[0]
        self.screen_height=screen.get_size()[1]
        self.live=True
    def move(self):
        if not self.stop:
            if self.direction=="上":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top=0
            if self.direction=="下":
                if self.rect.bottom<self.screen_height:
                    self.rect.bottom+=self.speed
                else:
                    self.rect.bottom=self.screen_height
            if self.direction=="左":
                if self.rect.left>0:
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            if self.direction=="右":
                if self.rect.right<self.screen_width:
                    self.rect.right+=self.speed      
                else:
                    self.rect.right=self.screen_width
        
    def attack(self):
        c=Cannonball(self.screen, self)
        return c

    
class MyTank(Tank):
    def __init__(self, screen, left, top):
        super().__init__(screen, left, top)
        self.images={}
        self.images["上"]=pygame.image.load(r"D:\test\pic\我的坦克上.png")
        self.images["下"]=pygame.image.load(r"D:\test\pic\我的坦克下.png")
        self.images["左"]=pygame.image.load(r"D:\test\pic\我的坦克左.png")
        self.images["右"]=pygame.image.load(r"D:\test\pic\我的坦克右.png")
        self.image=self.images[self.direction]
        
        
    
class EnemyTank(Tank):
    
    def __init__(self, screen):
        super().__init__(screen, randint(1,6)*100,200)
        self.speed=4
        self.get_random_direction()
        self.stop=False
        self.step=30
        self.live=True
        
    def get_random_direction(self):
        r=randint(0, 4)
        if r==0:
            self.direction="上"
        if r==1:
            self.direction="下"
        if r==2:
            self.direction="左"
        if r==3:
            self.direction="右"
    def random_move(self):
        if self.live:
            if self.step==0:
                self.get_random_direction()
                self.step=30
            else:
                self.move()
                self.step-=1
        else:
            self=None
            
        
        
    
class Wall():
    pass
    
class Cannonball(BaseObject):
    def __init__(self, screen, tank):
        self.screen=screen
        self.speed=12
        self.direction=tank.direction
        self.images={}
        self.images["上"]=pygame.image.load(r"D:\test\pic\子弹上.png")
        self.images["下"]=pygame.image.load(r"D:\test\pic\子弹下.png")
        self.images["左"]=pygame.image.load(r"D:\test\pic\子弹左.png")
        self.images["右"]=pygame.image.load(r"D:\test\pic\子弹右.png")
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left=tank.rect.left
        self.rect.top=tank.rect.top
        self.screen_width=screen.get_size()[0]
        self.screen_height=screen.get_size()[1]
        self.live=True
        self.good=False
    def move(self):
        if self.live:
            if self.direction=="上":
                if self.rect.top>0:
                    self.rect.top-=self.speed
                else:
                    self.live=False
            if self.direction=="下":
                if self.rect.bottom<self.screen_height:
                    self.rect.bottom+=self.speed
                else:
                    self.live=False
            if self.direction=="左":
                if self.rect.left>0:
                    self.rect.left-=self.speed
                else:
                    self.live=False
            if self.direction=="右":
                if self.rect.right<self.screen_width:
                    self.rect.right+=self.speed      
                else:
                    self.live=False
        else:
            self=None
    
        
        
    def collide_tank(self, enemy):
        if self.good:
            collide_tank_list=pygame.sprite.spritecollide(self, enemy, False)
            return collide_tank_list

                
                
                
                
            
        
    
class Bomb(BaseObject):
    def __init__(self, screen, tank):
        super().__init__(screen)
        self.screen=screen
        self.tank=tank
        self.live=True
        self.images=[pygame.image.load(r"D:\test\pic\0.png"), \
                     pygame.image.load(r"D:\test\pic\1.png"), \
                     pygame.image.load(r"D:\test\pic\2.png"), \
                     pygame.image.load(r"D:\test\pic\3.png"), \
                     pygame.image.load(r"D:\test\pic\4.png"), \
                     pygame.image.load(r"D:\test\pic\5.png"), \
                     pygame.image.load(r"D:\test\pic\6.png"), \
                     pygame.image.load(r"D:\test\pic\7.png"), \
                     pygame.image.load(r"D:\test\pic\8.png"), \
                     pygame.image.load(r"D:\test\pic\9.png"), \
                     pygame.image.load(r"D:\test\pic\10.png")]
        self.step=0
        self.rect=tank.rect
    def display(self):
        if self.live:
            if self.step==len(self.images):
                self.live=False
                self=None
            else:
                self.image=self.images[self.step]
                self.screen.blit(self.image, self.tank.rect)
                self.step+=1
            
    

def main():
    game=Game()
    game.start()
if __name__=='__main__':
    main()
