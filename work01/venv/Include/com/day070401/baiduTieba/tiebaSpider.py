import loadPage
import writeFile

def tiebaSpider(url, beginPage, endPage):
    """
        作用：负责处理url，分配每个url去发送请求
        url：需要处理的第一个url
        beginPage: 爬虫执行的起始页面
        endPage: 爬虫执行的截止页面
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        #print(fullurl)

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage.loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile.writeFile(html, filename)