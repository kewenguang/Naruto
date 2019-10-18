'''
Created on 2019年9月12日

@author: kewenguang
'''
import time

from fight.nanuto_style import NarutoStyle
from fight.saske_style import SaskeStyle
from fight.woailuo_style import WoailuoStyle
from fight.kakaxi_style import KakaxiStyle
from fight import saske_style

class Controller():
    def __init__(self, sprite_group):
        self.naruto_style = NarutoStyle(sprite_group)
        self.saske_style = SaskeStyle(sprite_group)
        self.sprite_group = sprite_group
        self.current_attack_player = "naruto"
        self.current_attacked_player = 'saske'
        #self.t = time.time()
        self.flush_time = 0 #int(round(self.t * 1000))
        self.update_function = self.start
        self.insert_action_num = 0
        
        self.test_flag = True
        
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        
    def remove_naruto_from_sprite_group(self):
        for i in range(len(self.list_naruto)):
            self.sprite_group.remove_internal(self.list_naruto[i])
        
        
    #鸣人特效##############################################################################################
    def sub_insert_action_num(self):
        self.insert_action_num = self.insert_action_num - 1
        print('self.insert_action_num:' + str(self.insert_action_num))
    
    def multi_shadow_separation_end(self):
        for i in range(len(self.list_naruto)):
            self.list_naruto[i].change_to_status('螺旋丸')
            self.list_naruto[i].character['naruto/螺旋丸'].append_end_update_function(self.sub_insert_action_num)
            
    def multi_shadow_separation_update(self, image_index):
        if image_index % 5 == 0 and image_index < 62 and image_index > 9:
            self.saske_style.change_to_houyang()
        
    def end_update_fenshen(self):
        print("6个放完了，接下来是多重影分身")
        
        naruto = NarutoStyle(self.sprite_group, situation_flag = 3)
        naruto.add_to_sprite_group()
        naruto.set_key_controller(self.key_controller)
        naruto.set_left_padding( self.saske_style.get_left_padding())
        naruto.set_top_padding( self.saske_style.get_top_padding() + 105)
        naruto.character['naruto/multi_shadow_separation'].append_update_function(self.multi_shadow_separation_update)
        
        for i in range(len(self.list_naruto)):
            self.list_naruto[i].change_to_status_for_fenshen('idle')
            self.list_naruto[i].set_saske(self.saske_style)
            self.naruto_style.change_to_status('idle')
        
        naruto.character["naruto/multi_shadow_separation"].append_end_update_function(self.multi_shadow_separation_end)
        
        
    def lianxufenshen(self):
        if self.insert_action_num > self.fenshen_num - 1:
            self.list_naruto[self.insert_action_num - 1].clear_end_update_yigefenshen()
            self.list_naruto[self.insert_action_num - 1].clear_end_update_jieyin_by_index(1)
            self.list_naruto[self.insert_action_num - 1].change_to_status('结印')
            self.list_naruto[self.insert_action_num - 1].append_jieyin_end_func(self.end_update_fenshen)
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
        self.fenshen_num = 4
        for i in range(self.fenshen_num):
            naruto = NarutoStyle(self.sprite_group, situation_flag = 2)
            naruto.add_to_sprite_group()
            naruto.set_key_controller(self.key_controller)
            naruto.change_to_status('一个分身')
            naruto.set_left_padding((len(self.list_naruto) + 1) * 170 + len(self.list_naruto) * 120)
            self.list_naruto.append(naruto)
            naruto.set_current_sprite_hide()
        self.lianxufenshen()
        #单个分身的65-71是和做分身之术，所以重新捣鼓图片生成一下 以65为基准的分身之术
        #优化，注释掉那些不需要加载的图片，init方法应该可以自选加载哪些图片，可以加函数
            
    def chu_fa_fen_shen(self):
        self.list_naruto = []
        self.add_fenshen_to_group()
        self.naruto_style.change_to_status('结印')
    #鸣人特效##############################################################################################
    
    
    #佐助特效##############################################################################################
    def xuzuo_jian_update(self, image_index):
        left_padding = self.saske_xuzuo_jian.character['saske/须左的箭'].get_left_padding()
        if left_padding - self.naruto_style.get_left_padding() < 30:
            self.saske_xuzuo_jian.remove_current_sprite_from_sprite_group()
            self.naruto_style.change_to_status('death')
            self.saske_xuzuo.character['saske/须左'].clear_update_function()
            #self.saske_xuzuo_jian.character['saske/须左的箭'].image_index = 14
        else:
            self.saske_xuzuo_jian.character['saske/须左的箭'].set_left_padding(left_padding - 120)
    
    def xuzuo_update(self, image_index):
        if image_index == 12:
            self.saske_xuzuo_jian = SaskeStyle(self.sprite_group, situation_flag = 3)
            self.saske_xuzuo_jian.set_left_padding(self.saske_style.get_left_padding() - 200)
            self.saske_xuzuo_jian.set_top_padding(self.saske_style.get_top_padding() - 30)
            self.saske_xuzuo_jian.character['saske/须左的箭'].append_update_function(self.xuzuo_jian_update)
        elif image_index == 14:
            self.saske_xuzuo.character['saske/须左'].image_index = 13
            
    def xu_zuo(self):
        self.saske_xielunyan.remove_current_sprite_from_sprite_group()
        self.saske_xuzuo = SaskeStyle(self.sprite_group, situation_flag = 2)
        self.saske_xuzuo.set_left_padding(self.saske_style.get_left_padding())
        self.saske_xuzuo.set_top_padding(self.saske_style.get_top_padding() + 20)
        self.saske_xuzuo.character['saske/须左'].append_update_function(self.xuzuo_update)
        self.saske_xuzuo.character['saske/须左'].append_end_update_function(self.saske_xuzuo.remove_current_sprite_from_sprite_group)
        
    def xie_lun_yan(self):
        self.saske_xielunyan = SaskeStyle(self.sprite_group, situation_flag = 4)
        self.saske_xielunyan.set_left_padding(self.saske_style.get_left_padding() - 40)
        self.saske_xielunyan.set_top_padding(self.saske_style.get_top_padding() - 40)
        self.saske_xielunyan.character['saske/写轮眼'].append_end_update_function(self.xu_zuo)
    #佐助特效##############################################################################################
    
    
    #我爱罗特效##############################################################################################
    def songzang(self):
        print('送葬')
    
    def wo_ai_luo_to_idle(self):
        self.wo_ai_luo.change_to_status('idle')
        
    def add_wo_ai_luo(self):
        self.wo_ai_luo = WoailuoStyle(self.sprite_group)
        self.wo_ai_luo.set_left_padding(self.saske_style.get_left_padding() - 600)
        self.wo_ai_luo.change_to_status('出现')
        self.wo_ai_luo.character['woailuo/出现'].append_end_update_function(self.wo_ai_luo_to_idle)
        
    def end_sa_pu(self):
        self.wo_ai_luo_to_idle()
        self.wo_ai_luo_sa_pu.remove_current_sprite_from_sprite_group()
        
    def sa_pu_update(self, image_index):
        if image_index == 8 :
            self.saske_style.change_to_houyang()
        if image_index == 11 :
            self.saske_style.change_to_houyang()
    
    def sa_pu(self):
        self.wo_ai_luo.character['woailuo/蹲下'].stop_flush = True
        self.wo_ai_luo_sa_pu = WoailuoStyle(self.sprite_group, situation_flag = 2)
        self.wo_ai_luo_sa_pu.set_left_padding(self.saske_style.get_left_padding() - 150)
        self.wo_ai_luo_sa_pu.character['woailuo/沙瀑送葬'].append_end_update_function(self.end_sa_pu)
        self.wo_ai_luo_sa_pu.character['woailuo/沙瀑送葬'].append_update_function(self.sa_pu_update)
        
    def sa_pu_song_zang(self):
        self.wo_ai_luo.change_to_status('蹲下')
        self.wo_ai_luo.character['woailuo/蹲下'].append_end_update_function(self.sa_pu)
        
    def sa_fu_jiu_update(self, image_index):
        if image_index == 11:
            self.saske_style.remove_current_sprite_from_sprite_group()
        if image_index == 14:
            self.wo_ai_luo_sa_fu_jiu.character['woailuo/砂缚柩'].image_index = image_index - 1

    def end_update_wo_quan(self):
        #if self.wo_ai_luo.character['woailuo/举手握拳'].image_index == 0:
        self.wo_ai_luo.character['woailuo/举手握拳'].image_index = len(self.wo_ai_luo.character['woailuo/举手握拳'].images) - 1
        
    def remove_safujiu(self):
        self.wo_ai_luo_sa_fu_jiu.remove_current_sprite_from_sprite_group()
        self.wo_ai_luo.change_to_status('idle')
        
    def sa_fu_jiu(self):
        self.wo_ai_luo.change_to_status('举手握拳')
        self.wo_ai_luo.character['woailuo/举手握拳'].append_end_update_function(self.end_update_wo_quan)
        self.wo_ai_luo_sa_fu_jiu = WoailuoStyle(self.sprite_group, situation_flag = 3)
        self.wo_ai_luo_sa_fu_jiu.set_left_padding(self.saske_style.get_left_padding() + 10)
        self.wo_ai_luo_sa_fu_jiu.character['woailuo/砂缚柩'].append_update_function(self.sa_fu_jiu_update)
        self.wo_ai_luo_sa_fu_jiu.character['woailuo/砂缚柩'].append_end_update_function(self.remove_safujiu)
    #我爱罗特效##############################################################################################
    
    
    #卡卡西特效##############################################################################################
    
    def ka_ka_xi_to_idle(self):
        self.ka_ka_xi.change_to_status('idle')
        
    def add_ka_ka_xi(self):
        self.saske_style.remove_current_sprite_from_sprite_group()
        self.ka_ka_xi = KakaxiStyle(self.sprite_group)
        self.ka_ka_xi.set_left_padding(self.saske_style.get_left_padding())
        self.ka_ka_xi.change_to_status('出现')
        self.ka_ka_xi.character['kakaxi/出现'].append_end_update_function(self.ka_ka_xi_to_idle)
    
    def shui_long_dan_zhi_shu_update_function(self, image_index):
        left_padding = self.ka_ka_xi_shui_long_dan_zhi_shu.get_left_padding()
        self.ka_ka_xi_shui_long_dan_zhi_shu.set_left_padding(left_padding - 20) #12 20
        if image_index == 20:
            self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].image_index = 12
        if left_padding == 300: #这个数值在最后联调的时候需要改动-----------------------------------------
            self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].image_index = 21
    
    def release_shui_long_dan_zhi_shu(self):
        self.ka_ka_xi_shui_long_dan_zhi_shu = KakaxiStyle(self.sprite_group, situation_flag = 5)
        self.ka_ka_xi_shui_long_dan_zhi_shu.set_left_padding(self.saske_style.get_left_padding() + 80)
        self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].append_update_function(self.shui_long_dan_zhi_shu_update_function)
        self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].append_end_update_function(self.ka_ka_xi_to_idle)
        self.ka_ka_xi.character['kakaxi/站直'].clear_end_update_function_by_index(0)
    
    #首先  龙的高度太高了，要放下来一些
    #另外  龙打过去的话，是要放特效的，那个特效要加上
    
    def end_update_zhan_zhi(self):
        #if self.wo_ai_luo.character['woailuo/举手握拳'].image_index == 0:
        self.ka_ka_xi.character['kakaxi/站直'].image_index = len(self.ka_ka_xi.character['kakaxi/站直'].images) - 1
    
    def shui_long_dan_zhi_shu(self):
        self.ka_ka_xi.change_to_status('站直')
        self.ka_ka_xi.character['kakaxi/站直'].append_end_update_function(self.release_shui_long_dan_zhi_shu)
        self.ka_ka_xi.character['kakaxi/站直'].append_end_update_function(self.end_update_zhan_zhi)
    #神威的特效暂时定为卡卡西通过神威隐身，然后我爱罗被四面八方的手里剑转一圈受伤，最后卡卡西出现在原来的地方
    #卡卡西特效##############################################################################################
    
    def handle_key_event(self):
        if self.key_controller.key_m:
            self.chu_fa_fen_shen()
        elif self.key_controller.key_w:
            #self.xie_lun_yan()
            #self.sa_pu_song_zang()
            #self.sa_fu_jiu()
            self.shui_long_dan_zhi_shu()
        elif self.key_controller.key_a:
            #self.add_wo_ai_luo()
            self.add_ka_ka_xi()
        elif self.key_controller.key_s:
            #self.change_to_status('naruto/idle')
            self.wo_ai_luo_sa_fu_jiu.character['woailuo/砂缚柩'].clear_update_function()
    
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
        self.naruto_style.add_to_sprite_group()
        self.naruto_style.set_key_controller(self.key_controller)
        self.saske_style.add_to_sprite_group()
        self.saske_style.set_key_controller(self.key_controller)
    
    def saske_be_hit_far_away(self):
        self.saske_style.change_to_status('倒在地上')
        self.current_attack_player = 'saske'
        self.current_attacked_player = 'naruto'
    
    def naruto_be_hit_far_away(self):
        self.naruto_style.change_to_status('death')
        self.current_attack_player = 'naruto'
        self.current_attacked_player = 'saske'
        
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
            return True
            if self.insert_action_num == 0 and self.sleep(3000):
                #self.saske_style.change_to_status('站起来')
                self.naruto_style.change_to_status('run')
                self.saske_style.change_to_status('run')

        return False
    
    def naruto_attack_saske(self):
        #在下面添加判断的逻辑，是在跑还是在干什么，根据逻辑确定两者之间的位置以及是否要切换
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #首先跑一下看看是不是idle3秒之后开始相对跑近     然后下面需要判断一下是不是距离足够进了
            #print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 84:
                self.naruto_style.change_to_status('挥拳')
                self.naruto_style.append_end_update_huiquan(self.saske_style.change_to_houyang())
                self.naruto_style.append_end_update_yongtouda(self.saske_style.change_to_houyang())
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
                #self.naruto_style.change_to_status('色诱之术')
                #self.saske_style.change_to_status('开篇挥手')
                
                #手动添加一下，下面这些函数以后是要删除掉的
                self.naruto_end_update_seyouzhishu()
                self.saske_end_update_kai_pian_hui_shou()
                
                self.naruto_style.append_end_update_seyouzhishu(self.naruto_end_update_seyouzhishu)
                self.saske_style.append_end_update_kai_pian_hui_shou(self.saske_end_update_kai_pian_hui_shou)
    
    #看看有没有用python来裁剪图片的
    def update(self):
        if self.current_attack_player == 'naruto' and self.current_attacked_player == 'saske':
            self.naruto_attack_saske()
        elif self.current_attack_player == 'saske' and self.current_attacked_player == 'naruto':
            self.saske_attack_naruto()