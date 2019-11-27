'''
Created on 2019年11月27日

@author: kewenguang
'''

import pygame

class Time():
    @staticmethod
    def tick(FPS):
        pygame.time.Clock().tick(FPS)