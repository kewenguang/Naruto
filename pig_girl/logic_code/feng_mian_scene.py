'''
Created on 2019年12月10日

@author: kewenguang
'''
import pygame

from scene import Scene

class FengmianScene(Scene):
    
    #接下来需要搞的是这个场景
    #上背景图片，一个女孩的头像自底向上出现，然后是放“我有一支仙女棒，变大变小变漂亮”
    #喊声音的同时，也会有一只小猪从一边跑到另一边，然后发出鼻子的叫声”吭 吭“
    
    #接下来想一想怎么基于框架的层面添加背景，刷背景
    
    def __init__(self):
        self.name = "封面"
        self.background = pygame.image.load(r"./assert/pic/城堡背景.jpg")
        self.signal_to_upper = ''
        self.next_scene_name = ''
        
        self.loop = self.start
    
    def update_background(self):
        self.screen.blit(self.background, (0,0))
    
    def start(self):
        print('游戏封面 loop为start()')
        self.loop = self.update
        
    def update(self):
        print('游戏封面loop为update()')
        self.update_background() #这个在超类里面有一个刷白背景的
        
    #先让它跑起来显示一个窗体先