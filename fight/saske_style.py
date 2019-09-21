'''
Created on 2019年9月16日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class SaskeStyle(Style):
    def hou_yang_end_update_handle(self):
        self.character["saske/后仰"].image_index = len(self.character["saske/后仰"].images) - 1
    
    def saske_status_to_qilai(self):
        self.change_to_status('站起来')
    
    def saske_status_to_idle(self):
        self.change_to_status('idle')
        
    def __init__(self):
        self.character = {}
        saske_image_url = ['saske/倒在地上', 'saske/挥刀',
                            'saske/挥两刀', 'saske/挥拳',
                            'saske/向上一脚', 'saske/idle',
                            'saske/run','saske/后仰', 'saske/站起来']
        for i in range(len(saske_image_url)):
            print('saske_image_url[i]:' + saske_image_url[i])
            self.add_sprite(saske_image_url[i], need_flip = True)
        self.character["saske/run"].append_update_function(self.update_run) 
        self.character["saske/倒在地上"].append_update_function(self.update_fall_down) 
        self.character["saske/倒在地上"].append_end_update_function(self.saske_status_to_qilai) 
        self.character["saske/站起来"].append_end_update_function(self.saske_status_to_idle)
        
        self.current_sprite = self.character["saske/idle"]
        self.status = 'idle'
        self.current_sprite.hidden = False
        self.current_sprite.set_left_padding(GameCommonData.WIDTH - 60)
        self.current_sprite.set_top_padding(200)
        
        self.character["saske/后仰"].append_end_update_function(self.hou_yang_end_update_handle)
        
        self.fall_down_interval = 0
    
    def change_to_status(self, cmd):
        if cmd == 'run':
            Style.change_to_status(self, 'saske/run')
            self.status = 'run'
        elif cmd == 'idle':
            Style.change_to_status(self, 'saske/idle')
            self.status = 'idle'
        elif cmd == '倒在地上':
            Style.change_to_status(self, 'saske/倒在地上')
            self.status = '倒在地上'
        elif cmd == '挥刀':
            Style.change_to_status(self, 'saske/挥刀')
            self.status = '挥刀'
        elif cmd == '挥两刀':
            Style.change_to_status(self, 'saske/挥两刀')
            self.status = '挥两刀'
        elif cmd == '挥拳':
            Style.change_to_status(self, 'saske/挥拳')
            self.status = '挥拳'
        elif cmd == '向上一脚':
            Style.change_to_status(self, 'saske/向上一脚')
            self.status = '向上一脚'
        elif cmd == '后仰':
            Style.change_to_status(self, 'saske/后仰')
            self.status = '后仰'
        elif cmd == '站起来':
            Style.change_to_status(self, 'saske/站起来')
            self.status = '站起来'
        
    def update(self):
        #可以在这里填充关于键盘的响应
        return
        
    def update_run(self, image_index):
        current_left_padding = self.character["saske/run"].get_left_padding()
        being_left_padding = current_left_padding - 7
        if being_left_padding > GameCommonData.LeftPadding:
            self.character["saske/run"].set_left_padding(being_left_padding)  
    
    
    def update_fall_down(self, image_index):
        images_num = self.character["saske/倒在地上"].get_image_num()
        current_left_padding = self.character["saske/倒在地上"].get_left_padding()
        current_top_padding = self.character["saske/倒在地上"].get_top_padding()
        being_left_padding = current_left_padding + 7
        being_top_padding = current_top_padding + (image_index*2 - images_num)*10
        self.character["saske/倒在地上"].set_left_padding(being_left_padding)  
        self.character["saske/倒在地上"].set_top_padding(being_top_padding)  