'''
Created on 2019年11月28日

@author: kewenguang
'''
#经过试验，子类没有的方法会到父类里面找相关的方法，子类有的会优先调用子类的方法
#一个list和map是可以放不同类型的value的，为多态做好了准备
#
import pygame

from core.color import WHITE
from character_manager import CharacterManager

class Scene():
    
    def __init__(self):
        pygame.init()
        self.loop = self.start
        #self.sprites = pygame.sprite.Group()
        self.next_scene_name = ''
        self.signal_to_upper = ''
        self.sprite_group = pygame.sprite.Group()
        self.character_manager = CharacterManager()
        self.text_list = []
    
    def update_background(self):
        #这里的screen属性在添加到screen_manager的时候会被设置
        self.screen.fill(WHITE)  
        
    def start(self):
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)  #scene_manager会赋予self.screen属性
        pygame.display.flip()
        
    def update(self):
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)  #scene_manager会赋予self.screen属性
        pygame.display.flip()
        
        #raise NotImplementedError('子类中必须实现update方法')
    def clear_character_signal(self):
        for value in self.character_manager.get_characters().values():
            value.signal_to_scene = ''
            
    def update_text(self):
        for item in self.text_list:
            self.screen.blit(item[0], item[1])
        
    def add_text(self, 
                  font='华文宋体',
                  size = 50, 
                  text = 'text', 
                  color = (0, 0, 0),
                  location = (0, 0) ):
        font_info = pygame.font.SysFont(font, size)
        text_info = font_info.render(text, 1, color)
        self.text_list.append((text_info, location))
        #常见字体如下:
        #['arial', 'arialblack', 'bahnschrift', 'calibri', 
        #'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 
        #'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 
        #'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 
        #'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 
        #'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 
        #'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 
        #'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 
        #'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'extra', 'bookantiqua', 'bookshelfsymbol7', 'century', 'centurygothic', 'msoutlook', 'msreferencesansserif', 'msreferencespecialty', 'wingdings2', 'wingdings3', '方正舒体', '方正姚体', '隶书', '幼圆', '华文彩云', '华文仿宋', '华文琥珀', '华文楷体', '华文隶书', '华文宋体', '华文细黑', '华文行楷', '华文新魏', '华文中宋', '方正兰亭超细黑简体', 'fzshuti', 'fzyaoti', 'stcaiyun', 'stfangsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'simsunfounderextended', 'bitstreamverasansmonooblique', 'bitstreamverasansmono', 'dejavusansmono', 'dejavusansmonooblique']

        
        
    #每个场景里面的人物有一些，怎么加到这个场景中来？？
    #看看某个具体的人物代码，看看有什么可以让你抽取的以及logic_controller
    
    #人物应该是可以通过配置一下url有哪些就可以配出来的
    