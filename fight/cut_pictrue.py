'''
Created on 2019年9月26日

@author: kewenguang
'''
from PIL import Image
import os
import sys
#input_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/佐助小时候/images/开篇挥手裁剪'
#input_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/佐助小时候/sprites/idle'
#output_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/佐助小时候/images/裁剪之后的'

#input_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/色诱之术剪切前'
#output_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/色诱之术剪切后'

input_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/裁剪之前的图片'
output_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/裁剪之后的图片'
def change_pic_width():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        cropped = img.crop((0, 0, 60, 66)) 
        cropped.save(output_dir + "/" + filename)

#change_pic_width()
#sys.exit()
        
def change_pic_height():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        cropped = img.crop((0, 0, 170, 85)) 
        cropped.save(output_dir + "/" + filename)
        
def change_pic_color():
    for filename in os.listdir(input_dir):
        i = 1
        j = 1
        img = Image.open(input_dir + "/" + filename)#读取系统的内照片
        print (img.size)#打印图片大小
        
        print("img.getpixel((0,0))")
        print (img.getpixel((0, 0)))
        print("img.getpixel((0,0))")
        
        width = img.size[0]#长度
        height = img.size[1]#宽度
        for i in range(0,width):#遍历所有长度的点
          for j in range(0,height):#遍历所有宽度的点
            data = (img.getpixel((i,j)))#打印该图片的所有点
            #print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            #print (data[0])#打印RGBA的r值
            #if data[0] == 159 and data[1] == 186 and data[2] == 193 and data[3] == 255:
            #    img.putpixel((i,j),(255, 255, 255, 0))
            img.putpixel((i,j),(255, 255, 255, 0))
            #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #  img.putpixel((i,j),(234, 53, 57, 255))#则这些像素点的颜色改成大红色
        
        img = img.convert("RGB")#把图片强制转成RGB
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片

change_pic_color()
sys.exit()

def change_pic_color_in_width():
    for filename in os.listdir(input_dir):
        i = 1
        j = 1
        img = Image.open(input_dir + "/" + filename)#读取系统的内照片
        print (img.size)#打印图片大小
        
        print("img.getpixel((0,0))")
        print (img.getpixel((0, 0)))
        print("img.getpixel((0,0))")
        
        width = img.size[0]#长度
        height = img.size[1]#宽度
        for i in range(0,width):#遍历所有长度的点
          for j in range(0,height):#遍历所有宽度的点
            if i >= 100:
                data = (img.getpixel((i,j)))#打印该图片的所有点
                #print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
                #print (data[0])#打印RGBA的r值
                img.putpixel((i,j),(255, 255, 255, 0))
            #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #  img.putpixel((i,j),(234, 53, 57, 255))#则这些像素点的颜色改成大红色
        
        img = img.convert("RGB")#把图片强制转成RGB
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片

one_pictrue_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/Naruto'
another_pic_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/云朵'
output_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/叠加之后的图片'

def add_one_pictrue_to_another():
    one_pictrue_img = Image.open(one_pictrue_dir + "/" + '194.png')
    print (one_pictrue_img.size)
    for filename in os.listdir(another_pic_dir):
        i = 1
        j = 1
        img = Image.open(another_pic_dir + "/" + filename)#读取系统的内照片
        print (img.size)#打印图片大小
        
        width = img.size[0]#长度
        print('img.size[0]:' + str(img.size[0]))
        print('img.size[1]:' + str(img.size[1]))
        
        left_pix = int(width/2 - one_pictrue_img.size[0]/2)
        right_pix = int(width/2 + one_pictrue_img.size[0]/2)
        
        data_left_top = img.getpixel((0, 0))
        print('data_left_top:' + str(data_left_top))
        for i in range(left_pix, right_pix, 1):#遍历所有长度的点
          for j in range(0, one_pictrue_img.size[1]):#遍历所有宽度的点
            data = (img.getpixel((i, j+10)))#加10是为了被贴上去的图片整体下移10个像素
            #print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            #print (data[0])#打印RGBA的r值
            if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2]:
                data_added = one_pictrue_img.getpixel((i-left_pix, j))
                img.putpixel((i,j+10),(data_added[0], data_added[1], data_added[2], data_added[3]))
            #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #  img.putpixel((i,j),(234, 53, 57, 255))#则这些像素点的颜色改成大红色
        
        img = img.convert("RGBA")#把图片强制转成RGBA
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片


one_pictrue_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/裁剪之前的图片1'
output_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/裁剪之后的图片1'
def add_one_pictrue_to_another_white_background():
    one_pictrue_img = Image.open(one_pictrue_dir + "/" + '194.png')
    print (one_pictrue_img.size)
    for filename in os.listdir(another_pic_dir):
        i = 1
        j = 1
        img = Image.open(another_pic_dir + "/" + filename)#读取系统的内照片
        print (img.size)#打印图片大小
        
        width = img.size[0]#长度
        print('img.size[0]:' + str(img.size[0]))
        print('img.size[1]:' + str(img.size[1]))
        
        left_pix = int(width/2 - one_pictrue_img.size[0]/2)
        right_pix = int(width/2 + one_pictrue_img.size[0]/2)
        
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                img.putpixel((i,j),(255, 255, 255, 255))
                
        data_left_top = one_pictrue_img.getpixel((0, 0))
        for i in range(one_pictrue_img.size[0]):
            for j in range(one_pictrue_img.size[1]):
                data = one_pictrue_img.getpixel((i, j))
                if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2]:
                    one_pictrue_img.putpixel((i,j),(255, 255, 255, 255))
        
        data_left_top = img.getpixel((0, 0))
        print('data_left_top:' + str(data_left_top))
        for i in range(left_pix, right_pix, 1):#遍历所有长度的点
          for j in range(0, one_pictrue_img.size[1]):#遍历所有宽度的点
            data = (img.getpixel((i, j+10)))#加10是为了被贴上去的图片整体下移10个像素
            #print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            #print (data[0])#打印RGBA的r值
            if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2]:
                data_added = one_pictrue_img.getpixel((i-left_pix, j))
                img.putpixel((i,j+10),(data_added[0], data_added[1], data_added[2], data_added[3]))
            #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #  img.putpixel((i,j),(234, 53, 57, 255))#则这些像素点的颜色改成大红色
        
        img = img.convert("RGBA")#把图片强制转成RGBA
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片
        break
        
add_one_pictrue_to_another_white_background()