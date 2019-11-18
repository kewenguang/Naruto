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
        
input_dir = prefix_dir + '我爱罗/我爱罗_idle'
output_dir = prefix_dir + '我爱罗/我爱罗_idle_change'
def change_pic_height():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        cropped = img.crop((0, 0, img.size[0], 52)) 
        cropped.save(output_dir + "/" + filename)
        
#change_pic_height()
#sys.exit()
        


def di_bao_tian_xing():
    img = Image.open(prefix_dir + '/佩恩/地爆天星/774.png')
    for i in range(36):
        img_rotate = img.rotate(10*i)
        img_rotate.save(prefix_dir + '/佩恩/地爆天星旋转/' + str(i*10) + '.png')
        #img = rotate_image_in_angle(image, 20*i)
        #cv.imwrite(prefix_dir + '/佩恩/地爆天星旋转/' + str(i*10) + '.png', img)

#di_bao_tian_xing()
#sys.exit()
        
input_dir = prefix_dir + '佩恩/出场'
output_dir = prefix_dir + '佩恩/整理后的出场'
def change_pic_color():
    for filename in os.listdir(input_dir):
        i = 1
        j = 1
        img = Image.open(input_dir + "/" + filename)#读取系统的内照片
        print (img.size)#打印图片大小
        
        #print("img.getpixel((0,0))")
        #print (img.getpixel((0, 0)))
        #print("img.getpixel((0,0))")
        
        data_left_top = img.getpixel((0, 0))
        
        width = img.size[0]#长度
        height = img.size[1]#宽度
        for i in range(0,width):#遍历所有长度的点
          for j in range(0,height):#遍历所有宽度的点
            data = (img.getpixel((i,j)))#打印该图片的所有点
            #print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            #print (data[0])#打印RGBA的r值
            #if i == 167 and j == 197:
            #    print(data)
            if data[0] == data_left_top[0] and data[1] == data_left_top[1] and data[2] == data_left_top[2] and data[3] == data_left_top[3]:
                img.putpixel((i, j),(255, 255, 255, 255))
            #if data[0] == 25 and data[1] == 25 and data[2] == 25 and data[3] == 255:
            #    img.putpixel((i,j),(0, 0, 0, 255)) 
            #img.putpixel((i,j),(255, 255, 255, 0))
            #if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #  img.putpixel((i,j),(234, 53, 57, 255))#则这些像素点的颜色改成大红色
        
        img.save(output_dir + "/" + filename)#保存修改像素点后的图片
#change_pic_color()
#sys.exit()

one_pic = prefix_dir + '佩恩/地爆天星个球/774.png'
def add_pic_to_center():
    img_one = Image.open(one_pic)
    for i in range(img_one.size[0]):
        for j in range(img_one.size[1]):
            img_one.putpixel((i, j), (255, 255, 255, 255))
    for filename in os.listdir(input_dir):
        img_white = img_one.copy()
        img = Image.open(input_dir + '/' + filename)
        start_left = int(img_white.size[0]/2) - int(img.size[0]/2)
        start_top = int(img_white.size[1]/2) - int(img.size[1]/2)
        top_left_data = img.getpixel((0, 0))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if data[0] == top_left_data[0] and data[1] == top_left_data[1] and data[2] == top_left_data[2] and data[3] == top_left_data[3]:
                    continue
                img_white.putpixel((start_left + i, start_top +j), (data[0], data[1], data[2], data[3]))
        img_white.save(output_dir + "/" + filename)
        
one_pic = prefix_dir + '背景资源/images/4.png'
another_pic = prefix_dir + '背景资源/images/1.png'
output_dir =  prefix_dir + '背景资源/images/'
def add_pic_to_center_down():
    img_one = Image.open(one_pic)
    img_another = Image.open(another_pic)
    
    img_another = img_another.resize((img_one.size[0], img_one.size[1]), Image.ANTIALIAS)
    
    start_left = int(img_another.size[0]/2) - int(img_another.size[0]/2)
    start_top = int(img_another.size[1]) - int(img_one.size[1])
    top_left_data = img_one.getpixel((0, 0))
    for i in range(img_one.size[0]):
        for j in range(img_one.size[1]):
            data = img_one.getpixel((i, j))
            if data[0] == top_left_data[0] and data[1] == top_left_data[1] and data[2] == top_left_data[2] and data[3] == top_left_data[3]:
                continue
            img_another.putpixel((start_left + i, start_top +j), (data[0], data[1], data[2], data[3]))
    img_another.save(output_dir + "/游戏背景.jpg")
#add_pic_to_center_down()
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

input_dir = prefix_dir + '自来也/长条火焰'
output_dir = prefix_dir + '自来也/拉长的火焰'
def resize_pic():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        out = img.resize((int(1000), int(150)), Image.ANTIALIAS)
        out.save(output_dir + "/" + filename)

#resize_pic()
#sys.exit()

input_dir = prefix_dir + '自来也/长条火焰'
output_dir = prefix_dir + '自来也/拉长的火焰'
def set_left_top_padding_pixel_to_white():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        img.putpixel((0, 0), (255, 255, 255, 255))
        img.save(output_dir + "/" + filename)

set_left_top_padding_pixel_to_white()
sys.exit()

def cut_top_pic():
    img_white = Image.open(input_dir + "/39.png")
    img_white = img_white.crop((0, 0, img_white.size[0], img_white.size[1] - 15))
    for i in range(img_white.size[0]):
        for j in range(img_white.size[1]):
            img_white.putpixel((i, j), (255, 255, 255, 255))
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        data_left_top = img.getpixel((0, 0))
        img_copy = img_white.copy()
        for i in range(img_white.size[0]):
            for j in range(img_white.size[1]):
                data = img.getpixel((i, j + 15))
                if data_left_top[0] == data[0] and data_left_top[1] == data[1] and data_left_top[2] == data[2] and data_left_top[3] == data[3]:
                    continue
                img_copy.putpixel((i, j), (data[0], data[1], data[2], data[3]))
        img_copy.save(output_dir + "/" + filename)
cut_top_pic()
sys.exit()

from PIL import ImageDraw, ImageFont
def add_text():
    img = Image.open(input_dir + '/封面.jpg')
    font = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', 30)
    draw = ImageDraw.Draw(img)
    fill_color = '#ffffff'
    position = (450, 62)
    draw.text(position, '语音玩法和手势玩法', font=font, fill=fill_color, spacing=0, align='left')
    position = (542, 110)
    draw.text(position, '&&', font=font, fill=fill_color, spacing=0, align='left')
    position = (504, 150)
    draw.text(position, 'IP类游戏', font=font, fill=fill_color, spacing=0, align='left')
    img.save(output_dir + '/封面.jpg')

#add_text()
#sys.exit()

def get_center_pixel():
    width = 720 - 317
    height = 870 - 460
    img_white = Image.open(input_dir + '/777.png')
    img_white = img_white.crop((0,0,width,height))
    for i in range(img_white.size[0]):
        for j in range(img_white.size[1]):
            img_white.putpixel((i, j), (255,255,255,255))
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + '/' + filename)
        img_white_copy = img_white.copy()
        for i in range(img_white_copy.size[0]):
            for j in range(img_white_copy.size[1]):
                data = img.getpixel((i + 317, j + 460))
                img_white_copy.putpixel((i , j ), (data[0], data[1], data[2], data[3]))
        img_white_copy.save(output_dir + '/' + filename)

def pic_to_square():
    #球的形成与旋转
    img_white = Image.open(input_dir + '/0.png')
    max_length = img_white.size[0]
    if max_length <  img_white.size[1]:
        max_length = img_white.size[1]
    
    img_white = img_white.crop((0, 0, max_length, max_length))
    for i in range(img_white.size[0]):
        for j in range(img_white.size[1]):
            img_white.putpixel((i, j), (255, 255, 255, 255))
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + '/' + filename)
        start_left_padding = int(max_length/2) - int(img.size[0]/2)
        start_top_padding = int(max_length/2) - int(img.size[1]/2)
        img_white_copy = img_white.copy()
        
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                img_white_copy.putpixel((i + start_left_padding ,j + start_top_padding), (data[0], data[1], data[2], data[3]))
        img_white_copy.save(output_dir + '/' + filename)
pic_to_square()
sys.exit()

#get_center_pixel()
#sys.exit()

def resize_one_pic_in_center():
    img = Image.open(input_dir + "/70.png")
    out = img.resize((int(img.size[0]*0.6), int(img.size[1]*0.6)), Image.ANTIALIAS)
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            img.putpixel((i, j), (255,255,255,255))
    
    start_left = int(img.size[0]/2) - int(out.size[0]/2)
    start_top = int(img.size[1]/2) - int(out.size[1]/2)
    for i in range(out.size[0]):
        for j in range(out.size[1]):
            data = out.getpixel((i, j))
            img.putpixel((start_left + i, start_top + j), (data[0], data[1], data[2], data[3]))
    
    img.save(output_dir + "/70.png")

#resize_one_pic_in_center()

def one_center_change_to_another_center():
    one_image = Image.open(input_dir + "/70.png")
    another_image = Image.open(input_dir + "/214.png")
    
    for i in range(another_image.size[0]):
        for j in range(another_image.size[1]):
            another_image.putpixel((i, j), (255,255,255,255))
            
    start_left = int(one_image.size[0]/2) - int(another_image.size[0]/2)
    start_top = int(one_image.size[1]/2) - int(another_image.size[1]/2)
    
    for i in range(another_image.size[0]):
        for j in range(another_image.size[1]):
            data = one_image.getpixel((start_left + i, start_top + j))
            another_image.putpixel((i, j), (data[0], data[1], data[2], data[3]))
    another_image.putpixel((0, 0), (255, 255, 255, 255))
    another_image.save(output_dir + "/70.png")
    
#one_center_change_to_another_center()
#sys.exit()
#resize_pic()
#sys.exit()

def resize_one_pic_to_another_pic_size():
    one_image = Image.open(input_dir + '/1.png')
    another_image = Image.open(input_dir + '/210.png')
    out = one_image.resize(((another_image.size[0]), (another_image.size[1])), Image.ANTIALIAS)
    out.save(output_dir + '/1.png')

now_dir_pic = prefix_dir + '自来也/现在的自来也/235.png'
pics_dir = prefix_dir + '自来也/下蹲通灵'
output_dir = prefix_dir + '自来也/缩小的下蹲通灵'
def resize_pics_to_another_pic():
    one_image = Image.open(now_dir_pic)
    for filename in os.listdir(pics_dir):
        img = Image.open(pics_dir + "/" + filename)
        img = img.resize(((one_image.size[0]), (one_image.size[1])), Image.ANTIALIAS)
        img.save(output_dir + '/' + filename)
#resize_pics_to_another_pic()
#sys.exit()

#resize_one_pic_to_another_pic_size()
#sys.exit()

input_dir = prefix_dir + '我爱罗/我爱罗_idle'
output_dir = prefix_dir + '我爱罗/我爱罗_idle_change'
def change_to_transparent():
    color_set = set()
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if data[0] == 0 and data[1] == 0 and data[2] == 0 and data[3] == 0:
                    img.putpixel((i, j), (255,255,255,255))
                #if i == 35 and j == 17 and filename == '345.png':
                #    print(i,j,data[0], data[1], data[2], data[3])
                #if i == 1 and j == 1 and filename == '345.png':
                #    print(i,j,data[0], data[1], data[2], data[3])
                #   print(i,j,data[0], data[1], data[2], data[3])
        img.save(output_dir + "/" + filename)
                
    #for item in color_set:
    #    print(item)

#change_to_transparent()
#sys.exit()
def add_yun_duo_to_another_pic():
    zilaiye_url = prefix_dir + '我爱罗/自来也/1.png'
    zilaiye_img = Image.open(zilaiye_url)
    for filename in os.listdir(input_dir):
        img_yun_duo = Image.open(input_dir + "/" + filename)
        zilaiye_copy = zilaiye_img.copy()
        data_top_left = img_yun_duo.getpixel((0, 0))
        for i in range(img_yun_duo.size[0]):
            for j in range(img_yun_duo.size[1]):
                data = img_yun_duo.getpixel((i, j))
                if data[0] == data_top_left[0] and data[1] == data_top_left[1] and data[2] == data_top_left[2] and data[3] == data_top_left[3]:
                    continue
                zilaiye_copy.putpixel((i, j), (data[0], data[1], data[2], data[3]))
        zilaiye_copy.save(output_dir + "/" + filename)        

#add_yun_duo_to_another_pic()

def only_change_pic_height():
    img_one = Image.open(input_dir + "/233.png")
    height = img_one.size[1]
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        img_copy = img.copy()
        img = img.crop((0, 0, img.size[0], height))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                img.putpixel((i, j), (255,255,255,255))
        start_height = height - img_copy.size[1]
        for i in range(img_copy.size[0]):
            for j in range(img_copy.size[1]):
                data = img_copy.getpixel((i, j))
                img.putpixel((i, start_height + j), (data[0], data[1], data[2], data[3]))
        img.save(output_dir + "/" + filename)
#only_change_pic_height()

def find_dir_max_width_and_height(input_dir):
    max_width = 0
    max_height = 0
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        if img.size[0] > max_width:
            max_width = img.size[0]
        if img.size[1] > max_height:
            max_height = img.size[1]
    return max_width, max_height

input_dir = prefix_dir + '佩恩/出场'
output_dir = prefix_dir + '佩恩/整理后的出场'
def add_pic_to_max_width_and_max_height():
    max_width, max_height = find_dir_max_width_and_height(input_dir)

    img_white = Image.open(input_dir + "/603.png")
    for i in range(img_white.size[0]):
        for j in range(img_white.size[1]):
            img_white.putpixel((i, j), (255, 255, 255, 255))
    img_white = img_white.crop((0, 0, max_width, max_height))
    for i in range(img_white.size[0]):
        for j in range(img_white.size[1]):
            img_white.putpixel((i, j), (255, 255, 255, 255))
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + "/" + filename)
        img_white_copy = img_white.copy()
        start_left = int(img_white_copy.size[0]/2) - int(img.size[0]/2)
        start_top = img_white_copy.size[1] - img.size[1]
        left_top_data = img.getpixel((0, 0))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if left_top_data[0] == data[0] and left_top_data[1] == data[1] and left_top_data[2] == data[2] and left_top_data[3] == data[3]: 
                    continue
                img_white_copy.putpixel((start_left + i, start_top + j), (data[0], data[1], data[2], data[3]))
        img_white_copy.save(output_dir + "/" + filename)
        
#add_pic_to_max_width_and_max_height()
#sys.exit()

#加一个函数，对图片中的像素进行下降
def pixel_down():
    img = Image.open(input_dir + '/603.png')
    padding_down = 22 #下降22个像素
    img_copy = img.copy()
    for i in range(img_copy.size[0]):
        for j in range(img_copy.size[1]):
            img_copy.putpixel((i, j), (255, 255, 255, 255))
    data_top_left = img.getpixel((0, 0))
    for i in range(img.size[0]):
        for j in range(img.size[1] - padding_down):
            data = img.getpixel((i, j))
            if data[0] == data_top_left[0] and data[1] == data_top_left[1] and data[2] == data_top_left[2] and data[3] == data_top_left[3]:
                continue
            img_copy.putpixel((i, j + padding_down), (data[0], data[1], data[2], data[3]))
    img_copy.save(output_dir + '/603.png')
#pixel_down()
#sys.exit()

def add_height_and_pixel_down(img, height):
    img_copy = img.copy()
    for i in range(img_copy.size[0]):
        for j in range(img_copy.size[1]):
            img_copy.putpixel((i, j), (255, 255, 255, 255))
    img_copy = img_copy.crop((0, 0, img_copy.size[0], height))
    for i in range(img_copy.size[0]):
        for j in range(img_copy.size[1]):
            img_copy.putpixel((i, j), (255, 255, 255, 255))
    height_padding = height - img.size[1]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            data = img.getpixel((i, j))
            img_copy.putpixel((i, j + height_padding),(data[0], data[1], data[2], data[3]))
    return img_copy
            
def exe_add_height_and_pixel_down():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + '/' + filename)
        zeng_gao = add_height_and_pixel_down(img, 125)
        zeng_gao.save(output_dir + '/' + filename)
#exe_add_height_and_pixel_down()
#sys.exit()


hama = prefix_dir + '自来也/蛤蟆/219.png'
hama_yun_dir = prefix_dir + '自来也/蛤蟆的云'
hama_tong_ling_dir = prefix_dir + '自来也/蛤蟆通灵'
def add_hama_to_yun():
    max_width, max_height = find_dir_max_width_and_height(hama_yun_dir)
    hama_img = Image.open(hama)
    if max_width < hama_img.size[0]:
        max_width = hama_img.size[0]
    if max_height < hama_img.size[1]:
        max_height = hama_img.size[1]
    
    white_img = hama_img.copy()
    
    white_img = white_img.crop((0, 0, max_width, max_height))
    
    for i in range(white_img.size[0]):
        for j in range(white_img.size[1]):
            white_img.putpixel((i, j), (255, 255, 255, 255))
    
    
    for filename in os.listdir(hama_yun_dir):
        img = Image.open(hama_yun_dir + '/' + filename)
        
        white_img_copy = white_img.copy()
        
        #先加上蛤蟆
        start_left = int(white_img.size[0]/2) - int(hama_img.size[0]/2)
        start_top = white_img.size[1] - hama_img.size[1]
        left_top_data = hama_img.getpixel((0,0))
        for i in range(hama_img.size[0]):
            for j in range(hama_img.size[1]):
                data = hama_img.getpixel((i, j))
                if left_top_data[0] == data[0] and left_top_data[1] == data[1] and left_top_data[2] == data[2] and left_top_data[3] == data[3]: 
                    continue
                white_img_copy.putpixel((i+start_left, j + start_top), (data[0], data[1], data[2], data[3]))
        
        
        start_left = int(white_img.size[0]/2) - int(img.size[0]/2)
        start_top = white_img.size[1] - img.size[1]
        left_top_data = img.getpixel((0,0))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if left_top_data[0] == data[0] and left_top_data[1] == data[1] and left_top_data[2] == data[2] and left_top_data[3] == data[3]: 
                    continue
                white_img_copy.putpixel((i+start_left, j + start_top), (data[0], data[1], data[2], data[3]))
                
        white_img_copy.save(hama_tong_ling_dir + '/' + filename)
        
        
        start_left = int(white_img.size[0]/2) - int(hama_img.size[0]/2)
        start_top = white_img.size[1] - hama_img.size[1]
        left_top_data = hama_img.getpixel((0,0))
        for i in range(hama_img.size[0]):
            for j in range(hama_img.size[1]):
                data = hama_img.getpixel((i, j))
                if left_top_data[0] == data[0] and left_top_data[1] == data[1] and left_top_data[2] == data[2] and left_top_data[3] == data[3]: 
                    continue
                white_img.putpixel((i+start_left, j + start_top), (data[0], data[1], data[2], data[3]))
        white_img.save(hama_tong_ling_dir + '/228.png')
        
input_file = prefix_dir + '自来也/现在的蛤蟆/228.png'
input_dir = prefix_dir + '自来也/蛤蟆喷火'
output_dir = prefix_dir + '自来也/蛤蟆喷火处理过'
def resize_hama_penhuo():
    hama_img = Image.open(input_file)
    for i in range(hama_img.size[0]):
        for j in range(hama_img.size[1]):
            hama_img.putpixel((i, j),(255, 255, 255, 255)) 
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + '/' + filename)
        start_left = int(hama_img.size[0]/2) - int(img.size[0]/2)
        start_top = hama_img.size[1] - img.size[1]
        hama_img_copy = hama_img.copy()
        left_top_data = img.getpixel((0,0))
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                data = img.getpixel((i, j))
                if left_top_data[0] == data[0] and left_top_data[1] == data[1] and left_top_data[2] == data[2] and left_top_data[3] == data[3]: 
                    continue
                hama_img_copy.putpixel((i+start_left, j + start_top), (data[0], data[1], data[2], data[3]))
        hama_img_copy.save(output_dir + '/' + filename)

input_dir = prefix_dir + '自来也/长条火焰'
output_dir = prefix_dir + '自来也/旋转后的长条火焰'
def rotate_image():
    for filename in os.listdir(input_dir):
        img = Image.open(input_dir + '/' + filename)
        out = img.transpose(Image.ROTATE_180)
        out.save(output_dir + '/' + filename)
rotate_image()
#resize_hama_penhuo()
#add_hama_to_yun()
#add_pic_to_max_width_and_max_height()