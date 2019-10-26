'''
Created on 2019年10月25日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class PainStyle(Style):
    
    def __init__(self, sprite_group, situation_flag = 1):
        self.sprite_group = sprite_group
        self.character = {}
        if situation_flag == 1:
            pain_image_url = ['pain/idle', 'pain/出场', 'pain/地爆天星结印', 'pain/地爆天星举手', 'pain/六道散']
            for i in range(len(pain_image_url)):
                print('pain_image_url[i]:' + pain_image_url[i])
                self.add_sprite(pain_image_url[i], need_flip = True)
        elif situation_flag == 2:
            pain_image_url = ['pain/轮回眼打开']
            self.add_sprite(pain_image_url[0])
        elif situation_flag == 3:
            pain_image_url = ['pain/地爆天星的球', 'pain/地爆天星的爆炸']
            for i in range(len(pain_image_url)):
                print('pain_image_url[i]:' + pain_image_url[i])
                self.add_sprite(pain_image_url[i])
            #self.add_sprite(pain_image_url[0])
        elif situation_flag == 4:
            pain_image_url = ['pain/地爆天星的爆炸']
            self.add_sprite(pain_image_url[0])
        if situation_flag == 1:
            self.character["pain/idle"].set_frame_rate(17)
            self.character["pain/出场"].set_frame_rate(8)
            self.character["pain/地爆天星结印"].set_frame_rate(8)
            self.character["pain/六道散"].set_frame_rate(5)
            self.current_sprite = self.character["pain/idle"]
            self.sprite_group.add(self.character["pain/idle"])
            self.status = 'idle'
        elif situation_flag == 2:
            self.sprite_group.add(self.character["pain/轮回眼打开"])
            self.current_sprite = self.character["pain/轮回眼打开"]
            self.character["pain/轮回眼打开"].set_frame_rate(8)
        elif situation_flag == 3:
            self.sprite_group.add(self.character["pain/地爆天星的球"])
            self.current_sprite = self.character["pain/地爆天星的球"]
            self.character["pain/地爆天星的球"].set_frame_rate(4)
            self.character["pain/地爆天星的爆炸"].set_frame_rate(16)
            
        self.current_sprite.set_top_padding(GameCommonData.character_level)
        self.current_sprite.stop_flush = False
        
    def change_to_status(self, status):
        if status == '出场':
            Style.change_to_status(self, 'pain/出场')
            self.status = '出场'
        elif status == 'idle':
            Style.change_to_status(self, 'pain/idle')
            self.status = 'idle'
        elif status == '地爆天星结印':
            Style.change_to_status(self, 'pain/地爆天星结印')
            self.status = '地爆天星结印'
        elif status == '地爆天星举手':
            Style.change_to_status(self, 'pain/地爆天星举手')
            self.status = '地爆天星举手'
        elif status == '六道散':
            Style.change_to_status(self, 'pain/六道散')
            self.status = '六道散'
        elif status == '地爆天星旋转':
            Style.change_to_status(self, 'pain/地爆天星旋转')
            self.status = '地爆天星旋转'
        elif status == '地爆天星的爆炸':
            Style.change_to_status(self, 'pain/地爆天星的爆炸')
            self.status = '地爆天星的爆炸'