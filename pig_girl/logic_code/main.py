'''
Created on 2019年12月10日

@author: kewenguang
'''
import sys
sys.path.append('../')

from kengine.scene_manager import SceneManager
import pygame

running = True

####################################
scene_manager = SceneManager()

####################################

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
