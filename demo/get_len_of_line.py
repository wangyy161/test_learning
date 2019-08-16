# 导入math包
import math


# 定义点的函数
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y
    # 定义直线函数


class Getlen:
    def __init__(self, p1, p2):
        self.x = p1.getx() - p2.getx()
        self.y = p1.gety() - p2.gety()
        # 用math.sqrt（）求平方根
        self.len = math.sqrt((self.x ** 2) + (self.y ** 2))

    # 定义得到直线长度的函数
    def getlen(self):
        return self.len


# 设置点p1的坐标为（0,0）
p1 = Point(33452829.817629, 7861364.493524)
# 设置点p2的坐标为（3,4）
p2 = Point(33795692.193105, 7973115.696853)
# 定义对象
l = Getlen(p1, p2)
# 获取两点之间直线的长度
d = l.getlen()
print(d)
