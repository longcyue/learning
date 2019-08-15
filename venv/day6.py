import json
dic={1:'a',2:'b'}
print(type(dic),dic)
str_d = json.dumps(dic)
print(type(str_d),str_d)



f=open('ff','w',encoding='utf-8')
json.dump(dic,f)
f.close() #在本目录下新增了ff文件，dic内容被写入进去

f=open('ff')
res = json.load(f)
f.close()
print(type(res),res)


#最近工作比较忙，学得匆忙，周六看书好好复习，写5个列子的代码