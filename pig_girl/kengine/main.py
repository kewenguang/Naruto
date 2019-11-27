'''
Created on 2019年11月27日

@author: kewenguang
'''
#关于场景可以这样设计：
#有一个scene_manager,里面有个map存放【场景名-场景】，然后场景里面又有start，update  
#scene_manager可以通过返回值来确定执行一次loop之后要不要切换场景，以及切换到哪个场景
#外面专门调用场景的loop循环，loop是个function，第一次是start，以后是update