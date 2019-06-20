import os
import glob
from PIL import Image
import os.path



# '''修改图片文件大小jpgfile：图片文件；savedir：修改后要保存的路径'''
# def convertjpg(jpgfile,savedir,width=700,height=1050):
def convertjpg(jpgfile,savedir,width=96,height=96):
    img=Image.open(jpgfile) 
    w, h = img.size
    if w<h:    
        new_img=img.resize((width,height),Image.BILINEAR) 
        new_img.save(os.path.join(savedir,os.path.basename(jpgfile)))

'''查找给定路径下图片文件，并修改其大小'''
def modifyjpgSize(file,saveDir): 
    for jpgfile in glob.glob(file):
        convertjpg(jpgfile,saveDir)

#测试代码 png
file = r'/Users/lingo/Documents/meta/babypic/mt/*.jpg'
saveDir = r'/Users/lingo/Documents/meta/babypic/faces' 
modifyjpgSize(file,saveDir)



