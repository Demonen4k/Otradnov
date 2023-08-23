import random
 
def line():
    print('-' * 135)
    print('\n')
 
def menu1():
    print("Ход первого игрока:\n1 - идти в направлении\n2- повернуться по часовой стрелке\n3- повернуться против часовой стрелки\n")
 
def menu2():
    print("Ход второго игрока:\n1 - идти в направлении\n2- повернуться по часовой стрелке\n3- повернуться против часовой стрелки\n")

class field:
    player1x = random.randint(1, 3)
    player1y = random.randint(11, 13)
    player2x = random.randint(11, 13)
    player2y = random.randint(1, 3)
 
    # поле размером 15 на 15
 
    res1x = random.randint(0, 4)
    res1y = random.randint(0, 4)
    res2x = random.randint(0, 4)
    res2y = random.randint(5, 9)
    res3x = random.randint(5, 9)
    res3y = random.randint(0, 4)
    res4x = random.randint(5, 9)
    res4y = random.randint(5, 9)
    res5x = random.randint(5, 9)
    res5y = random.randint(10, 14)
    res6x = random.randint(10, 14)
    res6y = random.randint(10, 14)
    res7x = random.randint(10, 14)
    res7y = random.randint(5, 9)
 
    def show_field(self, player1x, player1y, player2x, player2y, res1x, res1y, res2x, res2y, res3x, res3y, res4x, res4y,
                   res5x, res5y, res6x, res6y, res7x, res7y):
        for i in range(15):
            for j in range(15):
                if (field.player1x == j and field.player1y == i):
                    print('X', end='   ')
 
                elif (field.player2x == j and field.player2y == i):
                    print('Y', end='   ')
 
                elif (field.res1x == j and field.res1y == i):
                    print('R', end='   ')
 
                elif (field.res2x == j and field.res2y == i):
                    print('R', end='   ')
 
                elif (field.res3x == j and field.res3y == i):
                    print('R', end='   ')
 
                elif (field.res4x == j and field.res4y == i):
                    print('R', end='   ')
 
                elif (field.res5x == j and field.res5y == i):
                    print('R', end='   ')
 
                elif (field.res6x == j and field.res6y == i):
                    print('R', end='   ')
 
                elif (field.res7x == j and field.res7y == i):
                    print('R', end='   ')
 
                else:
                    print('.', end='   ')
 
            print('\n')
 
 
# -------------------------------------------------------------

 
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
 
def move_attack_player1():
 
    if player1.direction == 1:
 
        if field.player2x == field.player1x and field.player1y-1 == field.player2y:
            player2.health = player2.health - 3
        else:
            field.player1y = field.player1y - 1
 
    elif player1.direction == 2:
        if field.player1x+1 == field.player2x and field.player1y == field.player2y:
            player2.health = player2.health - 3
        else:
            field.player1x = field.player1x + 1
 
 
 
    elif player1.direction == 3:
        if field.player1x == field.player2x and field.player1y+1 == field.player2y:
            player2.health = player2.health - 3
        else:
            field.player1y = field.player1y + 1
 
 
    else:
        if field.player1x -1== field.player2x and field.player1y == field.player2y:
            player2.health = player2.health - 3
        else:
            field.player1x = field.player1x - 1
 
 
    if field.player1x == field.res1x and field.player1y == field.res1y:
        player1.energy = player1.energy + 10
        field.res1x = 20
        field.res1y = 20
 
    if field.player1x == field.res2x and field.player1y == field.res2y:
        player1.energy = player1.energy + 10
        field.res2x = 20
        field.res2y = 20
 
    if field.player1x == field.res3x and field.player1y == field.res3y:
        player1.energy = player1.energy + 10
        field.res3x = 20
        field.res3y = 20
 
    if field.player1x == field.res4x and field.player1y == field.res4y:
        player1.energy = player1.energy + 10
        field.res4x = 20
        field.res4y = 20
 
    if field.player1x == field.res5x and field.player1y == field.res5y:
        player1.energy = player1.energy + 10
        field.res5x = 20
        field.res5y = 20
 
    if field.player1x == field.res6x and field.player1y == field.res6y:
        player1.energy = player1.energy + 10
        field.res6x = 20
        field.res6y = 20
 
    if field.player1x == field.res7x and field.player1y == field.res7y:
        player1.energy = player1.energy + 10
        field.res7x = 20
        field.res7y = 20
 
 
def move_attack_player2():
    if player2.direction == 1:
        if field.player1x == field.player2x and field.player1y == field.player2y-1:
            player1.health = player1.health - 3
 
        else:
            field.player2y = field.player2y - 1
 
 
    elif player2.direction == 2:
        if field.player1x == field.player2x+1 and field.player1y == field.player2y:
            player1.health = player1.health - 3
        else:
            field.player2x = field.player2x + 1
 
 
 
    elif player2.direction == 3:
        if field.player1x == field.player2x and field.player1y == field.player2y+1:
            player1.health = player1.health - 3
        else:
            field.player2y = field.player2y + 1
 
 
    else:
        if field.player1x == field.player2x-1 and field.player1y == field.player2y:
            player1.health = player1.health - 3
 
        else:   
            field.player2x = field.player2x - 1
 
 
    if field.player2x == field.res1x and field.player2y == field.res1y:
        player2.energy = player2.energy + 10
        field.res1x = 20
        field.res1y = 20
 
    if field.player2x == field.res2x and field.player2y == field.res2y:
        player2.energy = player2.energy + 10
        field.res2x = 20
        field.res2y = 20
 
    if field.player2x == field.res3x and field.player2y == field.res3y:
        player2.energy = player2.energy + 10
        field.res3x = 20
        field.res3y = 20
 
    if field.player2x == field.res4x and field.player2y == field.res4y:
        player2.energy = player2.energy + 10
        field.res4x = 20
        field.res4y = 20
 
    if field.player2x == field.res5x and field.player2y == field.res5y:
        player2.energy = player2.energy + 10
        field.res5x = 20
        field.res5y = 20
 
    if field.player2x == field.res6x and field.player2y == field.res6y:
        player2.energy = player2.energy + 10
        field.res6x = 20
        field.res6y = 20
 
    if field.player2x == field.res7x and field.player2y == field.res7y:
        player2.energy = player2.energy + 10
        field.res7x = 20
        field.res7y = 20
 
 
def rotate1_po():
    if player1.direction + 1 != 5:
        player1.direction = player1.direction + 1
    else:
        player1.direction = 1
 
 
def rotate1_protiv():
    if player1.direction - 1 != 0:
        player1.direction = player1.direction - 1
    else:
        player1.direction = 4
 
 
def rotate2_po():
    if player2.direction + 1 != 5:
        player2.direction = player2.direction + 1
    else:
        player2.direction = 1
 
 
def rotate2_protiv():
    if player2.direction - 1 != 0:
        player2.direction = player2.direction - 1
    else:
        player2.direction = 4
 
    # ------------------------------------------------------------------------------
 
 
print(
    'Правила игры: игровое поле 15 на 15. Точка - пустое поле, X - расположение вашего игрока, Y - расположение второго игрока, R - ресурсы.\n')
line()
field = field()
field.show_field(field.player1x, field.player1y, field.player2x, field.player2y, field.res1x, field.res1y, field.res2x, field.res2y,field.res3x, field.res3y, field.res4x, field.res4y, field.res5x, field.res5y, field.res6x,field.res6y,field.res7x, field.res7y)
print('Первый игрок:')
if player1.direction == 1:
    print('направление первого игрока - ▲')
 
if player1.direction == 2:
    print('направление первого игрока - ►')
 
if player1.direction == 4:
    print('направление первого игрока - ◄')
 
if player1.direction == 3:
    print('направление первого игрока - ▼')
 
print(f'Координаты первого игрока: {field.player1x + 1, 15 - field.player1y}')
 
print(f'health = {player1.health}, Energy = {player1.energy}')
 
print('\nВторой игрок:')
if player2.direction == 1:
    print('направление второго игрока - ▲')
 
if player2.direction == 2:
    print('направление второго игрока - ►')
 
if player2.direction == 4:
    print('направление второго игрока - ◄')
 
if player2.direction == 3:
    print('направление второго игрока - ▼')
 
print(f'Координаты второго игрока: {field.player2x + 1, 15 - field.player2y}')
 
print(f'health = {player2.health}, Energy = {player2.energy}')
 
while (player1.health > 0 and player1.energy>0 and player2.health>0 and player2.energy> 0):
    menu1()
    answer1 = int(input())
    while(answer1 != 1 and answer1 != 2 and answer1 !=3):
        answer1 = int(input())
    if answer1 == 1:
        move_attack_player1()
    elif answer1 == 2:
        rotate1_po()
    elif answer1 == 3:
        rotate1_protiv()
    menu2()
    answer2 = int(input())
    while(answer2 != 1 and answer2 != 2 and answer2 !=3):
        answer2 = int(input())
    if answer2 == 1:
        move_attack_player2()
    elif answer2 == 2:
        rotate2_po()
    elif answer2 == 3:
        rotate2_protiv()
    player1.energy=player1.energy-1
    player2.energy=player2.energy-1
    line()
    field.show_field(field.player1x, field.player1y, field.player2x, field.player2y, field.res1x, field.res1y, field.res2x, field.res2y,field.res3x, field.res3y, field.res4x, field.res4y, field.res5x, field.res5y, field.res6x,field.res6y,field.res7x, field.res7y)
    print('Первый игрок:')
    if player1.direction == 1:
        print('направление первого игрока - ▲')
 
    if player1.direction == 2:
        print('направление первого игрока - ►')
 
    if player1.direction == 4:
        print('направление первого игрока - ◄')
 
    if player1.direction == 3:
        print('направление первого игрока - ▼')
 
    print(f'Координаты первого игрока: {field.player1x + 1, 15 - field.player1y}')
 
    print(f'health = {player1.health}, Energy = {player1.energy}')
 
    print('\nВторой игрок:')
    if player2.direction == 1:
        print('направление второго игрока - ▲')
 
    if player2.direction == 2:
        print('направление второго игрока - ►')
 
    if player2.direction == 4:
        print('направление второго игрока - ◄')
 
    if player2.direction == 3:
        print('направление второго игрока - ▼')
 
    print(f'Координаты второго игрока: {field.player2x + 1, 15 - field.player2y}')
 
    print(f'health = {player2.health}, Energy = {player2.energy}')
print('╔═══╦══╦╗──╔╦═══╗╔══╦╗╔╦═══╦═══╗\n║╔══╣╔╗║║──║║╔══╝║╔╗║║║║╔══╣╔═╗║\n║║╔═╣╚╝║╚╗╔╝║╚══╗║║║║║║║╚══╣╚═╝║\n║║╚╗║╔╗║╔╗╔╗║╔══╝║║║║╚╝║╔══╣╔╗╔╝\n║╚═╝║║║║║╚╝║║╚══╗║╚╝╠╗╔╣╚══╣║║║\n╚═══╩╝╚╩╝──╚╩═══╝╚══╝╚╝╚═══╩╝╚╝')

