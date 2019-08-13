# 1、正则表达式

# 2、re模块相关方法
import re
ret = re.findall('[a-z]+','aaab ccd  abdc')
print(ret) # 返回所有满足匹配条件的结果,放在列表里

ret = re.search('[a-z]+','aaab ccd  abdc')
if ret:
    print(ret.group())
# 从前往后，找到一个就返回,返回的变量需要调用group才能拿到结果
# 如果没有找到，那么返回None，调用group会报错

ret = re.match('[a-z]+','aaab ccd  abdc')
if ret:
    print(ret.group())
# match是从头开始匹配，如果正则规则从头开始可以匹配上，就返回一个变量。
# 匹配的内容需要用group才能显示
# 如果没匹配上，就返回None，调用group会报错


ret = re.sub('\d', 'H', 'eva3egon4yuan4',1)
#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

obj = re.compile('\d{3}')
#将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc128399eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())


import re
ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
# print(next(ret).group())  #查看第一个结果
# print(next(ret).group())  #查看第二个结果
# print([i.group() for i in ret])  #查看剩余的左右结果
for i in ret:
    print(i.group())
