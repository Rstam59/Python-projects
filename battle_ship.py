from random import randint

temp_list = []
major_list = []
for _ in range(10):
    for _ in range(10):
        temp_list.append("O")
    major_list.append(temp_list[:])
    temp_list.clear()


class BattleShip:
    def __init__(self, size):
        self.size = size

    def create_ship(self):
        move = 0
        x = randint(0, 9)
        y = randint(0, 9)
        direction = randint(0, 1)
        increase_decrease = randint(0,1)
        major_list[x][y] = "X"
        for _ in range(self.size - 1):
            if direction == 0:
                if increase_decrease == 1:
                    y += 1 #8,9,10
                    move -= 1#-1,-2,-3
                    if y > 9 or major_list[x][y] == "X":
                        increase_decrease = 0
                        y += move-1#7
                    major_list[x][y] = "X"
                else:
                    y -= 1
                    move += 1
                    if y < 0 or major_list[x][y] == "X":
                        increase_decrease = 1
                        y += move + 1
                    major_list[x][y] = "X"
            else:
                if increase_decrease == 1:
                    x += 1
                    move -= 1
                    if x > 9 or major_list[x][y] == "X":
                        increase_decrease = 0
                        x += move-1
                    major_list[x][y] = "X"
                else:
                    x -= 1
                    move += 1
                    if x < 0 or major_list[x][y] == "X":
                        increase_decrease = 1
                        x += move + 1
                    major_list[x][y] = "X"
    def unvalid_place(self):
        for i in range(10):
            for j in range(10):
                if major_list[i][j] == "X":
                    print("entered")
                    if i + 1 <= 9 and major_list[i + 1][j] != "X":
                        print(i)
                        major_list[i+1][j] = "*"
                    if major_list[i-1][j] != "X" and i-1 >= 0:
                        print(i)
                        major_list[i-1][j] = "*"
                    if j + 1 <= 9 and major_list[i][j + 1] != "X":
                        print(j)
                        major_list[i][j+1] = "*"
                    if major_list[i][j-1] != "X" and j-1 >= 0:
                        print(j)
                        major_list[i][j-1] = "*"


ship_4 = BattleShip(4)
ship_4.create_ship()
ship_4.unvalid_place()
ship_4 = BattleShip(3)
ship_4.create_ship()
ship_4.unvalid_place()
for i in major_list:
    print(i)
