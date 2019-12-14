'''
Created on 2019年12月10日

@author: kewenguang
'''
from scene import Scene

class FengmianScene(Scene):
    
    #接下来需要搞的是这个场景
    #上背景图片，一个女孩的头像自底向上出现，然后是放“我有一支仙女棒，变大变小变漂亮”
    #喊声音的同时，也会有一只小猪从一边跑到另一边，然后发出鼻子的叫声”吭 吭“
    def start(self):
        print('游戏封面 loop为start()')
        self.loop = self.update
        
    def update(self):
        print('游戏封面 loop为update()')
        
    #先让它跑起来显示一个窗体先