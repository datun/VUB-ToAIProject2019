# VUB - Techniques of AI Project        #
# Further Improvements                  #
# By: Deniz Alp ATUN - 0552182          #

import time
import tree_stuff as tree


class NIMgame(object):
    def __init__(self):  # init the NIM game
        self.hcount = 2
        self.heaps = []
        self.move = [1, 2]
        self.isturnMax = True
        self.depth = 0
        self.treeInit = False
        self.piletotal = 0

    def heapgen(self, hnum):
        for i in range(hnum+1):
            self.heaps.append(int(0))

    def heapsize(self, hsize, hpos):  # define the amount in given heap
        self.heaps[hpos] = hsize
        self.piletotal += hsize

    def moves(self, listin):  # define moves (removing 1,2 or 3 from one pile for example)
        for i in listin:
            self.move.append(int(i))

    def gameover(self):
        if self.piletotal <= 0:
            return True
        else:
            return False


'''
class PlayerNim(object):
    def __init__(self, iname):
        self.name = iname
        self.map = None

    def map(self, tree):
        self.map = tree.minimaxmap()

    def update(self, nodein):
        for index in self.map.root.leaf:
            if index.val == nodein:
                self.map.root = index

    def play(self):
        if (self.name == "MAX") and self.map.root.isturnMax:
            play = self.map.root.leaf[0]
            for index in self.map.root.leaf:
                if play.score < max(play.score, index.score):
                    play = index
                    continue
        else:
            play = self.map.root.leaf[0]
            for index in self.map.root.leaf:
                if play.score > min(play.score, index.score):
                    play = index
                    continue
        self.update(play)
        return play
'''

gamestart = NIMgame()
print("########## NIMGAME INIT ##########")
print("By default there are two heaps to play!")

while True:
    hnum = input("Type number of heaps to play: ")
    if hnum.isdigit():
        if int(hnum) > 0:
            gamestart.heapgen(int(hnum))
            break
        else:
            print("Number of heaps cannot be zero or lower!")
    else:
        print("Input is not a digit!")


for i in range(len(gamestart.heaps)):
    while True:
        nhsize = input("Type pile size for heap " + str(i) + " :")
        if nhsize.isdigit():
            gamestart.heapsize(int(nhsize), i)
            break
        else:
            print("Input is not a digit!")

while True:
    nmoves = input("Type moves seperated by space: ")
    templist = nmoves.split()
    checker = True
    for i in templist:
        if not i.isdigit():
            checker = False
    if checker:
        gamestart.moves(templist)
        break
    else:
        print("One of the inputs is not a digit!")

gametree = tree.NIMTree(gamestart.heaps, gamestart.move, True)

while True:
    tdepth = input("Type depth limit for tree generation: ")
    if not tdepth.isdigit():
        print("Input is not a digit!")
    else:
        gametree.init_tree(int(tdepth), True)
        break

print("\n########## MINIMAX INIT ##########")

print("########## PLAY ##########")
timetup = time.gmtime()
unique = time.strftime('%H-%M-%S', timetup)
print(unique)
filename = "movesfile_" + unique
print(filename)
file = open(filename + ".txt", "w+")



file.write("Player " + x + " Lost!")
print("Game over! Player " + x + " lost the game!")
file.close()
