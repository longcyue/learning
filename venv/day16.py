# # class Foo:
# #     def f1(self):
# #         print('from Foo.f1')
# #
# #     def f2(self):
# #         print('from Foo.f2')
# #
# #
# # class Bar(Foo):
# #     def f1(self):
# #         print('from Bar.f1')
# #
# #
# # b = Bar()
# # print(b.__dict__)  # {}
# # b.f1()  # from Bar.f1
#
#
# class People:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# class Course:
#     def __init__(self, name, period, price):
#         self.name = name
#         self.period = period
#         self.price = price
#
#     def tell_info(self):
#         print('<%s %s %s>' % (self.name, self.period, self.price))
#
#
# class Teacher(People):
#     def __init__(self, name, age, sex, job_title):
#         People.__init__(self, name, age, sex)
#         self.job_title = job_title
#         self.course = []
#         self.students = []


class Vehicle:  # 定义交通工具类
    Country = 'China'

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('开动啦...')


class Subway(Vehicle):  # 地铁
    def __init__(self, name, speed, load, power, line):
        Vehicle.__init__(self, name, speed, load, power)
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您' % self.line)
        Vehicle.run(self)


line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
line13.run()