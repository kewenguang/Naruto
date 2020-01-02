'''
Created on 2019年12月10日

@author: kewenguang
'''
import pygame

from scene import Scene
from sprite.wendy import WendyHead
from sprite.wendy import Wendy
from sprite.pig import Pig
from kengine.core.windows import Windows

class FengmianScene(Scene):
    
    #接下来需要搞的是这个场景
    #上背景图片，一个女孩的头像自底向上出现，然后是放“我有一支仙女棒，变大变小变漂亮”
    
    #喊声音的同时，也会有一只小猪从一边跑到另一边，然后发出鼻子的叫声”吭 吭“
    #接下来要做的是创建一个窗体，然后可以拖动图集进入窗体，可以对图片进行放大缩小
    #选中图片的话，右下角会显示图片两个端点针对当前窗体左上角的坐标
    #还要可以拖文字，并显示文字坐标
    #
    
    
    def __init__(self):
        super().__init__()
        self.play_nick()
        self.name = "封面"
        self.background = pygame.image.load(r"./assert/pic/城堡背景.jpg")
        
        self.wendy_head_character = WendyHead(self.sprite_group, "tou_xiang")
        self.character_manager.add_character(self.wendy_head_character)
        
        self.loop = self.start
        
    
    def update_background(self):
        self.screen.blit(self.background, (0,0))
        
    #播放妖尾的波波的小白音乐
    def play_nick(self):
        self.mixer.music.load('./assert/voice/bgm/尼克.wav')
        self.mixer.music.play(1, 0)
    
    def logic_clear_character_in_manager(self):
        if self.pig_character.signal_to_scene == 'pig disappear':
            self.pig_character.clear_signal_to_scene()
            self.character_manager.remove_character(self.pig_character)
        if self.wendy_character.signal_to_scene == 'wendy disappear':
            self.wendy_character.clear_signal_to_scene()
            self.character_manager.remove_character(self.wendy_character)
            
            #窗体中间出现“猪猪女孩”的字样
            self.add_text_at_center(font = '华文琥珀',
                           text = '猪猪女孩', 
                           color = (255,192,203), 
                           center = (Windows.WIDTH/2 , 230),
                           size = 70)
            
    def logic_wait_for_pig(self):
        if self.wendy_head_character.signal_to_scene == 'pig appear':
            self.pig_character = Pig(self.sprite_group)
            self.character_manager.add_character(self.pig_character)
            self.logic_update = self.logic_wait_for_wendy_run
            print('小猪出现。。。')
    
    def logic_wait_for_wendy_run(self):
        if self.pig_character.signal_to_scene == 'wendy run appear':
            self.wendy_character = Wendy(self.sprite_group)
            self.character_manager.add_character(self.wendy_character)
            
            self.wendy_character.add_wendy_run()
            #self.wendy_character.set_current_sprite('run')
            self.wendy_character.add_wendy_run_out_of_windows_update()
            
            self.logic_update = self.logic_clear_character_in_manager
        
            #self.wendy_run = Wendy(self.)
    
    def start(self):
        print('游戏封面 loop为start()')
        super().start()
        self.update_background()
        self.loop = self.update
        self.clear_character_signal()
        self.logic_update = self.logic_wait_for_pig
        
    def update(self):
        self.update_background()#先刷背景再刷人物
        self.update_text()
        #所有的图片刷新都要在super().update()之上，因为只有这样才能不闪烁
        #原因是这里的系统是先把一张图片瞄好了，然后整体飙到屏幕上的
        super().update()
        self.logic_update()
        
        self.clear_character_signal()
        
    #先让它跑起来显示一个窗体先