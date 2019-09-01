# weekeen with family
# 属性 和 方法都藏起来 不让你看见
class Person:
    __key = 123  # 私有静态属性
    def __init__(self,name,passwd):
        self.name = name
        self.__passwd = passwd   # 私有属性

    def __get_pwd(self):         # 私有方法
        return self.__passwd   #只要在类的内部使用私有属性，就会自动的带上_类名

    def login(self):          # 正常的方法调用私有的方法
        self.__get_pwd()

alex = Person('alex','alex3714')
print(alex._Person__passwd)   # _类名__属性名
# print(alex.get_pwd())
