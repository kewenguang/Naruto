'''
Created on 2019年8月28日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class NarutoStyle(Style):
    
    def hou_yang_end_update_handle(self):
        self.change_to_status('idle')
        
    def naruto_status_to_qilai(self):
        self.change_to_status('翻身起来')
        
    def naruto_status_to_touda(self):
        self.change_to_status('用头打')
        
    def naruto_status_to_fanjiaoti(self):
        self.change_to_status('反脚踢')
        
    def naruto_status_to_idle(self):
        self.change_to_status('idle')
        
    def naruto_status_to_jieyin(self):
        self.change_to_status('结印')
        
    def set_naruto_jieyin_end_func(self):
        self.character["naruto/结印"].image_index = len(self.character["naruto/结印"].images) - 1
        
    def append_jieyin_end_func(self, func):
        self.character["naruto/结印"].append_end_update_function(func) 
        
    
    #situation_flag为1的时候，正常的鸣人
    #situation_flag为2的时候，单个分身的鸣人
    #situation_flag为3的时候，多重影分身
        
    def __init__(self, situation_flag = 1):
        self.character = {}
        
        '''
        naruto_image_url = ["naruto/multi_shadow_separation","naruto/向上跳", "naruto/向下跳", "naruto/小手里剑",
                             "naruto/idle", "naruto/win", "naruto/death",
                            "naruto/shadow_separator", "naruto/liandan", "naruto/大手里剑", 
                            "naruto/手里剑分身", "naruto/run", "naruto/完整跳", "naruto/铲地踢", "naruto/冲挥苦无", "naruto/打中特效",
                            "naruto/单个分身", "naruto/蹲着", "naruto/二人踢", "naruto/发手里剑", "naruto/翻身起来",
                            "naruto/反脚踢", "naruto/防御", "naruto/风遁螺旋丸形成", "naruto/后仰", "naruto/挥苦无",
                            "naruto/挥拳", "naruto/举螺旋丸", "naruto/空中一脚", "naruto/螺旋丸", "naruto/螺旋丸击中",
                            "naruto/扔手里剑", "naruto/色诱之术", "naruto/下按螺旋丸", "naruto/向上一脚",
                            "naruto/用头打", "naruto/云朵", "naruto/风遁螺旋丸", "naruto/风遁螺旋丸爆炸", "naruto/一个分身", "naruto/结印"]
        '''
        naruto_image_url = ["naruto/multi_shadow_separation", "naruto/idle", "naruto/death", "naruto/run", "naruto/挥拳"
                            , "naruto/用头打", "naruto/反脚踢", "naruto/后仰", "naruto/翻身起来", "naruto/色诱之术", "naruto/一个分身",
                            "naruto/结印"]
        
        if situation_flag == 1:
            naruto_image_url = ["naruto/multi_shadow_separation", "naruto/idle", "naruto/death", "naruto/run", "naruto/挥拳"
                            , "naruto/用头打", "naruto/反脚踢", "naruto/后仰", "naruto/翻身起来", "naruto/色诱之术", "naruto/一个分身",
                            "naruto/结印"]
        elif situation_flag == 2:
            naruto_image_url = ["naruto/结印", "naruto/一个分身", "naruto/idle", "naruto/螺旋丸"]
        elif situation_flag == 3:
            naruto_image_url = ["naruto/multi_shadow_separation"]
        
        #不应该这样笼统地加，而应该一个一个图集地添加  这样好确定应该放在什么位置 以及update里的内容是什么
        #并且所有图集都应该放在一个HashMap里面，这样比如按下了d键就知道显示哪个图集代表鸣人在往前走
        #left_begin = 60
        #top_begin = 200
        
        #考虑到加载图集会访问硬盘，所以一次性把需要的图集都加载进来
        for i in range(len(naruto_image_url)):
            self.add_sprite(naruto_image_url[i])
            
        if situation_flag == 1:
            self.character["naruto/run"].append_update_function(self.update_run) 
            self.character["naruto/挥拳"].append_end_update_function(self.naruto_status_to_touda)
            self.character["naruto/挥拳"].set_frame_rate(8)
            self.character["naruto/用头打"].append_end_update_function(self.naruto_status_to_fanjiaoti)
            self.character["naruto/用头打"].set_frame_rate(8)
            self.character["naruto/反脚踢"].append_end_update_function(self.naruto_status_to_idle)
            
            self.character["naruto/后仰"].append_end_update_function(self.hou_yang_end_update_handle)
            self.character["naruto/后仰"].set_frame_rate(8)
            
            self.character["naruto/death"].append_update_function(self.update_fall_down) 
            self.character["naruto/death"].append_end_update_function(self.naruto_status_to_qilai) 
            
            self.character["naruto/翻身起来"].append_end_update_function(self.naruto_status_to_idle) 
            self.character["naruto/翻身起来"].set_frame_rate(8)
            
            self.character["naruto/色诱之术"].set_frame_rate(7)
        
        if situation_flag == 2:
            self.character["naruto/螺旋丸"].set_frame_rate(11)
        
        if situation_flag == 1 or situation_flag == 2: 
            self.current_sprite = self.character["naruto/idle"]
            self.status = 'idle'
            self.current_sprite.hidden = False
            self.current_sprite.set_left_padding(60)
            self.current_sprite.set_top_padding(GameCommonData.character_level)
            
            self.character["naruto/一个分身"].set_frame_rate(20)
            
            self.character["naruto/结印"].set_frame_rate(15)
            self.character["naruto/结印"].append_end_update_function(self.set_naruto_jieyin_end_func) 
        elif situation_flag == 3:
            self.current_sprite = self.character["naruto/multi_shadow_separation"]
            self.status = 'multi_shadow_separation'
            self.current_sprite.hidden = False
            self.character["naruto/multi_shadow_separation"].set_frame_rate(23)
            
        
        #用来保存最初始的left_padding
        self.left_padding = self.get_left_padding()
            #character_sprite = self.add_sprite(naruto_image_url_2[i])
            #top_begin = top_begin + 130
            #if top_begin > GameCommonData.HEIGHT:
                #top_begin = 120
                #left_begin = left_begin + 120
                
    #这个update处理键盘响应，然后移动图集，不处理图片更新，图片更新由sprite_group负责
    
    def set_left_padding(self, left_padding):
        self.current_sprite.set_left_padding(left_padding)
    
    def set_top_padding(self, top_padding):
        self.current_sprite.set_top_padding(top_padding)
    
    def change_to_status_for_fenshen(self, status):
        if status == 'idle':
            Style.change_to_status(self, 'naruto/idle')
            self.status = 'idle'
            
    def change_to_status(self, status):
        if status == 'run':
            Style.change_to_status(self, 'naruto/run')
            self.status = 'run'
        elif status == 'idle':
            Style.change_to_status(self, 'naruto/idle')
            self.status = 'idle'
            self.character["naruto/idle"].set_left_padding(self.left_padding)
        elif status == '挥拳':
            Style.change_to_status(self, 'naruto/挥拳')
            self.status = '挥拳'
        elif status == '反脚踢':
            Style.change_to_status(self, 'naruto/反脚踢')
            self.status = '反脚踢'
        elif status == '用头打':
            Style.change_to_status(self, 'naruto/用头打')
            self.status = '用头打'
        elif status == '后仰':
            Style.change_to_status(self, 'naruto/后仰')
            self.status = '后仰'
        elif status == 'death':
            Style.change_to_status(self, 'naruto/death')
            self.status = 'death'
        elif status == '翻身起来':
            Style.change_to_status(self, 'naruto/翻身起来')
            self.status = '翻身起来'
        elif status == '色诱之术':
            Style.change_to_status(self, 'naruto/色诱之术')
            self.status = '色诱之术'
            self.character["naruto/色诱之术"].set_left_padding(85)
        elif status == '一个分身':
            Style.change_to_status(self, 'naruto/一个分身')
            self.status = '一个分身'
        elif status == '结印':
            Style.change_to_status(self, 'naruto/结印')
            self.status = '结印'
        elif status == '螺旋丸':
            Style.change_to_status(self, 'naruto/螺旋丸')
            self.status = '螺旋丸'
            
    def update(self):
        if self.key_controller.key_d:
            self.change_to_status('naruto/run')
        elif self.key_controller.key_s:
            self.change_to_status('naruto/idle')
        elif self.key_controller.key_j:
            self.change_to_status('naruto/挥拳')
        elif self.key_controller.key_k:
            self.change_to_status('naruto/反脚踢')
        elif self.key_controller.key_l:
            self.change_to_status('naruto/用头打')
        elif self.key_controller.key_u:
            self.change_to_status('naruto/multi_shadow_separation')  #这个表现要组装一下
        elif self.key_controller.key_i:
            self.change_to_status('naruto/')   #这个表现要组装一下
        #我们要对用到的空白多的图片做边缘裁剪，来得到小的图片人物
    
    #专属某一个图集
    def update_run(self, image_index):
        current_left_padding = self.character["naruto/run"].get_left_padding()
        being_left_padding = current_left_padding + 7
        if being_left_padding < GameCommonData.RightPadding:
            self.character["naruto/run"].set_left_padding(being_left_padding)  
            
    def append_end_update_huiquan(self, func):
        if func:
            self.character["naruto/挥拳"].append_end_update_function(func)
    
    def append_end_update_yongtouda(self, func):
        if func:
            self.character["naruto/用头打"].append_end_update_function(func)
    
    def append_end_update_fanjiaoti(self, func):
        if func:
            self.character["naruto/反脚踢"].append_end_update_function(func)
           
    def append_end_update_yigefenshen(self):
        self.character["naruto/一个分身"].append_end_update_function(self.naruto_status_to_jieyin)
            
    def clear_end_update_yigefenshen(self):
        self.character["naruto/一个分身"].clear_end_update_function()
            
    def clear_end_update_jieyin_by_index(self, index):
        self.character["naruto/结印"].clear_end_update_function_by_index(index)  
            
    def clear_end_update_jieyin(self):
        self.character["naruto/结印"].clear_end_update_function()
            
    def update_fall_down(self, image_index):
        images_num = self.character["naruto/death"].get_image_num()
        current_left_padding = self.character["naruto/death"].get_left_padding()
        current_top_padding = self.character["naruto/death"].get_top_padding()
        being_left_padding = current_left_padding - 35
        being_top_padding = current_top_padding + (image_index*2 - images_num)*4
        self.character["naruto/death"].set_left_padding(being_left_padding)  
        self.character["naruto/death"].set_top_padding(being_top_padding)  
        
    def append_end_update_seyouzhishu(self, func):
        if func:
            self.character["naruto/色诱之术"].append_end_update_function(func)