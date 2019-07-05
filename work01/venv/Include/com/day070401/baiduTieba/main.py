import urllib
import tiebaSpider

# 模拟 main 函数
if __name__ == "__main__":

    #kw = input("请输入需要爬取的贴吧:")
    kw = 'lol'
    # 输入起始页和终止页，str转成int类型
    # beginPage = int(input("请输入起始页："))
    # endPage = int(input("请输入终止页："))
    beginPage=1
    endPage=5
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider.tiebaSpider(url, beginPage, endPage)