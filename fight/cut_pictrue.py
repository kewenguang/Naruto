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

prefix_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/'

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

#change_pic_color()
#sys.exit()

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
        
one_pictrue_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/叠加之前'
another_pic_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/叠加之后的图片'
yunduo_dir = 'E:/追捕/火影忍者模型/杂七杂八地搜集/2d资源/死神VS火影/反编译得到资源/鸣人/云朵'
def add_one_pictrue_to_another_with_anchor():
    one_pictrue_img = Image.open(one_pictrue_dir + "/" + '188.png')
    print (one_pictrue_img.size)
    yunduo1_img = Image.open(yunduo_dir + "/" + '210.png')
    yunduo2_img = Image.open(yunduo_dir + "/" + '226.png')
    
    start_left_padding = 85#93
    start_top_padding = 14#22
    data_left_top = yunduo1_img.getpixel((0, 0))
    for i in range(yunduo1_img.size[0]):
        for j in range(yunduo1_img.size[1]):
            data = (yunduo1_img.getpixel((i, j)))
            if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2] and data[3] == data_left_top[3]:
                continue
            one_pictrue_img.putpixel((start_left_padding + i, start_top_padding + j), (data[0], data[1], data[2], data[3]))
    one_pictrue_img.convert("RGBA")
    one_pictrue_img.save(another_pic_dir + "/188.png")
    
    data_left_top = yunduo2_img.getpixel((0, 0))
    for i in range(yunduo2_img.size[0]):
        for j in range(yunduo2_img.size[1]):
            data = (yunduo2_img.getpixel((i, j)))
            if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2] and data[3] == data_left_top[3]:
                continue
            one_pictrue_img.putpixel((start_left_padding + i, start_top_padding + j), (data[0], data[1], data[2], data[3]))
    one_pictrue_img.convert("RGBA")
    one_pictrue_img.save(another_pic_dir + "/189.png")
    
    
    image_name = ['228.png', '230.png', '232.png']
    for index in range(len(image_name)):
        for i in range(one_pictrue_img.size[0]):
            for j in range(one_pictrue_img.size[1]):
                one_pictrue_img.putpixel((i, j), (data_left_top[0], data_left_top[1], data_left_top[2], data_left_top[3]))
        yunduo1_img = Image.open(yunduo_dir + "/" + image_name[index])
        for i in range(yunduo1_img.size[0]):
            for j in range(yunduo1_img.size[1]):
                data = (yunduo1_img.getpixel((i, j)))
                if start_left_padding + i < one_pictrue_img.size[0] and start_top_padding + j < one_pictrue_img.size[1]:
                    one_pictrue_img.putpixel((start_left_padding + i, start_top_padding + j), (data[0], data[1], data[2], data[3]))
        one_pictrue_img.convert("RGBA")
        one_pictrue_img.save(another_pic_dir + "/" + image_name[index])
    
    '''
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
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片'''
        
#add_one_pictrue_to_another_with_anchor()
#input_dir = prefix_dir + '佐助长大了/须左'
input_dir = prefix_dir + '佐助长大了/须左的箭'
output_dir = prefix_dir + '佐助长大了/添加到白板的图'

def flush_image_to_white(img):
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            img.putpixel((i,j),(255, 255, 255, 255))
    return img
            
def add_pix_to_white():
    width_largest = 0
    height_largest = 0
    img_file_name = ''
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        if img.size[0] > width_largest:
            width_largest = img.size[0]
        if img.size[1] > height_largest:
            height_largest = img.size[1]
    
    for filename in os.listdir(input_dir):
        img_file_name = filename
    white_img = Image.open(input_dir + "/" + img_file_name)
    cropped = white_img.crop((0, 0, width_largest, height_largest)) 
    white_img = flush_image_to_white(cropped)
        
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)

        img_temp =  white_img.copy()
        left_pixel_padding = int(width_largest/2 - img.size[0]/2)
        top_pixel_padding = height_largest - img.size[1]
        top_left = img.getpixel((0, 0))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if top_left[0] == data[0] and top_left[1] == data[1] and top_left[2] == data[2] and top_left[3] == data[3]:
                    continue
                img_temp.putpixel((left_pixel_padding + i, top_pixel_padding + j), (data[0], data[1], data[2], data[3]))
        img_temp.convert("RGBA")
        img_temp.save(output_dir + "/" + filename)
        
#add_pix_to_white()

input_dir = prefix_dir + '佐助长大了/添加到白板的图'
output_dir = prefix_dir + '佐助长大了/对称中心添加图片'
def cut_off_white_left_padding():
    #给每一个图片设置一个中心线， 以中心线为基准进行图片刷到白板上的操作，每一张原图都有自己的中心线
    #列表的前面5个是还没有成型的须左，中轴线保持和第六个须左一致
    left_padding = [220, 220, 220, 220, 220, 220, 226, 223, 228, 233, 214, 210, 150, 210]
    
    img = Image.open(input_dir + "/531.png")   #150是最小的
    width_img = img.size[0] + 83 # 宽度-最小左边距=最大右边距   最大左边距即为最大左边  两者相加是最终的宽度
    cropped = img.crop((0, 0, width_img, img.size[1]))
    for i in range(cropped.size[0]):
        for j in range(cropped.size[1]):
            cropped.putpixel((i, j), (255, 255, 255, 255))
    
    index_padding = 0
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        img_temp =  cropped.copy()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if int(img_temp.size[0]/2) - left_padding[index_padding] + i < img_temp.size[0]:
                    img_temp.putpixel(( int(img_temp.size[0]/2) - left_padding[index_padding] + i, j), (data[0], data[1], data[2], data[3]))
        index_padding = index_padding + 1
        img_temp.save(output_dir + "/" + filename)

input_dir = prefix_dir + '佐助长大了/添加到白板的图'
output_dir = prefix_dir + '佐助长大了/对称中心添加图片'
def resize_pic():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        out = img.resize((int(img.size[0]/3), int(img.size[1]/2)))
        out.save(output_dir + "/" + filename)

#resize_pic()
input_dir = prefix_dir + '佐助长大了/写轮眼'
output_dir = prefix_dir + '佐助长大了/写轮眼处理'
def change_to_transparent():
    color_set = set()
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if data[0] == 0 and data[1] == 0 and data[2] == 0 and data[3] == 0:
                    img.putpixel((i, j), (255,255,255,255))
                if i == 35 and j == 17 and filename == '345.png':
                    print(i,j,data[0], data[1], data[2], data[3])
                if i == 1 and j == 1 and filename == '345.png':
                    print(i,j,data[0], data[1], data[2], data[3])
                #   print(i,j,data[0], data[1], data[2], data[3])
        img.save(output_dir + "/" + filename)
                
    #for item in color_set:
    #    print(item)
        
change_to_transparent()