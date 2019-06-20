import os
import glob
from PIL import Image
import os.path

### JPG->PNG
i=0
path = "/Users/lingo/Documents/meta/getbaby/data/faces/"
savepath = "/Users/lingo/Documents/meta/getbaby/data/faces1/"
filelist = os.listdir(path)
for file in filelist:
    im = Image.open(path+filelist[i])
    filename = os.path.splitext(file)[0]
    im.save(savepath+filename+'.png') # or 'test.tif'
    i=i+1


