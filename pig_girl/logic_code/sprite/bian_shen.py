'''
Created on 2019年12月21日

@author: kewenguang
'''
from kengine.character import Character

class BianShen(Character):
    
    def change_to_bian_shen(self):
        print('魔法棒转成变身')
        self.change_to_status('begin_girl')
    
    def change_to_next_scene(self):
        print('切换到封面场景')
        self.signal_to_scene = 'next scene'
    
    def __init__(self, sprite_group):
        print('BianShen init ...')
        Character.__init__(self)
        self.name = 'bian_shen'
        self.set_sprite_group(sprite_group)
        
        self.add_character_sprite_with_name('mo_fa_bang', './assert/pic/mo_fa_bang')
        self.add_character_sprite_with_name('begin_girl', './assert/pic/begin_girl')
        
        self.add_sprite_to_sprite_group_by_name('mo_fa_bang')
        self.set_current_sprite('mo_fa_bang')
        
        self.character_sprites['mo_fa_bang'].append_end_update_function(self.change_to_bian_shen)
        self.character_sprites['begin_girl'].append_end_update_function(self.change_to_next_scene)
        
        self.character_sprites['mo_fa_bang'].set_frame_rate(8)
        self.character_sprites['begin_girl'].set_frame_rate(14)
        
        self.set_padding(0,0)
        