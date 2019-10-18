'''
Created on 2019年10月17日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class WoailuoStyle(Style):
    
    def __init__(self, sprite_group, situation_flag = 1):
        self.sprite_group = sprite_group
        self.character = {}
        if situation_flag == 1:
            woailuo_image_url = ['woailuo/出现', 'woailuo/倒地', 'woailuo/蹲下', 
                                 'woailuo/后仰', 'woailuo/举手握拳', 'woailuo/idle']
            for i in range(len(woailuo_image_url)):
                print('saske_image_url[i]:' + woailuo_image_url[i])
                self.add_sprite(woailuo_image_url[i])
        elif situation_flag == 2:
            woailuo_image_url = ['woailuo/沙瀑送葬']
            self.add_sprite(woailuo_image_url[0], need_flip = True)
        elif situation_flag == 3:
            woailuo_image_url = ['woailuo/砂缚柩']
            self.add_sprite(woailuo_image_url[0])
            
        #for i in range(len(woailuo_image_url)):
        #    print('saske_image_url[i]:' + woailuo_image_url[i])
        #    self.add_sprite(woailuo_image_url[i], need_flip = True)
            
        if situation_flag == 1:
            self.character["woailuo/出现"].set_frame_rate(8)
            
            self.character["woailuo/倒地"].set_frame_rate(8)
            
            self.character["woailuo/蹲下"].set_frame_rate(15)
            
            self.character["woailuo/后仰"].set_frame_rate(8)
            
            self.character["woailuo/举手握拳"].set_frame_rate(8)
            
            self.character["woailuo/idle"].set_frame_rate(8)
            
            self.current_sprite = self.character["woailuo/idle"]
            self.sprite_group.add(self.character["woailuo/idle"])
            
            self.status = 'idle'
            #self.current_sprite.set_left_padding(60)
        elif situation_flag == 2:
            self.sprite_group.add(self.character["woailuo/沙瀑送葬"])
            self.current_sprite = self.character["woailuo/沙瀑送葬"]
            self.character["woailuo/沙瀑送葬"].set_frame_rate(5)
        elif situation_flag == 3:
            self.sprite_group.add(self.character["woailuo/砂缚柩"])
            self.current_sprite = self.character["woailuo/砂缚柩"]
            self.character["woailuo/砂缚柩"].set_frame_rate(8)
            
        self.current_sprite.set_top_padding(GameCommonData.character_level)
        self.current_sprite.stop_flush = False
        
    def change_to_status(self, status):
        if status == '出现':
            Style.change_to_status(self, 'woailuo/出现')
            self.status = '出现'
        elif status == '倒地':
            Style.change_to_status(self, 'woailuo/倒地')
            self.status = '倒地'
        elif status == '蹲下':
            Style.change_to_status(self, 'woailuo/蹲下')
            self.status = '蹲下'
        elif status == '后仰':
            Style.change_to_status(self, 'woailuo/后仰')
            self.status = '后仰'
        elif status == '举手握拳':
            Style.change_to_status(self, 'woailuo/举手握拳')
            self.status = '举手握拳'
        elif status == 'idle':
            Style.change_to_status(self, 'woailuo/idle')
            self.status = 'idle'
        elif status == 'run':
            Style.change_to_status(self, 'woailuo/run')
            self.status = 'run'