
import requests

kw = {'wd':'长城'}

'''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print (response.text)

# 查看响应内容，response.content返回的字节流数据
#print (respones.content)

# 查看完整url地址
print ("查看完整url地址",response.url)

# 查看响应头部字符编码
print ("查看响应头部字符编码",response.encoding)

# 查看响应码
print ("查看响应码",response.status_code)

'''

response = requests.get("http://www.baidu.com/")

# 7\. 返回CookieJar对象:
cookiejar = response.cookies

# 8\. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print (cookiejar)

print (cookiedict)