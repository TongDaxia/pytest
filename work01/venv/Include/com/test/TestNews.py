import xlwt
import requests
from lxml import etree
import time
import os

os.chdir('C:/Users/Administrator/Desktop')  # 更改工作目录为桌面

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

# 所有行的内容
all_info_list = []


def get_info(url):
    html = requests.get(url, headers=headers)
    # html = requests.get(url)
    selector = etree.HTML(html.content)
    # infos = selector.xpath('//ul[@class="all-img-list cf"]/li')

    # //*[@id="myul"]/li[1]/a
    # //*[@id="myul"]/li[20]/a

    # //*[@id="myul"]/li[20]/span

    # myul > li:nth-child(2) > a
    i = 1
    while i <= 20:
        title = selector.xpath('//*[@id="myul"]/li[{}]/a/text()'.format(i))[0]
        time = selector.xpath('//*[@id="myul"]/li[{}]/span/text()'.format(i))[0]
        aLink = selector.xpath('//*[@id="myul"]/li[{}]/a/@href'.format(i))[0].replace("../../..","http://www.csrc.gov.cn/pub")
        # 每一行的内容
        info_list = [title, time, aLink]
        all_info_list.append(info_list)
        i += 1
    # time.sleep(1)


if __name__ == '__main__':
    urls = ['http://www.csrc.gov.cn/pub/newsite/xxpl/yxpl/index_{}.html'.format(
        str(i)) for i in range(0, 20)]
    urls[0] = 'http://www.csrc.gov.cn/pub/newsite/xxpl/yxpl/index.html'
    page_crawled = 1
    for url in urls:
        get_info(url)
        print("{} pages has crawled".format(str(page_crawled)))
        page_crawled += 1
    header = ['标题', '发布时间', '详情链接']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1

    book.save('news2.xls')
