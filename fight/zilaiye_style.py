'''
Created on 2019年10月21日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class ZilaiyeStyle(Style):
    def __init__(self, sprite_group, situation_flag = 1):
        self.sprite_group = sprite_group
        self.character = {}
        if situation_flag == 1:
            zilaiye_image_url = ['zilaiye/idle', 'zilaiye/出现', 'zilaiye/捂嘴喷火',
                                  'zilaiye/下蹲通灵', 'zilaiye/被吸走']
            for i in range(len(zilaiye_image_url)):
                print('zilaiye_image_url[i]:' + zilaiye_image_url[i])
                self.add_sprite(zilaiye_image_url[i])
        elif situation_flag == 2:
            zilaiye_image_url = ['zilaiye/蛤蟆出现', 'zilaiye/蛤蟆喷火']
            for i in range(len(zilaiye_image_url)):
                print('zilaiye_image_url[i]:' + zilaiye_image_url[i])
                self.add_sprite(zilaiye_image_url[i])
        elif situation_flag == 3:
            zilaiye_image_url = ['zilaiye/火油']
            self.add_sprite(zilaiye_image_url[0])
        elif situation_flag == 4:
            zilaiye_image_url = ['zilaiye/长条火焰']
            self.add_sprite(zilaiye_image_url[0])
            
        if situation_flag == 1:
            self.character["zilaiye/idle"].set_frame_rate(16)
            self.character["zilaiye/出现"].set_frame_rate(8)
            self.character["zilaiye/捂嘴喷火"].set_frame_rate(1)
            self.character["zilaiye/下蹲通灵"].set_frame_rate(8)
            self.character["zilaiye/被吸走"].set_frame_rate(1)
            self.current_sprite = self.character["zilaiye/idle"]
            self.sprite_group.add(self.character["zilaiye/idle"])
            self.status = 'idle'
        elif situation_flag == 2:
            self.character["zilaiye/蛤蟆喷火"].set_frame_rate(8)
            self.sprite_group.add(self.character["zilaiye/蛤蟆出现"])
            self.current_sprite = self.character["zilaiye/蛤蟆出现"]
            self.character["zilaiye/蛤蟆出现"].set_frame_rate(5)
            self.status = '蛤蟆出现'
        elif situation_flag == 3:
            self.character["zilaiye/火油"].set_frame_rate(8)
            self.sprite_group.add(self.character["zilaiye/火油"])
            self.current_sprite = self.character["zilaiye/火油"]
            self.status = '火油'
        elif situation_flag == 4:
            self.character["zilaiye/长条火焰"].set_frame_rate(8)
            self.sprite_group.add(self.character["zilaiye/长条火焰"])
            self.current_sprite = self.character["zilaiye/长条火焰"]
            self.status = '长条火焰'
            
        self.current_sprite.set_top_padding(GameCommonData.character_level)
        self.current_sprite.stop_flush = False
        
    def change_to_status(self, status):
        if status == '出现':
            Style.change_to_status(self, 'zilaiye/出现')
            self.status = '出现'
        elif status == 'idle':
            Style.change_to_status(self, 'zilaiye/idle')
            self.status = 'idle'
        elif status == '捂嘴喷火':
            Style.change_to_status(self, 'zilaiye/捂嘴喷火')
            self.status = '捂嘴喷火'
        elif status == '下蹲通灵':
            Style.change_to_status(self, 'zilaiye/下蹲通灵')
            self.status = '下蹲通灵'
        elif status == '蛤蟆出现':
            Style.change_to_status(self, 'zilaiye/蛤蟆出现')
            self.status = '蛤蟆出现'
        elif status == '蛤蟆喷火':
            Style.change_to_status(self, 'zilaiye/蛤蟆喷火')
            self.status = '蛤蟆喷火'
        elif status == '被吸走':
            Style.change_to_status(self, 'zilaiye/被吸走')
            self.status = '被吸走'
            