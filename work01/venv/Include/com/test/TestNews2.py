import xlwt
import requests
from lxml import etree
import pdfkit
import time
import os

os.chdir('E:/backup')  # 更改工作目录为桌面

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

# 所有行的内容
all_info_list = []

def urllib_download(IMAGE_URL,name):
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, name)      # whole document


def request_download(IMAGE_URL,name):
    import requests
    r = requests.get(IMAGE_URL)
    with open(name, 'wb') as f:
        f.write(r.content)                      # whole document


def chunk_download(IMAGE_URL,name):
    import requests
    r = requests.get(IMAGE_URL, stream=True)    # stream loading
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.content)
    # //*[@id="gkml"]/div[2]/div[2]/div[3]  注意，附件可能有多个
    # //*[@id="gkml"]/div[2]/div[2]/div[3]/a[1]
    # //*[@id="gkml"]/div[2]/div[2]/div[3]/a[2]

    infos = selector.xpath('//*[@id="gkml"]/div[2]/div[2]/div[3]') #是一个列表
    i = 1 ;
    for info in infos :
        print("url:",url)
        title = info.xpath('a[{}]/text()'.format(i))[0] #标题
        aLink = info.xpath('a[{}]/@href'.format(i))[0].replace("./","http://www.csrc.gov.cn/pub/zjhpublic/G00306202/201906/") #链接
        # 每一行的内容
        info_list = [title, aLink]
        all_info_list.append(info_list)
        i += 1

    # time.sleep(1)


if __name__ == '__main__':
    urls = ['http://www.csrc.gov.cn/pub/zjhpublic/G00306202/201906/t20190628_3584{}.htm'.format(
        str(i)) for i in range(10, 30)]
    page_crawled = 1
    for url in urls:
        get_info(url)
        #print("{} pages has crawled".format(str(page_crawled)))
        page_crawled += 1
    header = ['标题', '链接']
    #book = xlwt.Workbook(encoding='utf-8')
    #sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        print(header[h],end='\t')
        #sheet.write(0, h, header[h])
    i = 1
    print('')
    for list in all_info_list:
        j = 0
        for data in list:
            print(data,end='\t')
            #sheet.write(i, j, data)
            j += 1
        print("")
        # 方法一
        print(list[1], list[0])
        #urllib_download(list[1], list[0])
        #request_download(list[1], list[0])
        chunk_download(list[1], list[0])
    i += 1



    #book.save('news2.xls')
