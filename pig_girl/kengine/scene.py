'''
Created on 2019年11月28日

@author: kewenguang
'''
#经过试验，子类没有的方法会到父类里面找相关的方法，子类有的会优先调用子类的方法
#一个list和map是可以放不同类型的value的，为多态做好了准备
#
import pygame

class Scene():
    
    def __init__(self):
        self.loop = self.start
        self.sprites = pygame.sprite.Group()
        
    def start(self):
        raise NotImplementedError('子类中必须实现start方法')
    
    def update(self):
        raise NotImplementedError('子类中必须实现update方法')
    
    #每个场景里面的人物有一些，怎么加到这个场景中来？？
    #看看某个具体的人物代码，看看有什么可以让你抽取的以及logic_controller
    
    #人物应该是可以通过配置一下url有哪些就可以配出来的
    