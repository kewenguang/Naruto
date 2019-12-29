'''
Created on 2019年12月27日

@author: kewenguang
'''
from kengine.character import Character
from kengine.core.windows import Windows

class WendyHead(Character):
    
    def tou_xiang_update(self, image_index):
        #在这里上移猪猪女孩的头像
        if self.character_sprites['tou_xiang'].get_top_padding() > 30:
            self.set_top_padding(self.get_top_padding() - 14)
        else:
            self.signal_to_scene = 'pig appear'
            self.character_sprites['tou_xiang'].clear_update_function()
    
    #def pig_appear(self):
    #    self.signal_to_scene = 'pig appear'
    #    self.character_sprites['tou_xiang'].clear_end_update_function()
    
    def __init__(self, sprite_group, name = 'wendy_head'):
        super().__init__()
        print('WendyHead init ...')
        self.name = name
        self.set_sprite_group(sprite_group)
        
        self.add_character_sprite_with_name('tou_xiang', './assert/pic/character/wendy/tou_xiang/')
        self.add_sprite_to_sprite_group_by_name('tou_xiang')
        self.set_current_sprite('tou_xiang')
        self.character_sprites['tou_xiang'].set_frame_rate(22)
        
        self.character_sprites['tou_xiang'].append_update_function(self.tou_xiang_update)
        #self.character_sprites['tou_xiang'].append_end_update_function(self.pig_appear)
        
        self.set_padding(Windows.WIDTH/2 - self.character_sprites['tou_xiang'].get_image_width()/2, Windows.HEIGHT)  #头像宽度除以2
        
class Wendy(Character):
    
    def __init__(self, sprite_group):
        super().__init__()
        self.set_sprite_group(sprite_group)
        
    def add_wendy_run(self):
        self.add_character_sprite_with_name('run', './assert/pic/character/wendy/big_wendy_run/', need_flip = True)
        self.add_sprite_to_sprite_group_by_name('run')
        self.set_current_sprite('run')
        self.character_sprites['run'].set_frame_rate(10)
        self.set_padding(Windows.WIDTH, Windows.HEIGHT - 140)
        
    def add_wendy_run_out_of_windows_update(self):
        def run_out_of_windows(image_index):
            self.set_left_padding(self.get_left_padding() - 24)
            if self.get_left_padding() < -200:
                print('remove wendy')
                self.remove_current_sprite_from_sprite_group()
                self.signal_to_scene = 'wendy disappear'
        self.character_sprites['run'].append_update_function(run_out_of_windows)
    