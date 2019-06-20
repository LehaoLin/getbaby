
import requests
from bs4 import BeautifulSoup
import re
import os
import time
import uuid
from PIL import Image 
 
# url="http://www.mm131.com/xinggan/"
url="https://www.mm131.net/xinggan/"

def allpage(endpage):
    i=2
    urls = ['https://www.mm131.net/xinggan/']
    while i <= endpage:
        url = 'https://www.mm131.net/xinggan/'+'list_6_'+str(endpage)+'.html'
        urls.append(url)
        i+=1
    return urls
    

def get_all():#获取首页所有图片组的信息
    # url="http://www.mm131.com/xinggan/"
    # urls=[
    #     'https://www.mm131.net/xinggan/',
    #     'https://www.mm131.net/xinggan/list_6_2.html',
    # ]
    urls = allpage(15)
    
    for url in urls:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
        html=requests.get(url,headers=headers)
        html.encoding="gbk"
        html=BeautifulSoup(html.text,'lxml')
        all_tpurl=html.select('.list-left > dd > a:nth-of-type(1) ')[:-1]
        #print(all_tpurl)
        for i in all_tpurl:
            tpz_url=i['href']#图片组链接
            name=i.find('img').get('alt')#图片组名字
            #print(tpz_url,name)
            yield (tpz_url,name)
#每组图片中，图片的链接是类似这样：http://img1.mm131.me/pic/3983/1.jpg，每张图片的链接只有结尾数字不同，
#因此只需要获取一组图片中的第一张图片，与组图的总张数即可获取每张图片的链接
 
def get_tuzu(tz):#获取单独一组图片中每张图片的链接并下载
    time.sleep(1)
    url=tz[0]
    name=tz[1]
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",}
    html=requests.get(url,headers=headers)
    html.encoding="gbk"
    html=BeautifulSoup(html.text,'lxml')
    tz_url=html.select('.content-pic > a > img:nth-of-type(1)')[0].get('src')
    tz_url=re.search(r'(http.*?/)\d+.jpg',tz_url)
    tz_url=tz_url.group(1)
    num=html.select('span.page-ch')[0].get_text()[1:3]#获取图片组的页数
     ####保存到C盘的mt文件夹中，并根据不同图片组命名不同的文件夹###
    # os.chdir('c:/')
    os.chdir('/Users/lingo/Documents/meta/babypic')
    c_list=os.listdir('/Users/lingo/Documents/meta/babypic')
    if "mt" in c_list:
        pass
    else:
        os.mkdir('/Users/lingo/Documents/meta/babypic/mt')
    os.chdir('/Users/lingo/Documents/meta/babypic/mt')
    # if name in os.listdir('/Users/lingo/Documents/meta/getbaby/mt'):
    #     pass
    # else:
    #     os.mkdir(name)
    # os.chdir(name)
     ####保存到C盘的mt文件夹中，并根据不同图片组命名不同的文件夹###
    q = 0
    for i in range(2,int(num)+1):
        tp_listurl=str(tz_url)+'{}.jpg'.format(str(i))
        #print(tp_listurl)
        html=xz(tp_listurl,referer=url)
        time.sleep(0.2)
        q += 1
        print(q)
        with open(str(uuid.uuid4()) +'.jpg','wb') as f:#下载
            f.write(html.content)
        
        #yield tp_listurl
    #yield url
 
    
def xz(url,referer):#获取单独一张图片的信息
    #要下载图片，headers必须添加【Referer】
    #根据测试Referer的可以是要下载图片本身的链接，也可以是要下载图片的组的链接，也可以是要下载图片的上一张图片的链接
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0','Referer':referer}
    html=requests.get(url,headers=headers)
    return html
 
if __name__=="__main__":
    for tz in get_all():
        get_tuzu(tz)
