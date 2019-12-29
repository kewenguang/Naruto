'''
Created on 2019年12月28日

@author: kewenguang
'''
from kengine.character import Character
from kengine.core.windows import Windows

class Pig(Character):

    def update_left_padding_run(self, image_index):
        self.set_left_padding(self.get_left_padding() - 24)
        if self.character_sprites['pig_run'].get_left_padding() < Windows.WIDTH - 100:
            self.signal_to_scene = 'wendy run appear'
        if self.character_sprites['pig_run'].get_left_padding() < -200:
            print('remove pig')
            self.remove_current_sprite_from_sprite_group()
            self.signal_to_scene = 'pig disappear'

    def __init__(self, sprite_group):
        super().__init__()
        print('Pig init ...')
        self.name = 'pig'
        self.set_sprite_group(sprite_group)
        
        self.add_character_sprite_with_name('pig_run', './assert/pic/character/pig/run')
        self.add_sprite_to_sprite_group_by_name('pig_run')
        self.set_current_sprite('pig_run')
        self.character_sprites['pig_run'].set_frame_rate(10)
        
        self.character_sprites['pig_run'].append_update_function(self.update_left_padding_run)
        
        self.set_padding(Windows.WIDTH, Windows.HEIGHT - 120)
