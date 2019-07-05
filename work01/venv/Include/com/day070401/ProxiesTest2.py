import requests

# 根据协议类型，选择不同的代理
proxies = {
  "http": "http://121.17.174.121:9797"
}
# https://www.xicidaili.com/wt/1

response = requests.get("http://www.baidu.com", proxies = proxies)
print(response.content.decode())