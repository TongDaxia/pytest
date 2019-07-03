import keyword

# l = keyword.kwlist
# print(l)
#
# x="111"
# y="222"
# print(x,end=" 32 ")
# print(y,end='')
import sys

print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
a=5//3
a1=5/3
print(a)
print(a1)


aa = ['a', 'b', 'c']
print(aa.__len__())
