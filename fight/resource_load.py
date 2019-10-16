'''
Created on 2019年8月28日

@author: kewenguang
'''
import os
from os import path
import pygame
import functools
import time

img_dir = path.join(path.dirname(__file__), '../assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

class Color():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

class Style():
    
    def change_to_status_common(self,status_name):
        self.sprite_group.remove_internal(self.current_sprite)
        self.current_sprite.hidden = True
        self.character[status_name].set_left_padding(self.current_sprite.get_left_padding())
        self.character[status_name].set_top_padding(self.current_sprite.get_top_padding())
        self.current_sprite = self.character[status_name]
        self.character[status_name].hidden = False
        
    def change_to_status(self, status_name):
        self.change_to_status_common(status_name)
        self.sprite_group.add(self.current_sprite)
    
    def change_to_status_with_no_remove_origin(self, status_name):
        self.current_sprite.hidden = True
        self.character[status_name].set_left_padding(self.current_sprite.get_left_padding())
        self.character[status_name].set_top_padding(self.current_sprite.get_top_padding())
        self.current_sprite.set_top_padding(1000)
        self.current_sprite = self.character[status_name]
        self.character[status_name].hidden = False
        self.sprite_group.add(self.current_sprite)
    
    def change_to_status_just_show(self, status_name): #已经添加到sprite_group中，只是改变现实状态
        self.current_sprite.hidden = True
        self.character[status_name].set_left_padding(self.current_sprite.get_left_padding())
        self.character[status_name].set_top_padding(self.current_sprite.get_top_padding())
        #self.sprite_group.remove_internal(self.current_sprite)
        self.current_sprite.set_top_padding(1000)
        self.current_sprite = self.character[status_name]
        self.current_sprite.hidden = False
    
    def set_current_sprite_hide(self):
        self.current_sprite.hidden = True
    
    def set_current_sprite_show(self):
        self.current_sprite.hidden = False
        
    def get_left_padding(self):
        return self.current_sprite.get_left_padding()
    
    def get_top_padding(self):
        return self.current_sprite.get_top_padding()
    
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group

    #外面需要设置的
    def add_to_sprite_group(self):
        self.sprite_group.add(self.current_sprite)
        
    def remove_from_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        self.sprite_group.remove_internal(self.current_sprite)
        
    def remove_current_sprite_from_sprite_group(self):
        self.sprite_group.remove_internal(self.current_sprite)
    #外面需要设置的
    def set_key_controller(self, key_controller):
        self.key_controller = key_controller
        
    def add_sprite(self, image_url, need_flip = False):
        character_sprite = CharacterSprite()
        character_sprite.set_images(image_url, need_flip)
        self.character[image_url] = character_sprite
        return character_sprite
    
class GameCommonData():
    #窗体的宽高
    WIDTH = 1500
    HEIGHT = 600
    
    character_level = HEIGHT - 200
    
    #游戏人物可移动的左右边界情况
    LeftPadding = 200
    RightPadding = 1000
    
    clock = pygame.time.Clock()
    tick = pygame.time.get_ticks()
    
    @staticmethod
    def pygame():
        return pygame
        
    @staticmethod
    def tick(FPS):
        GameCommonData.clock.tick(FPS)
    
    @staticmethod
    def SetWidth(width):
        GameCommonData.WIDTH = width
        
    @staticmethod
    def SetHeight(height):
        GameCommonData.HEIGHT = height
    
        
    
class KeyController():
    def init(self):
        self.key_w = False
        self.key_a = False
        self.key_s = False
        self.key_d = False
        self.key_u = False
        self.key_i = False
        self.key_o = False
        self.key_j = False
        self.key_k = False
        self.key_l = False
        self.key_m = False
        
    def key_response(self, key_down):
        if key_down == pygame.K_w:
            self.key_w = True
        if key_down == pygame.K_a:
            self.key_a = True
        if key_down == pygame.K_s:
            self.key_s = True
        if key_down == pygame.K_d:
            self.key_d = True
        if key_down == pygame.K_u:
            self.key_u = True
        if key_down == pygame.K_i:
            self.key_i = True
        if key_down == pygame.K_o:
            self.key_o = True
        if key_down == pygame.K_j:
            self.key_j = True
        if key_down == pygame.K_k:
            self.key_k = True
        if key_down == pygame.K_l:
            self.key_l = True
        if key_down == pygame.K_m:
            self.key_m = True
            
    def key_revert(self):
        self.key_w = False
        self.key_a = False
        self.key_s = False
        self.key_d = False
        self.key_u = False
        self.key_i = False
        self.key_o = False
        self.key_j = False
        self.key_k = False
        self.key_l = False
        self.key_m = False
        
key_controller = KeyController()
key_controller.init()

def compare_str(str_one, str_two):
    one = int(str_one.split('.')[0])
    two = int(str_two.split('.')[0])
    return one - two

def image_load(image_dir_str):
    multi_shadow_separation_images = []
    complete_img_dir = path.join(img_dir, image_dir_str)
    file_list = os.listdir(complete_img_dir) #列出文件夹下所有的目录与文件
    file_list.sort(key=functools.cmp_to_key(compare_str))
    for i in range(0,len(file_list)):
        file_path = os.path.join(complete_img_dir,file_list[i])
        multi_shadow_separation_images.append(pygame.image.load(file_path).convert())
    return multi_shadow_separation_images
    #for i in range(1,74):
    #    multi_shadow_separation_images.append(pygame.image.load(path.join(img_dir, image_dir_str, str(i) + '.png')).convert())

class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.multi_shadow_separation_images = image_load("naruto/multi_shadow_separation")
        #for i in range(1,74):
        #    multi_shadow_separation_images.append(pygame.image.load(path.join(img_dir, 'naruto_multi_shadow_separation', str(i) + '.png')).convert())
    
        #self.image = self.multi_shadow_separation_images[0] #pygame.transform.scale(multi_shadow_separation_images[0], (50, 38))
        
        self.radius = 20
        self.hidden = True
        self.hide_timer = GameCommonData.tick#pygame.time.get_ticks()
        self.image_index = 0
        self.flush_interval = 17
        self.flush_time = int(round(time.time() * 1000))
        
        self.start_update_function = []
        self.update_function = []
        self.end_update_function = []
        
        self.iter = 1
        self.bounce = False

        
    def set_images(self, images_url, need_flip = False):
        self.images = image_load(images_url)
        
        self.need_flip = need_flip
        if need_flip :#如果玩家站在右边，他的图片要翻转
            for i in range(len(self.images)):
                self.images[i] = pygame.transform.flip(self.images[i],True,False)
        
        self.image = self.images[0]
        for i in range(len(self.images)):
            transColor = self.images[i].get_at((0,0)) 
            self.images[i].set_colorkey(transColor)
            #self.image.set_colorkey(Color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = GameCommonData.WIDTH / 2
        self.rect.bottom = GameCommonData.HEIGHT - 10
 
    #如果这个列表中要移除元素，需要改存储方式，把存储方式改为map，然后自己造一个id生成器，id->func，移除根据id来
    def append_start_update_function(self, func):
        self.start_update_function.append(func)
        return len(self.start_update_function) - 1
 
    def append_update_function(self, func):
        self.update_function.append(func)
        return len(self.update_function) - 1
    
    def append_end_update_function(self, func):
        self.end_update_function.append(func)
        return len(self.end_update_function) - 1

    def clear_update_function(self):
        self.update_function.clear()

    def clear_end_update_function(self):
        self.end_update_function.clear()

    def clear_end_update_function_by_index(self, index):
        self.end_update_function.pop(index)

    def set_left_padding(self, left_padding):
        self.rect.centerx = left_padding
        
    def get_left_padding(self):
        return self.rect.centerx
        
    def set_top_padding(self, top_padding):
        self.rect.bottom = top_padding
        
    def get_top_padding(self):
        return self.rect.bottom
    
    def set_frame_rate(self, frame_rate):
        self.flush_interval = int(round(1000/frame_rate))
    
    def get_image_num(self):
        return len(self.images)
    
    def fixed_flush(self):
        current_time = int(round(time.time() * 1000))
        #print('current_time:' + str(current_time))
        #print('self.flush_time:' + str(self.flush_time))
        #print('self.flush_interval:' + str(self.flush_interval))
        if current_time - self.flush_time >= self.flush_interval:
            self.flush_time = current_time
            return True
        else:
            return False
    
    def set_image_update_bounce(self, bounce):
        self.bounce = bounce
    
    def set_iter(self, ints):
        self.iter = ints
    
    def update(self):
        if self.hidden:
            return
        if not self.fixed_flush():
            return
        if self.image_index == 0 :
            for func in self.start_update_function:
                func()
        
        self.image = self.images[self.image_index]
        
        self.image_index = self.image_index + self.iter
        if self.image_index == len(self.images) and not self.hidden:
            if self.bounce:
                self.iter = -1
                self.image_index = len(self.images) - 1
            else: 
                self.image_index = 0
                for func in self.end_update_function:
                    func()
        if self.image_index == 0 and not self.hidden and self.bounce:
            self.iter = 1
            for func in self.end_update_function:
                    func()
        
        for func in self.update_function:
                func(image_index = self.image_index)
