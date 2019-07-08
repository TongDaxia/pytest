import tushare as ts
import time
import os
os.chdir('E:/backup')  # 更改工作目录

start = time.time()
#arr = ts.get_hist_data('600848') #一次性获取全部日k线数据

# pro = ts.pro_api()
# df = pro.stock_basic()

df = ts.get_stock_basics() #获取所有股票列表

#直接保存
df.to_csv('stock.csv')
print(df)
print("操作总时间花费：",time.time()-start)