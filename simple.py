from random import randint

battle_map = []
little_list = []
for _ in range(0, 10):
    for _ in range(0, 10):
        little_list.append("O")
    battle_map.append(little_list[:])
    little_list.clear()
for row in battle_map:
    pass
    # print(row)


class Ship:
    def __init__(self, size):
        self.size = size

    def create_ship(self):
        move = 0
        pos = randint(0, 0)
        direc = randint(0, 1)
        x = randint(0, 9)
        y = randint(0, 9)
        battle_map[x][y] = "X"
        print(y)


ship1 = Ship(4)
ship1.create_ship()



