import math
class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius=radius
 
    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积
 
    @property
    def perimeter(self):
        return 2*math.pi*self.radius #计算周长
 
c=Circle(10)
print(c.radius)
print(c.area) #可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
print(c.perimeter) #同上


class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)
 
p1=People('egon',75,1.85)
print(p1.bmi)
