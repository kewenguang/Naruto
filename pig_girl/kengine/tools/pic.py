'''
Created on 2019年12月16日

@author: kewenguang
'''
'''
此脚本功能一览
resize_pic_in_dir 修改一个文件夹下的所有图片的大小，并按原来的名字输出

resize_one_pic 修改一个图片的大小，input_file_path是输入的路径加文件名，
output_file_path输出的路径加文件名


'''

import os
from PIL import Image

def resize_pic_in_dir(width, height, input_dir, output_dir):
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        out = img.resize((width, height), Image.ANTIALIAS)
        out.save(output_dir + "/" + filename)
        
def resize_one_pic(width, height, input_file_path, output_file_path):
    img = Image.open(input_file_path)
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(output_file_path)
    