class Dog:
    def __init__(self,name,aggr,hp,kind):
        self.name = name
        self.aggr = aggr
        self.hp=hp
        self.kind=kind
    def bite(self,Person):
        person.hp -= self.aggr



class Person:
    def __init__(self,name,aggr,hp,sex):
        self.name=name
        self.aggr=aggr
        self.hp=hp
        self.sex=sex
        self.money=0

    def attack(self,dog):
        dog.hp-=self.aggr
    def get_Weapon(self,weapon):
        if self.money>=weapon.price:
            self.money-=weapon.price
            self.weapon=weapon
            self.aggr+=weapon.aggr
        else:
            pass


class Weapon:
    def __init__(self,name,aggr,njd,price):
        self.name=name
        self.aggr=aggr
        self.njd=njd
        self.price=price
    # 武器大招
    def hand18(self,person):
        if self.njd > 0:
            person.hp -= self.aggr * 2
            self.njd -= 1

alex=Person('alex',0.5,100,'man')
pipi=Dog('pipi',100,500,'gongde')
alex.attack(pipi)
print(pipi.hp)

w = Weapon('打狗棒',100,3,998)
alex.money=1000
alex.get_Weapon(w)
alex.attack(pipi)
print(pipi.hp)
# 组合：一个对象的属性值是另外一个类的对象
alex.weapon.hand18(pipi)  # 组合调用，alex.weapon是Weapon类的对象
print(pipi.hp)





