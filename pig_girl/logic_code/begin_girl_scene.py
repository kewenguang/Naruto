'''
Created on 2019年12月21日

@author: kewenguang
'''
import pygame

from scene import Scene
from sprite.bian_shen import BianShen

class BeginGirlScene(Scene):
    
    def __init__(self):
        self.name = "少女变身"
        #self.background = pygame.image.load(r"./assert/pic/城堡背景.jpg")
        self.sprite_group = pygame.sprite.Group()
        self.bian_shen_character = BianShen(self.sprite_group)
        self.signal_to_upper = ''
        self.next_scene_name = '封面'
        
        self.loop = self.start
    #此场景中没有所谓的背景，所以就不刷了
    #def update_background(self):
    #    self.screen.blit(self.background, (0,0))
    
    def start(self):
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)  #scene_manager会赋予self.screen属性
        pygame.display.flip()
        
        if self.bian_shen_character.signal_to_upper == 'next scene':
            self.signal_to_upper = 'next scene'
        #执行完了之后直接切换到下一个场景
        #self.loop = self.update
        
    #def update(self):
        #self.update_background()
        
        