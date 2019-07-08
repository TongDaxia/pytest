import tushare as ts
import time
from sqlalchemy import create_engine


start = time.time()
engine = create_engine('mysql://root:root@localhost/stock?charset=utf8')
'''
#获取所有股票列表
df = ts.get_stock_basics()
engine = create_engine('mysql://root:root@localhost/stock?charset=utf8')
print(df)
#追加数据到现有表
df.to_sql("stock_basics",engine,if_exists='append')
'''


df = ts.get_hist_data('600848',ktype = '5',end="20190706",start='20100102' ) #一次性获取全部日k线数据
'''
df = ts.get_hist_data('600848') #一次性获取全部日k线数据
print(df)
df.to_sql("hist_data_600848",engine,if_exists='append')
# 
# ts.get_hist_data('600848', ktype='W') #获取周k线数据
# ts.get_hist_data('600848', ktype='M') #获取月k线数据
# ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
# ts.get_hist_data('600848', ktype='15') #获取15分钟k线数据
# ts.get_hist_data('600848', ktype='30') #获取30分钟k线数据
# ts.get_hist_data('600848', ktype='60') #获取60分钟k线数据
# ts.get_hist_data('sh'）#获取上证指数k线数据，其它参数与个股一致，下同
# ts.get_hist_data('sz'）#获取深圳成指k线数据
# ts.get_hist_data('hs300'）#获取沪深300指数k线数据
# ts.get_hist_data('sz50'）#获取上证50指数k线数据
# ts.get_hist_data('zxb'）#获取中小板指数k线数据
# ts.get_hist_data('cyb'）#获取创业板指数k线数据

'''

# df = ts.get_hist_data('600848') #一次性获取全部日k线数据

# df = ts.get_tick_data('603223',date='2019-7-5',src="sn",retry_count=3)
print(df)

df.to_sql("hist_data_600848_5",engine,if_exists='append')

print("操作总时间花费：",time.time()-start)
