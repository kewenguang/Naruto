'''
Created on 2019年9月16日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class SaskeStyle(Style):
    def __init__(self):
        self.character = {}
        saske_image_url = ['saske/倒在地上', 'saske/挥刀',
                            'saske/挥两刀', 'saske/挥拳',
                            'saske/向上一脚', 'saske/idle',
                            'saske/run']
        for i in range(len(saske_image_url)):
            print('saske_image_url[i]:' + saske_image_url[i])
            self.add_sprite(saske_image_url[i], need_flip = True)
        self.character["saske/run"].set_fuction(self.update_run) 
        self.current_sprite = self.character["saske/idle"]
        self.status = 'idle'
        self.current_sprite.hidden = False
        self.current_sprite.set_left_padding(GameCommonData.WIDTH - 60)
        self.current_sprite.set_top_padding(200)
    
    def change_status(self, cmd):
        if cmd == 'run':
            self.change_to_status('saske/run')
            self.status = 'run'
        elif cmd == 'idle':
            self.change_to_status('saske/idle')
            self.status = 'idle'
        elif cmd == '倒在地上':
            self.change_to_status('saske/倒在地上')
            self.status = '倒在地上'
        elif cmd == '挥刀':
            self.change_to_status('saske/挥刀')
            self.status = '挥刀'
        elif cmd == '挥两刀':
            self.change_to_status('saske/挥两刀')
            self.status = '挥两刀'
        elif cmd == '挥拳':
            self.change_to_status('saske/挥拳')
            self.status = '挥拳'
        elif cmd == '向上一脚':
            self.change_to_status('saske/向上一脚')
            self.status = '向上一脚'
            
    def update(self):
        #可以在这里填充关于键盘的响应
        return
        
    def update_run(self):
        current_left_padding = self.character["saske/run"].get_left_padding()
        being_left_padding = current_left_padding - 10
        if being_left_padding > GameCommonData.LeftPadding:
            self.character["saske/run"].set_left_padding(being_left_padding)  
        