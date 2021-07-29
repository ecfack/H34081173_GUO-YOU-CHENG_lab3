import pygame
import math
import os
from settings import PATH,R_PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

GREEN=(0,255,0)
RED=(255,0,0)


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 1
        self.move_count = 0
        self.stride = 4
        self.x, self.y = self.path[0]


    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        #建一個surface做hp_bar
        hp_bar=pygame.Surface((50,5))

        #計算目前血量比率並且渲染綠方塊和紅方塊到hp_bar這surface上
        hp_ratio=self.health/self.max_health
        hp_bar_green_area=[0,0,int(hp_ratio*hp_bar.get_width()),hp_bar.get_height()]
        pygame.draw.rect(hp_bar,GREEN,hp_bar_green_area)

        hp_bar_red_area=[int(hp_ratio*hp_bar.get_width()),0,(1-int(hp_ratio))*hp_bar.get_width(),hp_bar.get_height()]
        pygame.draw.rect(hp_bar,RED,hp_bar_red_area)

        #再把hp_bar渲染到win上
        win.blit(hp_bar,(self.x - self.width // 2,self.y - self.height // 2-hp_bar.get_height()))
        # ...(to be done)
        pass

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        #如果未過終點
        if self.path_pos<len(self.path) :
            #算目前最近的兩點(A,B)間的距離和所需最大步數
            distance_A_B=(self.path[self.path_pos][0]-self.path[self.path_pos-1][0],self.path[self.path_pos][1]-self.path[self.path_pos-1][1])
            len_A_B=math.sqrt(distance_A_B[0]**2+distance_A_B[1]**2)
            max_count = math.ceil(len_A_B / self.stride)

            #還沒過B點
            if self.move_count < max_count :
                self.x+=self.stride*(distance_A_B[0]/len_A_B)
                self.y+=self.stride*(distance_A_B[1]/len_A_B)
                self.move_count+=1
            else:
                self.path_pos+=1
                self.move_count=0
        # ...(to be done)
        pass


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = [Enemy()]  # don't change this line until you do the EX.3 
        
        self.is_from_left=True  #用來給generate()判定要從哪出兵

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """
        self.gen_count+=1
        if self.gen_count>=self.gen_period:
            self.gen_count=0    #計時器歸0
            if len(self.reserved_members):
                self.expedition.append(self.reserved_members.pop())
        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)

        pass

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        for i in range(0,num):
            new_enemy=Enemy()
            #改動instance的預設值
            new_enemy.path=PATH if self.is_from_left else R_PATH
            new_enemy.x, new_enemy.y=new_enemy.path[0]

            self.reserved_members.append(new_enemy)
        self.is_from_left=not(self.is_from_left)    #換邊出兵
        # ...(to be done)
        pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





