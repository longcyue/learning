# 1、编写一个打印进度条代码
# 2、数据类型
# 3、进制转换
# 4、数学运算
# 5、内置函数：zip、filter、map、sorted
# 6、匿名函数：

# 1:编写一个打印进度条代码


import time
for i in range(0,101,2):
     time.sleep(0.1)
     char_num = i//2
     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
         if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
     print(per_str,end='', flush=True)



# 6：


# dic = {'k1':12,'k2':834,'k3':543,}
# # def func(k):
# #     return dic(k)
# ret = max(dic)
# print(ret)


#  6题目：有元组(（'a）,('b),('c),('d))---要变成：[{'a':'c'},{'b':'d'}]
# ret=zip((('a'),('b')),(('c'),('d')))
# def func():
#     for i in ret:
#         list = i
#         # return list[0]:list[1]
#         print({list[0]:list[1]})
# print(func())
#
#  6:
# ret =zip((('a'),('b')),(('c'),('d')))
# res = map(lambda tup:{tup[0]:tup[1]},ret)
# print(list(res))
