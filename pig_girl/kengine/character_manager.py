'''
Created on 2019年12月28日

@author: kewenguang
'''
from character import Character

class CharacterManager():
    
    def __init__(self):
        self.characters = {}
        
    def add_character(self, character):
        self.characters[character.name] = character
        
    def remove_character_by_name(self, character_name):
        self.characters.pop(character_name)
        
    def remove_character(self, character):
        self.remove_character_by_name(character.name)
        
    def get_character(self, name):
        return self.characters[name]
    
    def get_characters(self):
        return self.characters