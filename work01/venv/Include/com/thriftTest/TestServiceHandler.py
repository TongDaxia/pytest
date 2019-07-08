# -*- coding:utf-8 -*-
# 根据实际的包结构去引入
from test import TestService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


# test.thrift的具体实现

class TestServiceHandler:

    def __init__(self):
        self.log = {}

    # 服务端的方法名和客户端的相同，是通过thrift模板生成的
    def getStruct(self, num, name):
        print("接收到了请求，请求参数是：",num,name)
        print("执行一下服务端的相关方法……")
        return  name+"你好，请求已经接收到，我是黄河，我是黄河，有屁快放！"


if __name__ == '__main__':
    handler = TestServiceHandler()
    processor = TestService.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    #server.setNumThreads(5)
    print('python server:ready to start')
    server.serve()