'''
Created on 2019年12月10日

@author: kewenguang
'''
import sys
sys.path.append('../')

import pygame

from kengine.scene_manager import SceneManager

from feng_mian_scene import FengmianScene
from begin_girl_scene import BeginGirlScene

running = True

####################################
scene_manager = SceneManager()
#begin_girl_scene = BeginGirlScene()
#scene_manager.add_scene(begin_girl_scene)
feng_mian_scene = FengmianScene()
scene_manager.add_scene(feng_mian_scene)
####################################
#scene_manager.change_to_scene_by_name_with_no_remove('少女变身')
#为了调试界面，直接使用把界面改到封面
scene_manager.change_to_scene_by_name_with_no_remove('封面')

pygame.display.set_caption("pig girl")

#有哪些游戏场景可以在这里加载

while running:
    #那个休眠一段时间的不应该放在这里来，而是每个游戏人物的换帧有自己的休息时间才对
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    scene_manager.loop()
    pygame.display.flip()
pygame.quit()
