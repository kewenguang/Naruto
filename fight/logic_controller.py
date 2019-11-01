'''
Created on 2019年9月12日

@author: kewenguang
'''
import time

from fight.nanuto_style import NarutoStyle
from fight.saske_style import SaskeStyle
from fight.woailuo_style import WoailuoStyle
from fight.kakaxi_style import KakaxiStyle
from fight.zilaiye_style import ZilaiyeStyle
from fight.pain_style import PainStyle
from fight.resource_load import Color
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
        self.update_screen = self.update_screen_with_white
        
    def set_sprite_group(self, sprite_group):
        self.sprite_group = sprite_group
        
    def remove_naruto_from_sprite_group(self):
        for i in range(len(self.list_naruto)):
            self.sprite_group.remove_internal(self.list_naruto[i])
        
    def set_mixer(self, mixer):
        self.mixer = mixer
        self.channel2 = mixer.Channel(2)
        self.channel3 = mixer.Channel(3)
        self.channel4 = mixer.Channel(4)
    
    def play_music(self, url):
        self.mixer.music.load('../assets/bgm/' + url)
        self.mixer.music.play(1, 0)
        
    def play_sound(self, url):
        sound = self.mixer.Sound('../assets/bgm/' + url)
        self.channel2.play(sound)
        
    def play_sound_by_channel3(self, url):
        sound = self.mixer.Sound('../assets/bgm/' + url)
        self.channel3.play(sound)
        
    def play_sound_queue(self, url):
        sound = self.mixer.Sound('../assets/bgm/' + url)
        self.channel3.queue(sound)

    #鸣人特效##############################################################################################
    def sub_insert_action_num(self):
        self.insert_action_num = self.insert_action_num - 1
        print('self.insert_action_num:' + str(self.insert_action_num))
    
    '''
    #前面的鸣人走到一定距离了后面的鸣人才跟着走
    def update_luo_xuan_wan(self, image_index):
        if image_index == 10:
            forward_left_padding = self.list_naruto[self.insert_action_num - 1].get_left_padding()
            back_left_padding = self.list_naruto[self.insert_action_num - 2].get_left_padding()
            if forward_left_padding - back_left_padding > 200:
                self.insert_action_num = self.insert_action_num - 1'''
        
    
    def cast_voice_luo_xuan_wan(self, image_index):
        if image_index == 15:
            self.play_sound('打中别人.wav')
        elif image_index == 23:
            self.play_sound('影分身消失.wav')
            
    
    def cast_voice_luo_xuan_wan_once(self, image_index):
        if image_index == 2:
            self.play_sound('通灵出来的声音.wav')
        elif image_index == 5:
            self.play_sound('螺旋丸声音.wav')
        elif image_index == 10:
            self.play_sound('影分身消失.wav')
        elif image_index == 14:
            if self.list_naruto[len(self.list_naruto) - 1].speed != 40:
                self.play_sound('开了惊门快速跑.wav')
            self.list_naruto[len(self.list_naruto) - 1].speed = 40
    
    def end_luo_xuan_wan(self):
        self.list_naruto[self.insert_action_num - 2].speed = 40
        self.insert_action_num = self.insert_action_num - 1
        self.play_sound('开了惊门快速跑.wav')
    
    def multi_shadow_separation_end(self):
        #self.list_naruto[self.insert_action_num - 1].change_to_status('螺旋丸')
        #self.list_naruto[self.insert_action_num - 1].character['naruto/螺旋丸'].append_end_update_function(self.sub_insert_action_num)
        #if self.insert_action_num > 1:
        #    self.list_naruto[self.insert_action_num - 1].character['naruto/螺旋丸'].append_update_function(self.update_luo_xuan_wan)
        #for i in range(len(self.list_naruto) - 1):
        #    self.list_naruto[i].character['naruto/螺旋丸'].append_update_function(self.list_naruto[i].update_stop_flush)
            
        for i in range(len(self.list_naruto) - 2):
            self.list_naruto[i].speed = 9
            
        for i in range(len(self.list_naruto)):
            self.list_naruto[i].change_to_status('螺旋丸')
            #self.list_naruto[i].character['naruto/螺旋丸'].append_update_function(self.update_luo_xuan_wan)
            self.list_naruto[i].character['naruto/螺旋丸'].append_update_function(self.cast_voice_luo_xuan_wan)
            if i != 0:
                self.list_naruto[i].character['naruto/螺旋丸'].append_end_update_function(self.end_luo_xuan_wan)
        self.list_naruto[0].character['naruto/螺旋丸'].append_update_function(self.cast_voice_luo_xuan_wan_once)
            
    def multi_shadow_separation_update(self, image_index):
        if image_index % 5 == 0 and image_index < 62 and image_index > 9:
            self.saske_style.change_to_houyang()
        if image_index != 0 and image_index < 51 and image_index%5 == 0:
            self.play_sound('yun_beng.wav')
        
    def end_update_fenshen(self):
        print("6个放完了，接下来是多重影分身")
        
        naruto = NarutoStyle(self.sprite_group, situation_flag = 3)
        naruto.add_to_sprite_group()
        naruto.set_key_controller(self.key_controller)
        naruto.set_left_padding( self.saske_style.get_left_padding())
        naruto.set_top_padding( self.saske_style.get_top_padding() + 105)
        naruto.character['naruto/multi_shadow_separation'].append_update_function(self.multi_shadow_separation_update)
        
        self.list_naruto[self.insert_action_num - 1].set_current_sprite_stop_flush()
        self.list_naruto[self.insert_action_num - 1].set_saske(self.saske_style)
        for i in range(len(self.list_naruto) - 1):
            self.list_naruto[i].change_to_status_for_fenshen('idle')
            self.list_naruto[i].set_saske(self.saske_style)
            self.naruto_style.change_to_status('idle')
        naruto.character["naruto/multi_shadow_separation"].append_end_update_function(self.multi_shadow_separation_end)
        
    def update_yi_ge_fen_shen(self, image_index):
        if image_index == 4:
            #self.list_naruto[self.insert_action_num - 1].change_to_status_idle() 
            self.lianxufenshen()
        elif image_index == 1:
            self.play_sound('通灵出来的声音.wav')
        
    def lianxufenshen(self):
        if self.insert_action_num > self.fenshen_num - 1:
            self.list_naruto[self.insert_action_num - 1].clear_end_update_yigefenshen()
            #self.list_naruto[self.insert_action_num - 1].clear_end_update_jieyin_by_index(1)
            self.list_naruto[self.insert_action_num - 1].character["naruto/一个分身"].clear_end_update_function()
            self.list_naruto[self.insert_action_num - 1].change_to_status('结印')
            self.list_naruto[self.insert_action_num - 1].append_jieyin_end_func(self.end_update_fenshen)
            return
        #if self.insert_action_num != 0:
            #self.list_naruto[self.insert_action_num - 1].clear_end_update_yigefenshen()
            #self.list_naruto[self.insert_action_num - 1].clear_end_update_jieyin_by_index(1)
            #self.list_naruto[self.insert_action_num - 1].change_to_status('一个分身')
        
        self.list_naruto[self.insert_action_num].revert_top_padding()
        self.list_naruto[self.insert_action_num].change_to_status('一个分身')
        #self.list_naruto[self.insert_action_num].character["naruto/一个分身"].append_end_update_function(self.update_yi_ge_fen_shen)
        self.list_naruto[self.insert_action_num].character["naruto/一个分身"].append_update_function(self.update_yi_ge_fen_shen)
        self.list_naruto[self.insert_action_num].character["naruto/一个分身"].append_end_update_function(self.list_naruto[self.insert_action_num].change_to_status_idle)
        #分身之后不结印，只有最后一个结印搞出一大堆分身
        #self.list_naruto[self.insert_action_num].append_end_update_yigefenshen()#影分身结束之后去结印
        #不再使用结印的末尾去分身，而是分身的过程再分身
        #self.list_naruto[self.insert_action_num].append_jieyin_end_func(self.lianxufenshen)
        self.insert_action_num = self.insert_action_num + 1
        
            
    def add_fenshen_to_group(self):
        self.fenshen_num = 4
        for i in range(self.fenshen_num):
            naruto = NarutoStyle(self.sprite_group, situation_flag = 2)
            naruto.add_to_sprite_group()
            naruto.set_key_controller(self.key_controller)
            naruto.change_to_status('idle')
            naruto.set_left_padding(self.naruto_style.get_left_padding() + (len(self.list_naruto) + 1) * 150)
            self.list_naruto.append(naruto)
            naruto.set_top_padding(1000)
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
            #self.play_sound('打中别人.wav') #须左结束的时候也放一下音效
            self.play_sound('须左消失.wav')
            #self.saske_xuzuo_jian.character['saske/须左的箭'].image_index = 14
        else:
            self.saske_xuzuo_jian.character['saske/须左的箭'].set_left_padding(left_padding - 120)
    
    def xuzuo_update(self, image_index):
        if image_index == 12:
            self.saske_xuzuo_jian = SaskeStyle(self.sprite_group, situation_flag = 3)
            self.saske_xuzuo_jian.set_left_padding(self.saske_style.get_left_padding() - 200)
            self.saske_xuzuo_jian.set_top_padding(self.saske_style.get_top_padding() - 30)
            self.saske_xuzuo_jian.character['saske/须左的箭'].append_update_function(self.xuzuo_jian_update)
        elif image_index == 8:
            self.play_sound('搭箭.wav')
        elif image_index == 11:
            self.play_sound_queue('射出箭.wav')
        elif image_index == 14:
            self.saske_xuzuo.character['saske/须左'].image_index = 13
            
    def xu_zuo(self):
        self.saske_xielunyan.remove_current_sprite_from_sprite_group()
        self.saske_xuzuo = SaskeStyle(self.sprite_group, situation_flag = 2)
        self.saske_xuzuo.set_left_padding(self.saske_style.get_left_padding())
        self.saske_xuzuo.set_top_padding(self.saske_style.get_top_padding() + 20)
        self.saske_xuzuo.character['saske/须左'].append_update_function(self.xuzuo_update)
        self.saske_xuzuo.character['saske/须左'].append_end_update_function(self.saske_xuzuo.remove_current_sprite_from_sprite_group)
        self.play_sound('须左.wav')
        
    def xie_lun_yan(self):
        self.saske_xielunyan = SaskeStyle(self.sprite_group, situation_flag = 4)
        self.play_sound('写轮眼.wav')
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
    
    def end_update_shui_dun_te_xiao(self):
        self.ka_ka_xi_shui_dun_te_xiao.remove_current_sprite_from_sprite_group()
    
    def shui_long_dan_zhi_shu_update_function(self, image_index):
        left_padding = self.ka_ka_xi_shui_long_dan_zhi_shu.get_left_padding()
        self.ka_ka_xi_shui_long_dan_zhi_shu.set_left_padding(left_padding - 20) #12 20
        if image_index == 20:
            self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].image_index = 12
        elif image_index == 21:
            self.ka_ka_xi_shui_dun_te_xiao = KakaxiStyle(self.sprite_group, situation_flag = 4)
            self.ka_ka_xi_shui_dun_te_xiao.set_left_padding(150)
            self.ka_ka_xi_shui_dun_te_xiao.set_top_padding(self.ka_ka_xi.get_top_padding() + 10)
            self.ka_ka_xi_shui_dun_te_xiao.character['kakaxi/水龙弹打中特效'].append_end_update_function(self.end_update_shui_dun_te_xiao)
        elif image_index > 21 and image_index < 27:
            self.ka_ka_xi_shui_dun_te_xiao.character['kakaxi/水龙弹打中特效'].image_index = 0
            
        if left_padding == 300: #这个数值在最后联调的时候需要改动-----------------------------------------
            self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].image_index = 20
    
    def remove_shui_long_dan_zhi_shu(self):
        self.ka_ka_xi_shui_long_dan_zhi_shu.remove_current_sprite_from_sprite_group()
    
    def release_shui_long_dan_zhi_shu(self):
        self.ka_ka_xi_shui_long_dan_zhi_shu = KakaxiStyle(self.sprite_group, situation_flag = 5)
        self.ka_ka_xi_shui_long_dan_zhi_shu.set_left_padding(self.saske_style.get_left_padding() + 80)
        self.ka_ka_xi_shui_long_dan_zhi_shu.set_top_padding(self.ka_ka_xi.get_top_padding() + 40)
        self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].append_update_function(self.shui_long_dan_zhi_shu_update_function)
        self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].append_end_update_function(self.ka_ka_xi_to_idle)
        self.ka_ka_xi_shui_long_dan_zhi_shu.character['kakaxi/水龙弹之术'].append_end_update_function(self.remove_shui_long_dan_zhi_shu)
        self.ka_ka_xi.character['kakaxi/站直'].clear_end_update_function_by_index(0)
    
    def end_update_zhan_zhi(self):
        #if self.wo_ai_luo.character['woailuo/举手握拳'].image_index == 0:
        self.ka_ka_xi.character['kakaxi/站直'].image_index = len(self.ka_ka_xi.character['kakaxi/站直'].images) - 1
    
    def shui_long_dan_zhi_shu(self):
        self.ka_ka_xi.change_to_status('站直')
        self.ka_ka_xi.character['kakaxi/站直'].append_end_update_function(self.release_shui_long_dan_zhi_shu)
        self.ka_ka_xi.character['kakaxi/站直'].append_end_update_function(self.end_update_zhan_zhi)
        
    def generate_shou_li_jian(self, left_padding, top_padding):
        self.ka_ka_xi_shou_li_jian = KakaxiStyle(self.sprite_group, situation_flag = 3)
        self.ka_ka_xi_shou_li_jian.set_left_padding(left_padding)
        self.ka_ka_xi_shou_li_jian.set_top_padding(top_padding)  #手里剑飞到600 400的地方
        self.ka_ka_xi_shou_li_jian.character['kakaxi/手里剑'].append_update_function(self.shou_li_jian_fly)
        
    def end_update_shen_wei_reverse(self):
        self.ka_ka_xi_shen_wei_reverse.remove_current_sprite_from_sprite_group()
        self.ka_ka_xi.revert_top_padding()
        self.ka_ka_xi.change_to_status('idle')
    
    def shou_li_jian_fly(self, image_index):
        if image_index == 0:
            self.ka_ka_xi_shou_li_jian.character['kakaxi/手里剑'].image_index = 1
        #20 15
        left_padding = self.ka_ka_xi_shou_li_jian.get_left_padding() - 12
        top_padding = self.ka_ka_xi_shou_li_jian.get_top_padding() + 9
        self.ka_ka_xi_shou_li_jian.set_left_padding(left_padding)
        self.ka_ka_xi_shou_li_jian.set_top_padding(top_padding)
        if left_padding < 600:
            self.ka_ka_xi_shou_li_jian.character['kakaxi/手里剑'].clear_update_function()
            #这里本来要插入打中人的特效什么的，被打中的人要后仰-----------------------------------------------
            self.ka_ka_xi_shou_li_jian.remove_current_sprite_from_sprite_group()
            self.shou_li_jian_num = self.shou_li_jian_num - 1
            if self.shou_li_jian_num == 0:
                #倒序的神威
                self.ka_ka_xi_shen_wei_reverse = KakaxiStyle(self.sprite_group, situation_flag = 6)
                self.ka_ka_xi_shen_wei_reverse.set_left_padding(self.ka_ka_xi.get_left_padding())
                self.ka_ka_xi_shen_wei_reverse.set_top_padding(self.ka_ka_xi.get_reverse_top_padding() + 20)
                self.ka_ka_xi_shen_wei_reverse.character['kakaxi/神威倒序'].append_end_update_function(self.end_update_shen_wei_reverse)
            else:
                #这里的手里剑位置变更后面再调
                self.generate_shou_li_jian(800 + self.shou_li_jian_num * 48, 250 + self.shou_li_jian_num * 36)
                 
    def end_update_shen_wei(self):
        self.shou_li_jian_num = 4
        self.ka_ka_xi_shen_wei.remove_current_sprite_from_sprite_group()
        self.ka_ka_xi.set_top_padding(1000)
        self.generate_shou_li_jian(800, 250)
        
    def shen_wei(self):
        self.ka_ka_xi.change_to_status('捂眼')
        self.ka_ka_xi_shen_wei = KakaxiStyle(self.sprite_group, situation_flag = 2)
        self.ka_ka_xi_shen_wei.set_left_padding(self.ka_ka_xi.get_left_padding())
        self.ka_ka_xi_shen_wei.set_top_padding(self.ka_ka_xi.get_top_padding() + 20)
        self.ka_ka_xi_shen_wei.character['kakaxi/神威'].append_end_update_function(self.end_update_shen_wei)
    #神威的特效暂时定为卡卡西通过神威隐身，然后我爱罗被四面八方的手里剑转一圈受伤，最后卡卡西出现在原来的地方
    #卡卡西特效##############################################################################################
    
    
    #自来也特效##############################################################################################
    
    def zi_lai_ye_to_idle(self):
        self.zi_lai_ye.change_to_status('idle')
        
    def add_zi_lai_ye(self):
        self.naruto_style.remove_current_sprite_from_sprite_group()
        self.zi_lai_ye = ZilaiyeStyle(self.sprite_group)
        self.zi_lai_ye.set_left_padding(self.naruto_style.get_left_padding())
        self.zi_lai_ye.change_to_status('出现')
        self.zi_lai_ye.character['zilaiye/出现'].append_end_update_function(self.zi_lai_ye_to_idle)
        
    def hama_to_idle(self):
        self.zi_lai_ye.revert_top_padding()
        self.zi_lai_ye_tong_ling.set_current_sprite_stop_flush()
        self.zi_lai_ye.set_top_padding(self.zi_lai_ye.get_top_padding() - 45)
        self.zi_lai_ye.change_to_status('出现')
        
    def tong_ling(self):
        self.zi_lai_ye_tong_ling = ZilaiyeStyle(self.sprite_group, situation_flag = 2)
        self.zi_lai_ye_tong_ling.set_left_padding(self.zi_lai_ye.get_left_padding())
        self.zi_lai_ye_tong_ling.set_top_padding(self.zi_lai_ye.get_top_padding())
        self.zi_lai_ye_tong_ling.character['zilaiye/蛤蟆出现'].append_end_update_function(self.hama_to_idle)
        self.zi_lai_ye.change_to_status('idle')
        self.zi_lai_ye.set_top_padding(1000)
        
    def change_to_tong_ling(self):
        self.zi_lai_ye.change_to_status('下蹲通灵')
        self.zi_lai_ye.character['zilaiye/下蹲通灵'].append_end_update_function(self.tong_ling)
        
    def huo_yan_update_function(self, image_index):
        print('huo yan image_index:' + str(image_index))
        if image_index == 19:
            self.zi_lai_ye_huo_you.character['zilaiye/火油'].clear_update_function() 
        
    def remove_huo_yan(self):
        self.huo_yan.remove_current_sprite_from_sprite_group()
        
    def update_huo_you_function(self, image_index):
        print('aaaa' + str(image_index))
        if image_index == 1:
            self.huo_yan = ZilaiyeStyle(self.sprite_group, situation_flag = 4)
            self.huo_yan.set_left_padding(self.zi_lai_ye.get_left_padding() + 690)
            self.huo_yan.set_top_padding(self.zi_lai_ye.get_top_padding() + 20)
            self.huo_yan.character['zilaiye/长条火焰'].append_update_function(self.huo_yan_update_function)
            self.huo_yan.character['zilaiye/长条火焰'].append_end_update_function(self.remove_huo_yan)
        if image_index == 4:
           self.zi_lai_ye_huo_you.character['zilaiye/火油'].image_index = 3 
        
    def remove_huo_you(self):
        self.zi_lai_ye_huo_you.remove_current_sprite_from_sprite_group()
        
    def show_fier(self):
        self.zi_lai_ye_tong_ling.set_current_sprite_stop_flush()
        self.zi_lai_ye_huo_you = ZilaiyeStyle(self.sprite_group, situation_flag = 3)
        self.zi_lai_ye_huo_you.set_left_padding(self.zi_lai_ye.get_left_padding() + 105)
        self.zi_lai_ye_huo_you.set_top_padding(self.zi_lai_ye.get_top_padding() + 10)
        self.zi_lai_ye_huo_you.character['zilaiye/火油'].append_update_function(self.update_huo_you_function)
        self.zi_lai_ye_huo_you.character['zilaiye/火油'].append_end_update_function(self.remove_huo_you)
    
    def begin_fire(self):
        self.zi_lai_ye.change_to_status('捂嘴喷火')
        self.zi_lai_ye.set_current_sprite_stop_flush()
        self.zi_lai_ye_tong_ling.change_to_status('蛤蟆喷火')
        self.zi_lai_ye_tong_ling.character['zilaiye/蛤蟆喷火'].append_end_update_function(self.show_fier)
    #自来也特效##############################################################################################
    
    
    
    #佩恩特效###############################################################################################
    def pain_to_idle(self):
        self.pain.change_to_status('idle')
    
    def remove_bao_zha(self):
        self.pain_di_bao_tian_xing_qiu.remove_current_sprite_from_sprite_group()
        self.pain.change_to_status('idle')
    
    def di_bao_tian_xing_bao_zha(self):
        self.pain_di_bao_tian_xing_qiu.change_to_status('地爆天星的爆炸')
        self.pain_di_bao_tian_xing_qiu.set_top_padding(350)
        self.pain_di_bao_tian_xing_qiu.character['pain/地爆天星的爆炸'].append_end_update_function(self.remove_bao_zha) 
    
    #def end_chu_xian_ge_qiu(self):
    #    self.pain_di_bao_tian_xing_qiu.change_to_status('地爆天星旋转')
    #    self.pain_di_bao_tian_xing_qiu.character['pain/地爆天星旋转'].append_end_update_function(self.di_bao_tian_xing_bao_zha) 
    
    def chu_xian_ge_qiu(self):
        self.pain_di_bao_tian_xing_lun_hui_yan.remove_current_sprite_from_sprite_group()
        self.pain_di_bao_tian_xing_qiu = PainStyle(self.sprite_group, situation_flag = 3)#.character['pain/地爆天星的球'].append_update_function(self.hama_to_idle)
        self.pain_di_bao_tian_xing_qiu.set_left_padding(600)
        self.pain_di_bao_tian_xing_qiu.set_top_padding(400)
        self.pain_di_bao_tian_xing_qiu.character['pain/地爆天星的球'].append_end_update_function(self.di_bao_tian_xing_bao_zha)
        self.update_screen = self.update_screen_with_white
    
    def draw_screen_with_black(self):
        self.screen.fill(Color.BLACK)
    
    def end_di_bao_tian_xing_jie_ying(self):
        self.pain.set_current_sprite_stop_flush()
        self.pain_di_bao_tian_xing_lun_hui_yan = PainStyle(self.sprite_group, situation_flag = 2)
        self.pain_di_bao_tian_xing_lun_hui_yan.set_left_padding(600)
        self.pain_di_bao_tian_xing_lun_hui_yan.set_top_padding(250)
        self.pain_di_bao_tian_xing_lun_hui_yan.character['pain/轮回眼打开'].append_end_update_function(self.chu_xian_ge_qiu)
        self.update_screen = self.draw_screen_with_black
        
    def release_di_bao_tian_xing(self):
        self.pain.change_to_status('地爆天星结印')
        self.pain.character['pain/地爆天星结印'].append_end_update_function(self.end_di_bao_tian_xing_jie_ying)
        
    def pain_to_liu_dao_san(self):
        self.pain.change_to_status('六道散')
        self.pain.character['pain/六道散'].append_end_update_function(self.pain_to_idle)
        
    def add_pain(self):
        self.saske_style.remove_current_sprite_from_sprite_group()
        self.pain = PainStyle(self.sprite_group)
        self.pain.set_left_padding(self.saske_style.get_left_padding())
        self.pain.set_top_padding(self.saske_style.get_top_padding())
        self.pain.change_to_status('出场')
        self.pain.character['pain/出场'].append_end_update_function(self.pain_to_liu_dao_san)
        
    def xi_zhu_zi_lai_ye(self):
        self.pain.change_to_status('地爆天星举手')
    
    #对手在哪里，佩恩的球就在哪里形成
    #佩恩特效###############################################################################################
    
    def test_cast_sound(self):
        self.play_sound_queue('爆炸.wav')
        self.play_sound_queue('射出箭.wav')
        self.play_sound_queue('搭箭.wav')
        
    
    def update_screen_with_white(self):
        self.screen.fill(Color.WHITE)
    
    def handle_key_event(self):
        if self.key_controller.key_m:
            self.chu_fa_fen_shen()
        elif self.key_controller.key_w:
            self.xie_lun_yan()
            #self.sa_pu_song_zang()
            #self.sa_fu_jiu()
            #self.shui_long_dan_zhi_shu()
            #self.shen_wei()
            #self.change_to_tong_ling()
            #self.release_di_bao_tian_xing()
        elif self.key_controller.key_a:
            #self.add_wo_ai_luo()
            #self.add_zi_lai_ye()
            #self.add_pain()
            self.test_cast_sound()
        elif self.key_controller.key_s:
            #self.change_to_status('naruto/idle')
            #self.wo_ai_luo_sa_fu_jiu.character['woailuo/砂缚柩'].clear_update_function()
            #self.begin_fire()
            self.xi_zhu_zi_lai_ye()
    
    def set_key_controller(self, key_controller):
        self.key_controller = key_controller
        
    def set_screen(self, screen):
        self.screen = screen
        
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
    
    def cast_dao_di_voice(self, image_index):
        if image_index == 7:
            self.play_sound('倒地上.wav')
    
    def saske_be_hit_far_away(self):
        self.saske_style.change_to_status('倒在地上')
        self.current_attack_player = 'saske'
        self.current_attacked_player = 'naruto'
        self.saske_style.character['saske/倒在地上'].append_update_function(self.cast_dao_di_voice)
    
    def naruto_be_hit_far_away(self):
        self.naruto_style.change_to_status('death')
        self.current_attack_player = 'naruto'
        self.current_attacked_player = 'saske'
        self.naruto_style.character['naruto/death'].append_update_function(self.cast_dao_di_voice)
        
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
            #return True
            if self.insert_action_num == 0 and self.sleep(1000):
                #self.saske_style.change_to_status('站起来')
                self.naruto_style.change_to_status('run')
                self.saske_style.change_to_status('run')

        return False
    
    def play_yong_tou_da(self, image_index):  #其实这些声音应该挂在具体的玩家身上
        if image_index == 3:
            self.play_sound('打中别人.wav')
    
    def play_hui_tui_by_index(self, image_index):
        if image_index == 7:
            self.play_sound('打中别人.wav')
    
    def play_hui_tui(self):
        self.play_sound('挥拳.wav')
    
    def naruto_attack_saske(self):
        #在下面添加判断的逻辑，是在跑还是在干什么，根据逻辑确定两者之间的位置以及是否要切换
        if not self.idle_begin_run() and self.naruto_style.status == 'run' and self.saske_style.status == 'run':
            #首先跑一下看看是不是idle3秒之后开始相对跑近     然后下面需要判断一下是不是距离足够进了
            #print('padding:' + str(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()))
            if(self.saske_style.get_left_padding() - self.naruto_style.get_left_padding()) < 84:
                self.play_sound('挥拳.wav')
                self.naruto_style.change_to_status('挥拳')
                self.naruto_style.append_end_update_huiquan(self.saske_style.change_to_houyang())
                self.naruto_style.append_end_update_yongtouda(self.saske_style.change_to_houyang())
                self.naruto_style.append_end_update_fanjiaoti(self.saske_be_hit_far_away)
                
                self.naruto_style.character["naruto/用头打"].append_update_function(self.play_yong_tou_da)
                
                self.naruto_style.character["naruto/反脚踢"].append_update_function(self.play_hui_tui_by_index)
        #后仰的时候，先顺着波，然后倒着播，中途被打了再顺着播，然后倒着播，播完了就变成idle了
    
    def cast_dao_kan(self, image_index):
        if image_index == 3:
            self.play_sound('刀砍.wav')
            
    def cast_hui_quan(self, image_index):
        if image_index == 3:
            self.play_sound('打中别人.wav')
            
    def cast_liang_dao(self, image_index):
        if image_index == 2 or image_index == 5:
            self.play_sound('刀砍.wav')
            
    def cast_xiang_shang_yi_jiao(self, image_index):
        if image_index == 3:
            self.play_sound('打得重.wav')
            
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
                self.saske_style.character['saske/挥刀'].append_update_function(self.cast_dao_kan)
                self.saske_style.character['saske/挥拳'].append_update_function(self.cast_hui_quan)
                self.saske_style.character['saske/挥两刀'].append_update_function(self.cast_liang_dao)
                self.saske_style.character['saske/向上一脚'].append_update_function(self.cast_xiang_shang_yi_jiao)
    
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
                
                #手动添加一下，下面这些函数以后是要删除掉的
                self.naruto_end_update_seyouzhishu()
                self.saske_end_update_kai_pian_hui_shou()
                
                #self.naruto_style.append_end_update_seyouzhishu(self.naruto_end_update_seyouzhishu)
                #self.saske_style.append_end_update_kai_pian_hui_shou(self.saske_end_update_kai_pian_hui_shou)
    
    #看看有没有用python来裁剪图片的
    def update(self):
        if self.current_attack_player == 'naruto' and self.current_attacked_player == 'saske':
            self.naruto_attack_saske()
        elif self.current_attack_player == 'saske' and self.current_attacked_player == 'naruto':
            self.saske_attack_naruto()