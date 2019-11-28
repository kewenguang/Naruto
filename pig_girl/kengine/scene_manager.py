'''
Created on 2019年11月28日

@author: kewenguang
'''



class SceneManager():
    def __init__(self):
        self.scenes = {}
        
        
    def add_scene(self, scene):
        self.scenes[scene.name] = scene
       
    def remove_scene(self, scene_name):
        self.scenes.pop(scene_name)
        
    def loop(self):
        self.current_scene.loop()
        
    def change_to_scene_by_name(self, scene_name):
        self.remove_scene(self.current_scene.name)
        self.current_scene = self.scene[scene_name]
        
    def change_to_scene_by_name_with_no_remove(self, scene_name):
        self.current_scene = self.scene[scene_name]
        