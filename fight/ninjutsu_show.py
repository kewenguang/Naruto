'''
Created on 2019年8月11日

@author: kewenguang
'''

from __future__ import division
from fight.resource_load import Color
from fight.resource_load import GameCommonData
from fight.resource_load import key_controller
import pygame

from fight.logic_controller import Controller
###############################
## to be placed in "constant.py" later
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

###############################

###############################
## to placed in "__init__.py" later
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((GameCommonData.WIDTH, GameCommonData.HEIGHT))
pygame.display.set_caption("Naruto")

all_sprites = pygame.sprite.Group()

#all_sprites.has_internal(sprite)

logic_controller = Controller(all_sprites)
logic_controller.set_key_controller(key_controller)
#logic_controller.set_sprite_group(all_sprites)
logic_controller.ready()

running = True
while running:
    
    #GameCommonData.tick(FPS)
    GameCommonData.tick(10)
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            key_controller.key_response(event.key)
                
    screen.fill(Color.WHITE)
    #background_rect = multi_shadow_separation_images[0].get_rect()
    #screen.blit(multi_shadow_separation_images[0], background_rect)
    
    logic_controller.update_function()
    
    all_sprites.update()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    key_controller.key_revert()
pygame.quit()