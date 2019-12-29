'''
Created on 2019年12月21日

@author: kewenguang
'''
import pygame

from scene import Scene
from sprite.bian_shen import BianShen

class BeginGirlScene(Scene):
    
    def __init__(self):
        super().__init__()
        self.name = "少女变身"
        #self.background = pygame.image.load(r"./assert/pic/城堡背景.jpg")
        
        self.character_manager.add_character(BianShen(self.sprite_group))
        self.next_scene_name = '封面'
        self.loop = self.start
    #此场景中没有所谓的背景，所以就不刷了
    #def update_background(self):
    #    self.screen.blit(self.background, (0,0))
    
    def start(self):
        super().start()
        if self.bian_shen_character.signal_to_scene == 'next scene':
            self.signal_to_upper = 'next scene'
        self.clear_character_signal()
        #执行完了之后直接切换到下一个场景
        #self.loop = self.update
        
    #def update(self):
        #self.update_background()
        
        