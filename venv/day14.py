# class Teacher:
#     def __init__(self, name, age):
#         # self.__name=name
#         # self.__age=age
#         self.set_info(name, age)
#
#     def tell_info(self):
#         print('姓名:%s,年龄:%s' % (self.__name, self.__age))
#
#     def set_info(self, name, age):
#         if not isinstance(name, str):
#             raise TypeError('姓名必须是字符串类型')
#         if not isinstance(age, int):
#             raise TypeError('年龄必须是整型')
#         self.__name = name
#         self.__age = age
#
#
# t = Teacher('egon', 18)
# t.tell_info()
#
# t.set_info('ego', 19)
# t.tell_info()


# class ATM:
#     def __card(self):
#         print('插卡')
#
#     def __auth(self):
#         print('用户认证')
#
#     def __input(self):
#         print('输入取款金额')
#
#     def __print_bill(self):
#         print('打印账单')
#
#     def __take_money(self):
#         print('取款')
#
#     def withdraw(self):
#         self.__card()
#         self.__auth()
#         self.__input()
#         self.__print_bill()
#         self.__take_money()
#
#
# a = ATM()
# a.withdraw()


class Studentclass:
    school = 'jiaotong university'
    count = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        Studentclass.count += 1

    def learn(self):
        print('%s is learning' % self.name)


stu1 = Studentclass('james', 23, 'male')
stu2 = Studentclass('poal', 24, 'male')
stu3 = Studentclass('harden', 25, 'male')
print(Studentclass.count)
print(stu1.__dict__)
print(stu2.__dict__)
print(stu3.__dict__)
print(stu1.count)
print(stu2.count)
print(stu3.count)