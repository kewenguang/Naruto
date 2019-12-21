'''
Created on 2019年11月26日

@author: kewenguang
'''
import pygame
import time
import os
import functools

#img_dir = os.path.join(os.path.dirname(__file__), '../assets')

def image_load(image_dir_str):
        images = []
        #complete_img_dir = os.path.join(img_dir, image_dir_str)
        file_list = os.listdir(image_dir_str) #列出文件夹下所有的目录与文件
        file_list.sort(key=functools.cmp_to_key(compare_str))
        for i in range(0,len(file_list)):
            file_path = os.path.join(image_dir_str, file_list[i])
            images.append(pygame.image.load(file_path).convert())
        return images
    
def compare_str(str_one, str_two):
    one = int(str_one.split('.')[0])
    two = int(str_two.split('.')[0])
    return one - two
    
class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
            
        self.stop_flush = False
        self.image_index = 0
        self.flush_interval = 30
        self.flush_time = int(round(time.time() * 1000))
        
        self.start_update_function = []
        self.update_function = []
        self.end_update_function = []
    
    def set_images(self, images_url, need_flip = False):
        self.images = image_load(images_url)
        
        self.need_flip = need_flip
        if need_flip :#如果玩家站在右边，他的图片要翻转
            for i in range(len(self.images)):
                self.images[i] = pygame.transform.flip(self.images[i],True,False)
        
        self.image = self.images[0]
        self.image_width, self.image_height = self.image.get_size()
        for i in range(len(self.images)):
            transColor = self.images[i].get_at((0,0)) 
            self.images[i].set_colorkey(transColor)
        self.rect = self.image.get_rect()
 
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

    def clear_start_function(self):
        self.start_update_function.clear()

    def clear_update_function(self):
        self.update_function.clear()

    def clear_end_update_function(self):
        self.end_update_function.clear()

    def clear_start_function_by_index(self, index):
        self.start_update_function.pop(index)

    def clear_update_function_by_index(self, index):
        self.update_function.pop(index)

    def clear_end_update_function_by_index(self, index):
        self.end_update_function.pop(index)

    def set_left_padding(self, left_padding):
        self.rect.centerx = left_padding + int(self.image_width/2)
        
    def get_left_padding(self):
        return self.rect.centerx - int(self.image_width/2)
        
    def set_top_padding(self, top_padding):
        self.rect.bottom = top_padding + self.image_height
        
    def get_top_padding(self):
        return self.rect.bottom - self.image_height
    
    def set_right_padding(self, right_padding):
        self.rect.centerx = right_padding - int(self.image_width/2)
    
    def get_right_padding(self):
        return self.rect.centerx + int(self.image_width/2)
    
    def set_bottom_padding(self, bottom_padding):
        self.rect.bottom = bottom_padding
        
    def get_bottom_padding(self):
        return self.rect.bottom
    
    def set_frame_rate(self, frame_rate):
        self.flush_interval = int(round(1000/frame_rate))
    
    def get_image_num(self):
        return len(self.images)
    
    def fixed_flush(self):
        current_time = int(round(time.time() * 1000))
        if current_time - self.flush_time >= self.flush_interval:
            self.flush_time = current_time
            return True
        else:
            return False
    
    def update(self):
        if self.stop_flush:
            return
        if not self.fixed_flush():
            return
        
        if self.image_index == 0 :
            for func in self.start_update_function:
                func()
        
        self.image = self.images[self.image_index]
        self.image_index = self.image_index + 1
        if self.image_index == len(self.images):
            self.image_index = 0
            for func in self.end_update_function:
                func()
        
        for func in self.update_function:
            func(image_index = self.image_index)
