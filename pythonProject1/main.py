import random
from array import *
class entity:
    Name=""
    specialAttName= ""
    def __init__(self,health,maxhealth, rang, attack, defence, crt):
        self.health = int(health)
        self.rang = int(rang)
        self.attack = int(attack)
        self.crt = int(crt)
        self.defence = int(defence)
        self.maxhealth = int(maxhealth)
    def Attack(self):
        r = random.randint(0, 100)
        attack = self.attack
        if r <= self.crt:
            attack *=2
        return attack
    def Defense(self):
        r = random.randint(0, 100)
        defence = -self.defence
        if r <= self.crt:
            defence *=2
        return defence
        pass
    def Special(self):
        pass
    def RandomAction(self):
        action = random.randint(0, 6)
        if action <=2:
            return self.Attack()
        elif action >2 and action <=5:
            return self.Defense()
        elif action == 6:
            print(self.specialAttName)
            return self.Special()
class player(entity):
    health = 100
    rang=0
    maxhealth=100
    atc = 10
    crt = 10
class Goblin(entity):
    Name = "Гоблин"
    specialAttName = "Призыв родни\n(Гоблин призивает на помощь сородича)"
    def Special(self):
        return Goblin
class Vampair(entity):
    Name = "Вампир"
    specialAttName = "Укус вампира\n(Вампир высасывает из вас жизненные соки)"
    def Special(self):
        r = random.randint(0, 100)
        attack = self.attack
        if r <= self.crt:
            attack *= 2
        self.health+= attack
        return attack
p = player(100,100,1,10,10,10)
v= Vampair(10,10,1,10,10,10)
enemys = [v]
enemys.remove(enemys[0])
def create():
    r = random.randint(0,1)
    if r ==0:
        return Goblin(15,15,1,10,2,10)
    else:
        return Vampair(30,30,1,30,5,10)
while True :
    protect = 0
    print("Здоровье= "+str(p.health))
    if len(enemys)<1:
        print("Новый враг")
        enemys.append(create())
    print("ваши противник:")
    for i in enemys:
        print(i.Name+'\t Здоровье '+str(i.health))
    print('1: атака\n2: защита')
    action = int(input('ваши дествия \n'))
    if action == 1:
        if len(enemys)>1:
            print("у вас "+len(enemys)+"противников, ввыберете какого атаковать")
            action = int(input('противник № \n'))
            atc = p.Attack()
            enemys[action].health-=atc
            if enemys[action].health<=0:
                enemys.remove(enemys[action])
            print("Вы атаковали противника на "+str(atc)+" урона")
        else:
            atc = p.Attack()
            enemys[0].health-=atc
            if enemys[0].health<=0:
                enemys.remove(enemys[0])
            print("Вы атаковали противника на " + str(atc) + " урона")
    if action == 2:
        print("Вы ушли в защиту")
        protect = p.defence
    elif action == 0:
        break
    for i in enemys:
        act = (i.RandomAction())
        if type(act) ==int:
            if act>0:
                damage = act-protect
                if  damage<0:
                    damage = 0
                p.health -=damage
                print("Вас атаковали на "+str(damage)+" урона")
            else:
                if action == 1:
                    i.health+=-act
                    print("противник защитился ")
        #else:
            #enemys.append(Goblin(15,15,1,10,2,10))
        #print(type(act))


