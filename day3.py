# l = [0,1,2]
# print(len(l))

# 3.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
#
name=['alex','wupeiqi','yuanhao','nezha']
# def func(item):
#     return item+'_sb'
# ret = map(func,name)   #ret是迭代器
# for i in ret:
#     print(i)
# print(list(ret))

ret = map(lambda x:x+'_sb',name)
print(list(ret))


# 4.用filter函数处理数字列表，将列表中所有的偶数筛选出来
num = [1,3,5,6,7,8]
os = filter(lambda x:x%2==0,num)
print(list(os))

# num = [1,3,5,6,7,8]
# def func(x):
#     if x%2 == 0:
#         return True
# ret = filter(func,num)  #ret是迭代器
# print(list(ret))
#
# ret = filter(lambda x:x%2 == 0,num)
# ret = filter(lambda x:True if x%2 == 0 else False,num)
# print(list(ret))

# 6.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 6.1.计算购买每支股票的总价
# sum = map(lambda dic:dic{dic{'name'}:dic{'shares'}*dic{'price'}},portfolio)
# print(list(sum))

ret = map(lambda dic : {dic['name']:round(dic['shares']*dic['price'],2)},portfolio)
print(list(ret))




