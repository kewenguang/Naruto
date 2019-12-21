'''
Created on 2019年12月16日

@author: kewenguang
'''
from pic import resize_one_pic

WIDTH = 1200
HEIGHT = 600

input_file_path_1 = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/pic/城堡背景.jpg'
output_file_path_bak = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/bak/城堡背景.jpg'

'''
resize_one_pic(width = WIDTH,
               height = HEIGHT,
               input_file_path = input_file_path_1, 
               output_file_path = output_file_path_bak)
'''

input_dir_path_1 = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/pic/mo_fa_bang'
output_dir_path_bak = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/bak/'

from pic import resize_pic_in_dir
resize_pic_in_dir(width = WIDTH, 
                  height = HEIGHT, 
                  input_dir = input_dir_path_1, 
                  output_dir = output_dir_path_bak)