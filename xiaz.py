#coding=gbk

import re

import os

import random

import requests

import math


import threading
def url_open(url):
    headers={
     'Connection': 'Keep-Alive',
    'Accept': 'image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',

}
    proxies = {

#"https": "http://127.0.0.1:1080",
    #   "http": "http://127.0.0.1:9150",
"http": "http://127.0.0.1:1080",
 "http": "http://127.0.0.1:8087",
 #"http": "http://127.0.0.1:8787",


}
    try:
       r = requests.get(url,proxies=proxies)
    except:
        r = requests.get(url)

    return r.text



def pic1_open(url):
     headers={
    'Connection': 'Keep-Alive',
    'Accept': 'image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',

}

     r = requests.get(url,headers=headers,timeout=240)

     return r.content

def get_page(url):
    html = url_open(url)
    pattern = r'(?<=当前第)\d+?(?=页)'   #good

    page = int(re.findall(pattern,html)[0])
    print('页面')
    print(page)
    return page
#2
def sava_num(qishu):
     save_gone2(qishu[0])
def save_gone2(list11):
    file1= open('visted2.txt','a')
    file1.write(list11+',')
    file1.close()
def find_imgs(html):
    pattern = r'(?<=<a href=")http://rosi.wangyunsheng.com/rosi/tu/.*?\.jpg'

    img_addrs = re.findall(pattern,html)

    return img_addrs
def save_num2(html):
    try:
       herf=find_href11(html)
       save_gone2(herf[0])
    except:
        print('0')
#5
def find_href(page_url):

    pattern = r'(?<=<a href=")http://www\.rosi365\.com/\d+?\.html'

    herf1=url_open(page_url)
    page_herf= re.findall(pattern,herf1)
    return page_herf
#3
def find_href11(text):


    pattern=r'(?<=\<title\>  ROSI套图 No\.)\d*'

    page_herf= re.findall(pattern,text)
    return page_herf
def save_imgs(img_addrs,page_num):
    global num1
    mulu=str(page_num)+str(num1)
    os.mkdir(mulu)

    os.chdir(mulu)

    for i in img_addrs:

      global num1
      filename =i.split('/')[-1]
      filename =str(num1)+filename
      try:

          k=pic1_open(i)


      except:
          print('tupian错误')
          continue
      file_object = open(filename, 'wb')
      file_object.write(k)
      file_object.close()

def download(pp):
    for i in pp:

      global num1
      filename =i.split('/')[-1]
      filename =str(num1)+filename
      try:

          k=pic1_open(i)


      except:
          print('tupian错误')
          continue
      file_object = open(filename, 'wb')
      file_object.write(k)
      file_object.close()


def download_mm(folder='D:\55',pages=10):
    try:
       os.mkdir(folder)
    except:
       os.chdir(folder)
    os.chdir(folder)
    folder_top = os.getcwd()
    url = 'http://www.rosi365.com/rosi/rosi/page/1'
    page_num = 1

    cishu=1
    while (cishu<pages):

        page_url = 'http://www.rosi365.com/rosi/rosi/page/' + str(page_num)
        print(page_url)
        urlin=find_href(page_url)
        print(urlin)
        global visited
        for tt in urlin:
            if tt not in  vi1:
              print(tt)

              vi1.append(tt)

              print('已增加历史记录')


              img_addrs = find_imgs(tt)

              print(img_addrs)

              save_imgs(img_addrs,page_num)

              os.chdir(folder_top)
              save_gone(tt)
              global num1
              num1+=1

        page_num += 1
        cishu += 1
        print('下载次数')
        print(cishu)
def save_gone(list11):
    os.chdir(nowfolder)
    file1= open('visted.txt','a')
    file1.write(list11+',')
    file1.close()
    os.chdir(folder)
def read_save():
    os.chdir(nowfolder)
    try:
        file1= open('visted.txt','r')
    except:
        file1= open('visted.txt','a')
    k=file1.read()
    k=k.replace('\n','')
    file1.close()
    Li=k.split(",")
    return  Li  #历史记录

def herf_title(url):
     html = url_open(url)
     pattern = r'(?<=<title>).+?(?= | 妹子图</title>)'   #good
     title= re.findall(pattern,html)[0]
     return title

def download_mm3(folder='D:\55',pages=10):
    try:
       os.mkdir(folder)
    except:
       os.chdir(folder)
    os.chdir(folder)
    folder_top = os.getcwd()
    url = 'http://www.rosi365.com/rosi/rosi/page/1'
    page_num = 1

    cishu=1
    while (cishu<pages):

        page_url = 'http://www.rosi365.com/rosi/rosi/page/' + str(page_num)
        print(page_url)
        urlin=find_href(page_url)
        print(urlin)
        global visited
        for tt in urlin:
            if tt not in  vi1:
              print(tt)

              vi1.append(tt)

              print('已增加历史记录')

              html = url_open(tt)
              img_addrs = find_imgs(html) #历史纪录在这里加


              print(img_addrs)
              global liebiao1
              liebiao1=img_addrs
              mulu=str(page_num)+str(num1)#或用随机数


              os.mkdir(mulu)

              os.chdir(mulu)

              #save_imgs(img_addrs,page_num)
              thread1 = myThread("Thread-1", page_num,folder_top)
              thread2 = myThread("Thread-2", page_num,folder_top)
              thread3 = myThread("Thread-3", page_num,folder_top)
              thread4 = myThread("Thread-4", page_num,folder_top)

              thread5 = myThread("Thread-5", page_num,folder_top)
              thread6 = myThread("Thread-6", page_num,folder_top)
              '''
              thread7 = myThread("Thread-7", page_num,folder_top)
              thread8 = myThread("Thread-8", page_num,folder_top)
            '''
              thread1.start()
              thread2.start()
              thread3.start()
              thread4.start()

              thread5.start()
              thread6.start()
              '''
              thread7.start()
              thread8.start()
            '''
              thread1.join()
              thread2.join()
              thread3.join()
              thread4.join()

              thread5.join()
              thread6.join()
              '''
              thread7.join()
              thread8.join()
            '''
              os.chdir(folder_top)
              save_gone(tt)
              os.chdir(nowfolder)
              save_num2(html)
              os.chdir(folder)
              global num1
              num1+=1

        page_num += 1
        cishu += 1
        print('下载次数')
        print(cishu)



class myThread (threading.Thread):
    def __init__(self,name, counter,folder_top):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.folder_top=folder_top
    def run(self):
        k=10

        while k>1:

            print("Starting " + self.name)
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
            mylock.acquire()
            try:
              getjpg=liebiao1[0]
            except:
              mylock.release()
              break

            print(self.name+'正在抓取'+getjpg)
            del liebiao1[0]
            mylock.release()


            save_imgssingle(getjpg,self.counter,self.folder_top)

        print('终止线程')

def save_imgssingle(img_addrs,page_num,folder_top):
    global num1

    filename =img_addrs.split('/')[-1]
    filename =str(num1)+filename
    try:

          k=pic1_open(img_addrs)

    except:
          print('tupian错误')
    else:      
          file_object = open(filename, 'wb')
          file_object.write(k)
          file_object.close()

def read_peizhi():
    os.chdir(nowfolder)
    try:
        file1= open('peizhi.txt','r')
    except:
        print('无配置文件')
    peizhiwenjian=file1.read()
    pattern = r'(?<=dizhi:).*?(?=;)'
    pattern_yeshu = r'(?<=yeshu:).*?(?=;)'
    dizhi=re.findall(pattern,peizhiwenjian)
    dizhi=dizhi[0].replace('\\\\','\\')
    yeshu=re.findall(pattern_yeshu,peizhiwenjian)
    yeshu=int(yeshu[0])
    peizhi=[]
    suijiwenjianjia=math.ceil(1000*random.random())
    dizhi=dizhi+str(suijiwenjianjia)
    peizhi.append(dizhi)
    peizhi.append(yeshu)
    print(peizhi)
    return  peizhi


if __name__ == '__main__':
    nowfolder=os.getcwd()
    folder = input("Please enter a folder(default is 'ooxx'): " )
    pages = input("How many pages do you wan to download(default is 10): ")
    peizhi=read_peizhi()

    if folder=='':
        folder=peizhi[0]
    if pages=='':
        pages=peizhi[1]

    print(folder)
    print(pages)
    kk=int(pages)
    pp=str(folder)
    num1=566
    global    liebiao1

    pool=[]
    vi1=read_save()
    print('爬虫历史记录')
    print(vi1)
    mylock = threading.RLock()
    download_mm3(pp,kk)



