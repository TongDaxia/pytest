class MyNumber:
    def __init__(self):
        print("初始化开始:",end=" ")
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return  x
        else:
            raise StopIteration

print("55555",end=" ")
myclass = MyNumber()
print("23333")
myiter = iter(myclass)

for x in myiter:
    print(x)