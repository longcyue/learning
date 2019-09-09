import hashlib
usr = input("username:")
pwd = input("passwd :")

with open('userinfo') as f:
    for line in f:
        user,passwd,role = line.split('|')
        md5 = hashlib.md5()
        md5.update(bytes(pwd,encoding='utf-8'))
        md5_pwd = md5.hexdigest()
        if usr == user and md5_pwd == passwd:
            print("alex ..")