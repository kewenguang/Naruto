'''
Created on 2019年10月18日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class KakaxiStyle(Style):
    
    def __init__(self, sprite_group, situation_flag = 1):
        self.sprite_group = sprite_group
        self.character = {}
        if situation_flag == 1:
            kakaxi_image_url = ['kakaxi/idle', 'kakaxi/站直', 'kakaxi/出现', 'kakaxi/捂眼']
            for i in range(len(kakaxi_image_url)):
                print('kakaxi_image_url[i]:' + kakaxi_image_url[i])
                self.add_sprite(kakaxi_image_url[i], need_flip = True)
        elif situation_flag == 2:
            kakaxi_image_url = ['kakaxi/神威']
            self.add_sprite(kakaxi_image_url[0])
        elif situation_flag == 3:
            kakaxi_image_url = ['kakaxi/手里剑']
            self.add_sprite(kakaxi_image_url[0])
        elif situation_flag == 4:
            kakaxi_image_url = ['kakaxi/水龙弹打中特效']
            self.add_sprite(kakaxi_image_url[0], need_flip = True)
        elif situation_flag == 5:
            kakaxi_image_url = ['kakaxi/水龙弹之术']
            self.add_sprite(kakaxi_image_url[0], need_flip = True)
            
        if situation_flag == 1:
            self.character["kakaxi/idle"].set_frame_rate(8)
            self.character["kakaxi/站直"].set_frame_rate(8)
            self.character["kakaxi/出现"].set_frame_rate(10)
            self.current_sprite = self.character["kakaxi/idle"]
            self.sprite_group.add(self.character["kakaxi/idle"])
            self.status = 'idle'
        elif situation_flag == 2:
            self.sprite_group.add(self.character["kakaxi/神威"])
            self.current_sprite = self.character["kakaxi/神威"]
            self.character["kakaxi/神威"].set_frame_rate(5)
        elif situation_flag == 3:
            self.sprite_group.add(self.character["kakaxi/手里剑"])
            self.current_sprite = self.character["kakaxi/手里剑"]
            self.character["kakaxi/手里剑"].set_frame_rate(10)
        elif situation_flag == 4:
            self.sprite_group.add(self.character["kakaxi/水龙弹打中特效"])
            self.current_sprite = self.character["kakaxi/水龙弹打中特效"]
            self.character["kakaxi/水龙弹打中特效"].set_frame_rate(5)
        elif situation_flag == 5:
            self.sprite_group.add(self.character["kakaxi/水龙弹之术"])
            self.current_sprite = self.character["kakaxi/水龙弹之术"]
            self.character["kakaxi/水龙弹之术"].set_frame_rate(20)
            
        self.current_sprite.set_top_padding(GameCommonData.character_level)
        self.current_sprite.stop_flush = False
        
    def revert_top_padding(self):
        self.current_sprite.set_top_padding(GameCommonData.character_level)
        
    def change_to_status(self, status):
        if status == '站直':
            Style.change_to_status(self, 'kakaxi/站直')
            self.status = '站直'
        elif status == 'idle':
            Style.change_to_status(self, 'kakaxi/idle')
            self.status = 'idle'
        elif status == '出现':
            Style.change_to_status(self, 'kakaxi/出现')
            self.status = '出现'
        elif status == '捂眼':
            Style.change_to_status(self, 'kakaxi/捂眼')
            self.status = '捂眼'