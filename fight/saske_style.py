'''
Created on 2019年9月16日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class SaskeStyle(Style):
    def hou_yang_end_update_handle(self):
        self.only_change_to_idle()
    
    def saske_status_to_qilai(self):
        self.change_to_status('站起来')
    
    def saske_status_to_idle(self):
        self.change_to_status('idle')
    
    def saske_status_to_huiquan(self):
        self.change_to_status('挥拳')
        
    def saske_status_to_huiliangdao(self):
        self.change_to_status('挥两刀')
    
    def saske_status_to_up_ti(self):
        self.change_to_status('向上一脚')
        
    def tiao_hui_qu(self, image_index):
        images_num = self.character["saske/完整跳"].get_image_num()
        current_left_padding = self.character["saske/完整跳"].get_left_padding()
        current_top_padding = self.character["saske/完整跳"].get_top_padding()
        being_left_padding = current_left_padding + 35
        being_top_padding = current_top_padding + (image_index*2 - images_num)*4
        self.character["saske/完整跳"].set_left_padding(being_left_padding)  
        self.character["saske/完整跳"].set_top_padding(being_top_padding)  
        
    def __init__(self, sprite_group, situation_flag = 1):
        self.sprite_group = sprite_group
        self.character = {}
        if situation_flag == 1:
            saske_image_url = ['saske/倒在地上', 'saske/挥刀',
                                'saske/挥两刀', 'saske/挥拳',
                                'saske/向上一脚', 'saske/idle',
                                'saske/run','saske/后仰', 'saske/站起来',
                                'saske/开篇挥手', 'saske/完整跳']
        elif situation_flag == 2:
            saske_image_url = ['saske/须左']
        elif situation_flag == 3:
            saske_image_url = ['saske/须左的箭']
        elif situation_flag == 4:
            saske_image_url = ['saske/写轮眼']
        for i in range(len(saske_image_url)):
            print('saske_image_url[i]:' + saske_image_url[i])
            self.add_sprite(saske_image_url[i], need_flip = True)
            
        if situation_flag == 1:
            self.character["saske/run"].append_update_function(self.update_run) 
            self.character["saske/倒在地上"].append_update_function(self.update_fall_down) 
            self.character["saske/倒在地上"].append_end_update_function(self.saske_status_to_qilai) 
            self.character["saske/倒在地上"].set_frame_rate(8)
            
            self.character["saske/站起来"].append_end_update_function(self.saske_status_to_idle)
            self.character["saske/站起来"].set_frame_rate(8)
            
            self.character["saske/完整跳"].append_end_update_function(self.saske_status_to_idle)
            self.character["saske/完整跳"].append_update_function(self.tiao_hui_qu)
            self.character["saske/完整跳"].set_frame_rate(8)
            
            self.character["saske/挥刀"].append_end_update_function(self.saske_status_to_huiquan)
            self.character["saske/挥刀"].set_frame_rate(8)
            self.character["saske/挥拳"].append_end_update_function(self.saske_status_to_huiliangdao)
            self.character["saske/挥拳"].set_frame_rate(8)
            self.character["saske/挥两刀"].append_end_update_function(self.saske_status_to_up_ti)
            self.character["saske/挥两刀"].set_frame_rate(8)
            self.character["saske/向上一脚"].append_end_update_function(self.saske_status_to_idle)
            self.character["saske/向上一脚"].set_frame_rate(8)
        
            #这个后仰的是一直存在于sprite_group里面的，所以以后你要切换人物，一定要把后仰删掉，而不是单单删除current_sprite
            self.character["saske/后仰"].set_image_update_bounce(False)
            self.sprite_group.add(self.character["saske/后仰"])   #self.character["saske/后仰"].stop_flush = False  如果这个后仰设置为True则会一直卡在第一张图片
            self.character["saske/后仰"].set_top_padding(1000)
            self.character["saske/后仰"].append_end_update_function(self.hou_yang_end_update_handle)
            self.character["saske/后仰"].set_frame_rate(8)
        
           
        
            #self.sprite_group.add(self.character["saske/idle"])
            self.current_sprite = self.character["saske/idle"]
            self.status = 'idle'
        
            self.start_left_padding = GameCommonData.WIDTH - 160
            self.current_sprite.set_left_padding(self.start_left_padding)
            self.current_sprite.set_top_padding(GameCommonData.character_level)
            self.character["saske/开篇挥手"].set_frame_rate(8)
        elif situation_flag == 2:
            self.sprite_group.add(self.character["saske/须左"])
            self.current_sprite = self.character["saske/须左"]
            self.character["saske/须左"].set_frame_rate(5)
        elif situation_flag == 3:
            self.sprite_group.add(self.character["saske/须左的箭"])
            self.current_sprite = self.character["saske/须左的箭"]
            self.character["saske/须左的箭"].set_frame_rate(8)
        elif situation_flag == 4:
            self.sprite_group.add(self.character["saske/写轮眼"])
            self.current_sprite = self.character["saske/写轮眼"]
            self.character["saske/写轮眼"].set_frame_rate(8)
            
        self.current_sprite.stop_flush = False
        self.fall_down_interval = 0
    
    def only_change_to_hou_yang(self):
        Style.change_to_status(self, 'saske/后仰')
        self.status = '后仰'
        
    def only_change_to_idle(self):
        Style.change_to_status(self, 'saske/idle')
        self.status = 'idle'
        print('执行了only_change_to_idle')
        #self.remove_original_just_show('saske/后仰')
        #self.status = '后仰'
    
    def change_to_houyang(self):
        if not self.status == '后仰':
            self.change_to_status_just_show('saske/后仰')
            self.status = '后仰'
    #def change_to_hou_yang_for_fen_shen(self):
        
    
    def change_to_status(self, cmd):
        if cmd == 'run':
            Style.change_to_status(self, 'saske/run')
            self.status = 'run'
        elif cmd == 'idle':
            if self.status == '后仰':
                self.change_to_status_with_no_remove_origin('saske/idle')
            else:
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
        elif cmd == '开篇挥手':
            Style.change_to_status(self, 'saske/开篇挥手')
            self.current_sprite.set_left_padding(self.start_left_padding)
            self.status = '开篇挥手'
        elif cmd == '完整跳':
            Style.change_to_status(self, 'saske/完整跳')
            self.status = '完整跳'
    def update(self):
        #可以在这里填充关于键盘的响应
        return
        
    def update_run(self, image_index):
        current_left_padding = self.character["saske/run"].get_left_padding()
        being_left_padding = current_left_padding - 11
        if being_left_padding > GameCommonData.LeftPadding:
            self.character["saske/run"].set_left_padding(being_left_padding)  
    
    
    def update_fall_down(self, image_index):
        images_num = self.character["saske/倒在地上"].get_image_num()
        current_left_padding = self.character["saske/倒在地上"].get_left_padding()
        current_top_padding = self.character["saske/倒在地上"].get_top_padding()
        being_left_padding = current_left_padding + 55
        being_top_padding = current_top_padding + (image_index*2 - images_num)*4
        self.character["saske/倒在地上"].set_left_padding(being_left_padding)  
        self.character["saske/倒在地上"].set_top_padding(being_top_padding)  
        
    def append_end_update_huidao(self, func):
        if func:
            self.character["saske/挥刀"].append_end_update_function(func)
           
    def append_update_huidao(self, func):
        if func:
            self.character["saske/挥刀"].append_update_function(func)
            
    def append_end_update_huiquan(self, func):
        if func:
            self.character["saske/挥拳"].append_end_update_function(func)
            
    def append_end_update_huiliangdao(self, func):
        if func:
            self.character["saske/挥两刀"].append_end_update_function(func)
                
    def append_update_huiliangdao(self, func):
        if func:
            self.character["saske/挥两刀"].append_update_function(func)
                
    def append_end_update_up_ti(self, func):
        if func:
            self.character["saske/向上一脚"].append_end_update_function(func)
            
    def append_end_update_kai_pian_hui_shou(self, func):
        if func:
            self.character["saske/开篇挥手"].append_end_update_function(func)
            
    def redress_left_padding(self):
        self.current_sprite.set_left_padding(self.current_sprite.get_left_padding() + 10)