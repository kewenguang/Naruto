'''
Created on 2019年11月26日

@author: kewenguang
'''
#此类对CharacterSprite进行封装，包含多个CharacterSprite，每一个CharacterSprite代表一个状态，一个动作
from .character_sprite import CharacterSprite

class Character():

    def __init__(self):
        self.speed = 10
        
    def change_to_status(self, status_name):
        self.sprite_group.remove_internal(self.current_sprite)
        self.current_sprite.stop_flush = True
        self.character[status_name].set_left_padding(self.current_sprite.get_left_padding())
        self.character[status_name].set_top_padding(self.current_sprite.get_top_padding())
        self.current_sprite = self.character[status_name]
        self.character[status_name].stop_flush = False
        self.sprite_group.add(self.current_sprite)
    
    def set_current_sprite_stop_flush(self):
        self.current_sprite.stop_flush = True
    
    def set_current_sprite_start_flush(self):
        self.current_sprite.stop_flush = False
        
    def get_left_padding(self):
        return self.current_sprite.get_left_padding()
    
    def get_top_padding(self):
        return self.current_sprite.get_top_padding()
    
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group

    #外面需要设置的
    def add_current_sprite_to_sprite_group(self):
        self.sprite_group.add(self.current_sprite)
        
    def remove_from_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        self.sprite_group.remove_internal(self.current_sprite)
        
    def remove_current_sprite_from_sprite_group(self):
        self.sprite_group.remove_internal(self.current_sprite)
    
    def set_left_padding(self, left_padding):
        self.current_sprite.set_left_padding(left_padding)
    
    def set_top_padding(self, top_padding):
        self.current_sprite.set_top_padding(top_padding)
        
    #为某一个人物添加一个状态的图集，一人物通常有很多的状态，每一个状态对应一个图集
    def add_character_sprite(self, image_url, need_flip = False):
        character_sprite = CharacterSprite()
        character_sprite.set_images(image_url, need_flip)
        self.character[image_url] = character_sprite
        return character_sprite