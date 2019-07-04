# VUB - Techniques of AI Project        #
# Start: 2019/04/10                     #
# By: Deniz Alp ATUN - 0552182          #

import minimax_heap2 as minimax
import time


class NIMgame(object):
    def __init__(self):  # init the NIM game
        self.hcount = 2
        self.heaps = [0, 0]
        self.move = [1,2]
        self.isturnMax = True
        self.depth = 0
        self.treeInit = False
        self.piletotal = 0

    def heap_poscheck(self, hpos):  # check if the given heap position is valid
        if 0 <= hpos < self.hcount:
            return True
        else:
            return False

    def heapsize(self, hsize, hpos):  # define the amount in given heap
        if self.heap_poscheck(hpos):
            self.heaps[hpos] = hsize
            self.piletotal += hsize
        else:
            print("Invalid heap position")

    def moves(self, listin):  # define moves (removing 1,2 or 3 from one pile for example)
        for i in listin:
            self.move.append(int(i))

    def gameover(self):
        if self.piletotal <= 0:
            return True
        else:
            return False

    def new_nimtree(self, heaps, move, turnmax):
        if not self.treeInit:
            turnmax = True
            nimtree = minimax.NIMTree(heaps, move, turnmax)
            while True:
                depth = input("Input a digit to limit the depth of NIM Tree. (0 is not a valid input!): ")
                if depth.isdigit():
                    if int(depth) != 0:
                        self.depth = int(depth)
                        nimtree.init_nimtree_gen(nimtree.root, int(depth), turnmax)
                        break
                    else:
                        print("Input is invalid!")
            self.treeInit = True
            nimtree.minimaxmap()
        else:
            nimtree = minimax.NIMTree(heaps, move, turnmax)
            nimtree.init_nimtree_gen(nimtree.root, self.depth, turnmax)
            nimtree.minimaxmap()
            print("Minimax tree has been generated!\n")
        return nimtree

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


def comp_play(nodein):
    if nodein.isleaf and nodein.val != [0, 0]:  # compute new minimax tree, since tree ended before game ended.
        minimax_tree = gamestart.new_nimtree(nodein.val, gamestart.move, gamestart.isturnMax)
        gamestart.heaps = minimax_tree.root.val
        gamestart.piletotal = gamestart.heaps[0] + gamestart.heaps[1]
        return minimax_tree.root
    else:
        if gamestart.isturnMax:  # MAX turn
            x = "MAX"
            file.write("Turn of: Player " + x + "\n")
            file.write("-------------------------------\n")
            file.write("Current Node:      [" + str(nodein.val[0]) + "," + str(nodein.val[1]) + "]   " +
                       "Current NIM-sum:       " + str(nodein.val[0] ^ nodein.val[1]) + "   " + "\n")
            j = nodein.leaf[0]
            for i in nodein.leaf:  # get MAX score from all possible moves
                file.write(
                    "Available Node:  [" + str(i.val[0]) + "," + str(i.val[1]) + "]   MINIMAX Val: " + str(i.score) + "\n")
                if j.score < max(j.score, i.score):
                    j = i
                    continue
            gamestart.heaps = j
            gamestart.piletotal = j.val[0] + j.val[1]
            gamestart.isturnMax = False
        else:  # MIN turn
            x = "MIN"
            file.write("Turn of: Player " + x + "\n")
            file.write("-------------------------------\n")
            file.write("Current Node:      [" + str(nodein.val[0]) + "," + str(nodein.val[1]) + "]   " +
                       "Current NIM-sum:       " + str(nodein.val[0] ^ nodein.val[1]) + "   " + "\n")
            j = nodein.leaf[0]
            for i in nodein.leaf:  # get MIN score from all possible moves
                file.write(
                    "Available Node:  [" + str(i.val[0]) + "," + str(i.val[1]) + "]   MINIMAX Val: " + str(i.score) + "\n")
                if j.score > min(j.score, i.score):
                    j = i
                    continue
            gamestart.heaps = j
            gamestart.piletotal = j.val[0] + j.val[1]
            gamestart.isturnMax = True
        file.write("Chosen Node:       [" + str(j.val[0]) + "," + str(j.val[1]) + "]   " +
                   "Chosen Node NIM-sum:   " + str(j.val[0] ^ j.val[1]) + "   " + "\n")
        file.write("-------------------------------\n")
        file.write("\n\n")
        return j


gamestart = NIMgame()
print("########## NIMGAME INIT ##########")
print("By default there are two heaps to play!")

for i in range(2):
    while gamestart.heaps[i] == 0:
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

print("\n########## MINIMAX INIT ##########")

minimax_tree = gamestart.new_nimtree(gamestart.heaps, gamestart.move, gamestart.isturnMax)
nodein = minimax_tree.root

print("########## PLAY ##########")
timetup = time.gmtime()
unique = time.strftime('%H-%M-%S', timetup)
print(unique)
filename = "movesfile_" + unique
print(filename)
file = open(filename + ".txt", "w+")

checker = comp_play(nodein)
while not gamestart.gameover():
    checker = comp_play(checker)

if not gamestart.isturnMax:
    x = "MAX"
else:
    x = "MIN"

file.write("Player " + x + " Lost!")
print("Game over! Player " + x + " lost the game!")
file.close()
