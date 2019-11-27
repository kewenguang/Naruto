'''
Created on 2019年11月27日

@author: kewenguang
'''
class Windows():
    #窗体的宽高
    WIDTH = 1200
    HEIGHT = 600
    
    @staticmethod
    def SetWidth(width):
        Windows.WIDTH = width
        
    @staticmethod
    def SetHeight(height):
        Windows.HEIGHT = height