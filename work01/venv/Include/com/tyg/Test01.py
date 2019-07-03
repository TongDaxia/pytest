class MyNumber:
    def __init__(self):
        print("初始化开始:",end=" ")
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return  x

print("1111",end=" ")
myclass = MyNumber()
print("2222")
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))