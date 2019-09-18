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
    
    def naruto_attack_saske(self):
        print('naruto attack')
        #在下面添加判断的逻辑，是在跑还是在干什么，根据逻辑确定两者之间的位置以及是否要切换
        if self.naruto_style.status == 'idle' and self.saske_style.status == 'idle':
            #这里要跳过3秒的帧数   resource_load里面有一个fixed_flush函数  我们要想办法把它抽成一个共有的类
            #需要用到跳帧的类可以声明一个这样的对象，这样子就可以Sleep(3000)来实现跳帧,里面会记录下来，再次执行到这里不会追加Sleep时间
            if self.sleep(3000):
                self.naruto_style.change_status('run')
                self.saske_style.change_status('run')
        elif self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #首先跑一下看看是不是idle3秒之后开始相对跑近     然后下面需要判断一下是不是距离足够进了
            
            return
    
    def saske_attack_naruto(self):
        print('saske attack')
    
    def update(self):
        if self.current_attack_player == 'naruto' and self.current_attacked_player == 'saske':
            self.naruto_attack_saske()
        elif self.current_attack_player == 'saske' and self.current_attacked_player == 'naruto':
            self.saske_attack_naruto()