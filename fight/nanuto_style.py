'''
Created on 2019年8月28日

@author: kewenguang
'''
from fight.resource_load import GameCommonData
from fight.resource_load import Style

class NarutoStyle(Style):
    def __init__(self):
        self.character = {}
        
        naruto_image_url = ["naruto/multi_shadow_separation","naruto/向上跳", "naruto/向下跳", "naruto/小手里剑",
                             "naruto/idle", "naruto/win", "naruto/death",
                            "naruto/shadow_separator", "naruto/liandan", "naruto/大手里剑", 
                            "naruto/手里剑分身", "naruto/run", "naruto/完整跳", "naruto/铲地踢", "naruto/冲挥苦无", "naruto/打中特效",
                            "naruto/单个分身", "naruto/蹲着", "naruto/二人踢", "naruto/发手里剑", "naruto/翻身起来",
                            "naruto/反脚踢", "naruto/防御", "naruto/风遁螺旋丸形成", "naruto/后仰", "naruto/挥苦无",
                            "naruto/挥拳", "naruto/举螺旋丸", "naruto/空中一脚", "naruto/螺旋丸", "naruto/螺旋丸击中",
                            "naruto/扔手里剑", "naruto/色诱之术", "naruto/下按螺旋丸", "naruto/向上一脚",
                            "naruto/用头打", "naruto/云朵", "naruto/风遁螺旋丸", "naruto/风遁螺旋丸爆炸"]

        #不应该这样笼统地加，而应该一个一个图集地添加  这样好确定应该放在什么位置 以及update里的内容是什么
        #并且所有图集都应该放在一个HashMap里面，这样比如按下了d键就知道显示哪个图集代表鸣人在往前走
        #left_begin = 60
        #top_begin = 200
        
        #考虑到加载图集会访问硬盘，所以一次性把需要的图集都加载进来
        for i in range(len(naruto_image_url)):
            self.add_sprite(naruto_image_url[i])
        self.character["naruto/run"].set_fuction(self.update_run) 
        self.current_sprite = self.character["naruto/idle"]
        self.status = 'idle'
        self.current_sprite.hidden = False
        self.current_sprite.set_left_padding(60)
        self.current_sprite.set_top_padding(200)
        
            #character_sprite = self.add_sprite(naruto_image_url_2[i])
            #top_begin = top_begin + 130
            #if top_begin > GameCommonData.HEIGHT:
                #top_begin = 120
                #left_begin = left_begin + 120
                
    #这个update处理键盘响应，然后移动图集，不处理图片更新，图片更新由sprite_group负责
    
    
    def change_status(self, status):
        if status == 'run':
            self.change_to_status('naruto/run')
            self.status = 'run'
        elif status == 'idle':
            self.change_to_status('naruto/idle')
            self.status = 'idle'
        elif status == '挥拳':
            self.change_to_status('naruto/挥拳')
            self.status = '挥拳'
        elif status == '反脚踢':
            self.change_to_status('naruto/反脚踢')
            self.status = '反脚踢'
        elif status == '用头打':
            self.change_to_status('naruto/用头打')
            self.status = '用头打'
            
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
    def update_run(self):
        current_left_padding = self.character["naruto/run"].get_left_padding()
        being_left_padding = current_left_padding + 10
        if being_left_padding < GameCommonData.RightPadding:
            self.character["naruto/run"].set_left_padding(being_left_padding)  
            
    def update_fan_jiao_ti(self):
        current_left_padding = self.character["naruto/反脚踢"].get_left_padding()
        being_left_padding = current_left_padding + 5
        if being_left_padding < GameCommonData.RightPadding:
            self.character["naruto/run"].set_left_padding(being_left_padding)
        '''
        multi_shadow_separation = CharacterSprite()
        multi_shadow_separation.set_images("naruto/multi_shadow_separation")
        self.character.append(multi_shadow_separation)
        
        idle = CharacterSprite()
        idle.set_images("naruto/idle")
        self.character.append(idle)

        win = CharacterSprite()
        win.set_images("naruto/win")
        self.character.append(win)
        win.rect.centerx = 30
        win.rect.bottom = 60
        
        death = CharacterSprite()
        death.set_images("naruto/death")
        self.character.append(death)
        death.rect.centerx = 30
        death.rect.bottom = 150
        
        shadow_separator = CharacterSprite()
        shadow_separator.set_images("naruto/shadow_separator")
        self.character.append(shadow_separator)
        shadow_separator.rect.centerx = 30
        shadow_separator.rect.bottom = 240
        
        liandan = CharacterSprite()
        liandan.set_images("naruto/liandan")
        self.character.append(liandan)
        liandan.rect.centerx = 30
        liandan.rect.bottom = 330
        
        da_shou_li_jian = CharacterSprite()
        da_shou_li_jian.set_images("naruto/大手里剑")
        self.character.append(da_shou_li_jian)
        da_shou_li_jian.rect.centerx = 60
        da_shou_li_jian.rect.bottom = 420
        
        feng_dun_luo_xuan_wan = CharacterSprite()
        feng_dun_luo_xuan_wan.set_images("naruto/风遁螺旋丸")
        self.character.append(feng_dun_luo_xuan_wan)
        feng_dun_luo_xuan_wan.rect.centerx = 60
        feng_dun_luo_xuan_wan.rect.bottom = 510
        
        show_li_jian_fen_shen = CharacterSprite()
        show_li_jian_fen_shen.set_images("naruto/手里剑分身")
        self.character.append(show_li_jian_fen_shen)
        show_li_jian_fen_shen.rect.centerx = 60
        show_li_jian_fen_shen.rect.bottom = 600
        
        show_li_jian_fen_shen = CharacterSprite()
        show_li_jian_fen_shen.set_images("naruto/向上跳")
        self.character.append(show_li_jian_fen_shen)
        show_li_jian_fen_shen.rect.centerx = 60
        show_li_jian_fen_shen.rect.bottom = 600
        
        show_li_jian_fen_shen = CharacterSprite()
        show_li_jian_fen_shen.set_images("naruto/向下跳")
        self.character.append(show_li_jian_fen_shen)
        show_li_jian_fen_shen.rect.centerx = 60
        show_li_jian_fen_shen.rect.bottom = 600
        
        show_li_jian_fen_shen = CharacterSprite()
        show_li_jian_fen_shen.set_images("naruto/小手里剑")
        self.character.append(show_li_jian_fen_shen)
        show_li_jian_fen_shen.rect.centerx = 60
        show_li_jian_fen_shen.rect.bottom = 600
        '''
            
    