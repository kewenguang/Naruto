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
        self.update_function = self.start
        self.insert_action_num = 0
        
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        
    def remove_naruto_from_sprite_group(self):
        for i in range(len(self.list_naruto)):
            self.sprite_group.remove_internal(self.list_naruto[i])
        
    def end_update_fenshen(self):
        print("6个放完了，接下来是多重影分身")
        
    def lianxufenshen(self):
        if self.insert_action_num > 5:
            self.list_naruto[self.insert_action_num - 1].clear_end_update_yigefenshen()
            self.list_naruto[self.insert_action_num - 1].change_to_status('结印')
            for i in range(len(self.list_naruto)):
                self.list_naruto[i].change_to_status_for_fenshen('idle')
                self.naruto_style.change_to_status('idle')
            self.end_update_fenshen()
            return
        if self.insert_action_num != 0:
            self.list_naruto[self.insert_action_num - 1].clear_end_update_yigefenshen()
            self.list_naruto[self.insert_action_num - 1].clear_end_update_jieyin_by_index(1)
            #self.list_naruto[self.insert_action_num - 1].change_to_status('一个分身')
        self.list_naruto[self.insert_action_num].set_current_sprite_show()
        self.list_naruto[self.insert_action_num].append_end_update_yigefenshen()#影分身结束之后去结印
        self.list_naruto[self.insert_action_num].append_jieyin_end_func(self.lianxufenshen)
        self.insert_action_num = self.insert_action_num + 1
        
            
    def add_fenshen_to_group(self):
        for i in range(6):
            naruto = NarutoStyle()
            naruto.add_to_sprite_group(self.sprite_group)
            naruto.set_key_controller(self.key_controller)
            naruto.change_to_status('一个分身')
            naruto.set_left_padding((len(self.list_naruto) + 2) * 130)
            self.list_naruto.append(naruto)
            naruto.set_current_sprite_hide()
        self.lianxufenshen()
        #单个分身的65-71是和做分身之术，所以重新捣鼓图片生成一下 以65为基准的分身之术
        #优化，注释掉那些不需要加载的图片，init方法应该可以自选加载哪些图片，可以加函数
            
    def handle_key_event(self):
        if self.key_controller.key_m:
            self.list_naruto = []
            self.add_fenshen_to_group()
            self.naruto_style.change_to_status('结印')
        elif self.key_controller.key_s:
            self.change_to_status('naruto/idle')
        
        
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
        self.naruto_style.add_to_sprite_group(self.sprite_group)
        self.naruto_style.set_key_controller(self.key_controller)
        self.saske_style.add_to_sprite_group(self.sprite_group)
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
            
    def naruto_be_houyang_with_image_index(self, image_index):
        if self.saske_style.status == '挥刀' and image_index == 4:
            self.naruto_style.change_to_status('后仰')
        elif self.saske_style.status == '挥两刀' and image_index == 3:
            self.naruto_style.change_to_status('后仰')
        elif self.saske_style.status == '挥两刀' and image_index == 6:
            self.naruto_style.change_to_status('后仰')
    
    def idle_begin_run(self):
        if self.naruto_style.status == 'idle' and self.saske_style.status == 'idle':
            #这里要跳过3秒的帧数   resource_load里面有一个fixed_flush函数  我们要想办法把它抽成一个共有的类
            #需要用到跳帧的类可以声明一个这样的对象，这样子就可以Sleep(3000)来实现跳帧,里面会记录下来，再次执行到这里不会追加Sleep时间
            #self.saske_style.change_to_status('站起来')
            self.handle_key_event()
            
            if self.insert_action_num == 0 and self.sleep(3000):
                #self.saske_style.change_to_status('站起来')
                self.naruto_style.change_to_status('run')
                self.saske_style.change_to_status('run')
            return True
        return False
    
    def naruto_attack_saske(self):
        #在下面添加判断的逻辑，是在跑还是在干什么，根据逻辑确定两者之间的位置以及是否要切换
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #首先跑一下看看是不是idle3秒之后开始相对跑近     然后下面需要判断一下是不是距离足够进了
            #print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 84:
                self.naruto_style.change_to_status('挥拳')
                self.naruto_style.append_end_update_huiquan(self.saske_be_houyang)
                self.naruto_style.append_end_update_yongtouda(self.saske_be_houyang)
                self.naruto_style.append_end_update_fanjiaoti(self.saske_be_hit_far_away)
                
        #后仰的时候，先顺着波，然后倒着播，中途被打了再顺着播，然后倒着播，播完了就变成idle了
    
    def saske_attack_naruto(self):
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 52:
                self.naruto_style.change_to_status('idle')
                self.saske_style.change_to_status('挥刀')
                self.saske_style.append_update_huidao(self.naruto_be_houyang_with_image_index)
                self.saske_style.append_end_update_huiquan(self.naruto_be_houyang)
                self.saske_style.append_update_huiliangdao(self.naruto_be_houyang_with_image_index)
                self.saske_style.append_end_update_up_ti(self.naruto_be_hit_far_away)
        
    
    def start_to_update(self):
        if self.naruto_style.status == 'idle' and self.saske_style.status == 'idle':
            self.update_function = self.update
    
    def naruto_end_update_seyouzhishu(self):
        self.naruto_style.change_to_status("idle")
        self.start_to_update()
    
    def saske_end_update_kai_pian_hui_shou(self):
        self.saske_style.change_to_status("idle")
        self.start_to_update()
        #self.saske_style. redress_left_padding()
        
    def start(self):
        if self.naruto_style.status == 'idle' and self.saske_style.status == 'idle':
            if self.sleep(1000):
                self.naruto_style.change_to_status('色诱之术')
                self.saske_style.change_to_status('开篇挥手')
                self.naruto_style.append_end_update_seyouzhishu(self.naruto_end_update_seyouzhishu)
                self.saske_style.append_end_update_kai_pian_hui_shou(self.saske_end_update_kai_pian_hui_shou)
    
    #看看有没有用python来裁剪图片的
    def update(self):
        if self.current_attack_player == 'naruto' and self.current_attacked_player == 'saske':
            self.naruto_attack_saske()
        elif self.current_attack_player == 'saske' and self.current_attacked_player == 'naruto':
            self.saske_attack_naruto()