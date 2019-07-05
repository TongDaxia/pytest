import  urllib.request

def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''
    print ("正在下载" + filename)

    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    #print(type(html))
    return html