'''
Created on 2019年12月16日

@author: kewenguang
'''
from pic import resize_one_pic

WIDTH = 1200
HEIGHT = 600

input_file_path_1 = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/pic/character/wendy/wendy_b.png'
output_file_path_bak = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/bak/wendy_b.png'

'''
resize_one_pic(width = WIDTH,
               height = HEIGHT,
               input_file_path = input_file_path_1, 
               output_file_path = output_file_path_bak)
 '''

'''
resize_one_pic(width = 120,#WIDTH,
               height = 120,
               input_file_path = input_file_path_1, 
               output_file_path = output_file_path_bak)
'''

input_dir_path_1 = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/pic/character/wendy/big_wendy_run/'
output_dir_path_bak = 'E:/javaWorkspace/Nanuto/pig_girl/logic_code/assert/bak/big_wendy_run/'

'''
from pic import resize_pic_in_dir
resize_pic_in_dir(width = WIDTH, 
                  height = HEIGHT, 
                  input_dir = input_dir_path_1, 
                  output_dir = output_dir_path_bak)
                  '''

'''
from pic import resize_pic_in_dir
resize_pic_in_dir(width = 90, 
                  height = 70, 
                  input_dir = input_dir_path_1, 
                  output_dir = output_dir_path_bak)
'''

from pic import resize_pic_in_dir_by_multiple
resize_pic_in_dir_by_multiple(1.5, 
                              input_dir = input_dir_path_1, 
                              output_dir = output_dir_path_bak)