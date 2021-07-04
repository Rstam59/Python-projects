def multiplication_table(size):
    Big_list = []
    small_list = []
    t = 0
    for i in range(1, size ** 2 + 1):
        small_list.append(i)
        if len(small_list) % size == 0:
            print("a")
            small = small_list
            Big_list.append(small[:])
            small_list.clear()
    for j in range(size ** 2):
        print((Big_list[t]))
        Big_list[t].append(j)
        if len((Big_list[t])) % 3 == 0:
            t += 1

    return Big_list


# print((multiplication_table(3)))


def josephus_survivor1(n, k):
    # your code here
    place = 0
    k += 1
    k = range(1, k)
    k = list(k)
    if len(k) == 1:
        return k
    print(k)
    while len(k) > 1:
        lentgh = len(k)
        place += n - 1
        if place >= lentgh:
            while place >= lentgh:
                place -= lentgh

        k.pop(place)
        print(k)
        print(place, "place")
    return k


k = 40
n = 3
# print(josephus_survivor1(n,k))
'''
li = [
    ['R', 'R', 'R', 'R', 'R', 'R', 'R'],
    ['R', 'e', ' ', ' ', ' ', ' ', 'R'],
    ['R', ' ', ' ', ' ', ' ', ' ', 'R'],
    ['R', ' ', 'R', 'R', 'R', ' ', 'R'],
    ['R', ' ', 'g', 'R', 'l', ' ', 'R'],
    ['R', 'R', 'R', 'R', 'R', 'R', 'R']
]
for row in range (len(li)):
    for column in range(len(li)) :
        if li[row][column] == "e":
            e_place=[row,column]
        elif li[row][column] == "g":
            g_place = [row,column]
        elif li[row][column] == "l":
            l_place = [row,column]
while True:
    if g_place[0] > e_place[0]:
        g_place[0] = g_place[0] - 1
        print(li[g_place[0]][g_place[1]])
        if li[g_place[0]][g_place[1]] == "R":
            g_place[0] = g_place[0] + 1
         #   print(g_place)
    elif g_place[0] < e_place[0]:
        g_place[0] = g_place[0] + 1
        if li[g_place[0]][g_place[1]] == "R":
            g_place[0] = g_place[0] - 1
            print(g_place)
    elif g_place[1] > e_place[1]:
        g_place[1] = g_place[1] - 1
        if li[g_place[0]][g_place[1]] == "R":
            g_place[1] = g_place[1] + 1
            print(g_place)
    elif g_place[1] < e_place[1]:
        g_place[1] = g_place[1] + 1
        print(g_place)
        if li[g_place[0]][g_place[1]] == "R":
            g_place[1] = g_place[1] - 1
            print(g_place)
    if g_place == e_place:
        print(li)
        print("yee")
        break

    if li[g_place[0]-1][g_place[1]] != "R":
        g_place[0] = g_place[0] - 1
        print(g_place)
        continue
    elif li[g_place[0]][g_place[1]-1] != "R":
        g_place[1] = g_place[1] - 1
        print(g_place)
        continue
    elif li[g_place[0]][g_place[1]+1] != "R":
        g_place[1] = g_place[1] + 1
        print(g_place)
        continue
    elif li[g_place[0]+1][g_place[1]] != "R":
        g_place[0] = g_place[0] + 1
        print(g_place)
        continue
'''
'''
class Stuffs():
    def __init__(self):
        self.List = []

    def push(self,reqem):
        self.List.append(reqem)

    def show(self):
        print(self.List)
class Pop(Stuffs):
    Stuffs.__init__
    Stuffs.push
    def poping(self):
        self.List.pop()
testing=Stuffs()
testing.push(3)
(testing.push(3))

testing.show()
take_out=Pop()
take_out.poping()
take_out.show()
'''
#george=Cats("george",5)
#print(george.age)
#print(george.calling())
#print(Cats.adding_stuffs(3,4))
#mayau=Cats("mayau",3)
#print(mayau.idk)
'''
class Instead:
    def __init__(self):
        self.my_list = []
    def push(self,num):
        self.my_list.append(num)
    def show(self):
        print(self.my_list)
class Delet(Instead):
    def poper(self):
        self.my_list.pop()

ins = Delet()
ins.push(3)
ins.push(3)
ins.show()
ins.poper()
ins.show()
'''
'''
Big_list=[]
little_list=[]
for i in range (1,26):
    if len(little_list) % 4 == 0 and len(little_list) != 0:
        little_list.append(i)
        Big_list.append(little_list[:])
        print(little_list)
        little_list.clear()
    else:
        little_list.append(i)

Big_list[len(Big_list)/2][len(Big_list)/2] = 1
print(Big_list)
'''
'''
print(list(map(lambda x : x * 2, [1,2,3])))
print(list(filter(lambda x : x % 2 == 0, [1,2,3])))
from functools import reduce
print(reduce(lambda acc,x:x+acc,[1,2,3]))
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(list(set(x for x in some_list if some_list.count(x) > 1)))
'''
'''
def decoretor(func):
    def wrapper(*args):
        print("*" * len(*args))
        func(*args)
        print("*" * len(*args))
    return wrapper
@decoretor
def fancy_word(word):
    print(word)
fancy_word("so it doesnt matter what the fuck im saying")
fancy_word("asdadsfgn")
'''
'''
class Students:
    def __init__(self,age,name,course):
        self.age=age
        self.name=name
        self.course = course
    def __repr__(self):
        return repr((self.age, self.name, self.course))


student = Students(20,"rustem",4)
student1 = Students(19,"asd",3)
student2 = Students(100,"aasd",13)
students=[student,student1,student2]
print(sorted(students,key=lambda x:x.age,reverse=True))


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda x: x[2],reverse=True))   # sort by age

'''
def add_5(num):
    return num + 5