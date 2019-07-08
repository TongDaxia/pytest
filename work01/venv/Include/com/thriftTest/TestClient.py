
import sys
sys.path.append("./test/")
from test import TestService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

if __name__ == '__main__':
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = TestService.Client(protocol)

      # connect
    transport.open()

    result = client.getStruct(123,"长江长江")  # 调用 ping 函数
    print(result)
    #test_obj = client.getObject("xxx", 2)  # 调用 getObject 函数


    # close
    transport.close()