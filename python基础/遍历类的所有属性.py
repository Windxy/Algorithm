class Car:
    def __init__(self, name, loss):  # loss [价格，油耗，公里数]
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        # 获取汽车价格
        return self.loss[0]

    def getLoss(self):
        # 获取汽车损耗值
        return self.loss[1] * self.loss[2]

Bmw = Car("宝马", [60, 9, 500])  # 实例化一个宝马车对象
print(getattr(Bmw, "name"))  # 使用getattr()传入对象名字,属性值。
print(dir(Bmw))  # 获Bmw所有的属性和方法

# 动态获取和设置对象的属性
if hasattr(Bmw,"name"):
    setattr(Bmw,"name","BaoMa")
    print(getattr(Bmw,"name"))