class player:
    def __init__(self, name, health, energy) :
        self.name = name
        self.health = health
        self.energy = energy
        self.display_personaj()
    def display_personaj(self):
        print('имя персонажа: {}. кол-во здоровья: {}. кол-во энергии: {}.'.format(self.name, self.health, self.energy))

pers1 = player("Hojy", 90, 20)
pers2 = player("Bony", 60, 45)
pers3 = player("Flash", 30, 80)
pers4 = player("Loky", 20, 90)
pers5 = player("Naru", 45, 60)
pers6 = player("Dolma", 80, 30)

def select_personaj1():
    vibran1 = 0
    print("Выберите персонажа для первого игрока: 1 - Hojy, 2 - Bony, 3 - Flash, 4 - Loky, 5 - Naru, 6 - Dolma")
    vibran1 = int(input())
    
    if vibran1 == 1:
        vibran1 = pers1
    if vibran1 == 2:
        vibran1 = pers2
    if vibran1 == 3:
        vibran1 = pers3
    if vibran1 == 4:
        vibran1 = pers4
    if vibran1 == 5:
        vibran1 = pers5
    if vibran1 == 6:
        vibran1 = pers6
    else:
        print("Введите число от 1 до 6!!!")
    return vibran1
znach1 = select_personaj1()
    
def select_personaj2():
    print("Выберите персонажа для второго игрока: 1 - Hojy, 2 - Bony, 3 - Flash, 4 - Loky, 5 - Naru, 6 - Dolma")
    vibran2 = int(input())
    
    if vibran2 == 1:
        vibran2 = pers1
    if vibran2 == 2:
        vibran2 = pers2
    if vibran2 == 3:
        vibran2 = pers3
    if vibran2 == 4:
        vibran2 = pers4
    if vibran2 == 5:
        vibran2 = pers5
    if vibran2 == 6:
        vibran2 = pers6
    else:
        print("Введите число от 1 до 6!!!")
    return vibran2
znach2 = select_personaj2()


direction = 0

player1 = znach1
player2 = znach2
player1.direction = random.randint(1, 4)
player2.direction = random.randint(1, 4)       
