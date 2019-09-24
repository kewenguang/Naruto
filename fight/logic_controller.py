'''
Created on 2019年9月12日

@author: kewenguang
'''
import time

from fight.nanuto_style import NarutoStyle
from fight.saske_style import SaskeStyle

class Controller():
    def __init__(self):
        self.naruto_style = NarutoStyle()
        self.saske_style = SaskeStyle()
        self.current_attack_player = "naruto"
        self.current_attacked_player = 'saske'
        #self.t = time.time()
        self.flush_time = 0 #int(round(self.t * 1000))
        
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        
    def set_key_controller(self, key_controller):
        self.key_controller = key_controller
        
    def sleep(self, time_interval):
        if self.flush_time == 0:
            self.flush_time = int(round(time.time() * 1000))
            return False
        else:
            if self.flush_time + time_interval > int(round(time.time() * 1000)):
                return False
            else:
                self.flush_time = 0
                return True
        
    def ready(self):
        self.naruto_style.set_sprite_group(self.sprite_group)
        self.naruto_style.set_key_controller(self.key_controller)
        self.saske_style.set_sprite_group(self.sprite_group)
        self.saske_style.set_key_controller(self.key_controller)
    
    def saske_be_hit_far_away(self):
        self.saske_style.change_to_status('倒在地上')
        self.current_attack_player = 'saske'
        self.current_attacked_player = 'naruto'
    
    def naruto_be_hit_far_away(self):
        self.naruto_style.change_to_status('death')
        self.current_attack_player = 'naruto'
        self.current_attacked_player = 'saske'
    
    def saske_be_houyang(self):
        self.saske_style.change_to_status('后仰')
        
    def naruto_be_houyang(self):
        self.naruto_style.change_to_status('后仰')
    
    def idle_begin_run(self):
        if self.naruto_style.status == 'idle' and self.saske_style.status == 'idle':
            #这里要跳过3秒的帧数   resource_load里面有一个fixed_flush函数  我们要想办法把它抽成一个共有的类
            #需要用到跳帧的类可以声明一个这样的对象，这样子就可以Sleep(3000)来实现跳帧,里面会记录下来，再次执行到这里不会追加Sleep时间
            #self.saske_style.change_to_status('站起来')
            if self.sleep(3000):
                #self.saske_style.change_to_status('站起来')
                self.naruto_style.change_to_status('run')
                self.saske_style.change_to_status('run')
            return True
        return False
    
    def naruto_attack_saske(self):
        #在下面添加判断的逻辑，是在跑还是在干什么，根据逻辑确定两者之间的位置以及是否要切换
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #首先跑一下看看是不是idle3秒之后开始相对跑近     然后下面需要判断一下是不是距离足够进了
            print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 85:
                self.naruto_style.change_to_status('挥拳')
                self.naruto_style.append_end_update_huiquan(self.saske_be_houyang)
                self.naruto_style.append_end_update_yongtouda(self.saske_be_houyang)
                self.naruto_style.append_end_update_fanjiaoti(self.saske_be_hit_far_away)
                
        #后仰的时候，先顺着波，然后倒着播，中途被打了再顺着播，然后倒着播，播完了就变成idle了
    
    def saske_attack_naruto(self):
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 85:
                self.saske_style.change_to_status('挥刀')
                self.saske_style.append_end_update_huidao(self.naroto_be_houyang)
                self.saske_style.append_end_update_huiquan(self.naroto_be_houyang)
                self.saske_style.append_end_update_huiliangdao(self.naroto_be_houyang)
                self.saske_style.append_end_update_up_ti(self.naruto_be_hit_far_away)
        
    
    def update(self):
        if self.current_attack_player == 'naruto' and self.current_attacked_player == 'saske':
            self.naruto_attack_saske()
        elif self.current_attack_player == 'saske' and self.current_attacked_player == 'naruto':
            self.saske_attack_naruto()