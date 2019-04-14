# VUB - Techniques of AI Project        #
# Start: 2019/04/10                     #
# By: Deniz Alp ATUN (github.com/mivvv) #


class NIMgame(object):
    def __init__(self, pnum):  # init the NIM game
        if pnum > 0:
            self.playercount = pnum
            self.hcount = 0
            self.heaps = []
            self.move = [1]
            self.turncount = 0
            self.heaptotal = 0
        else:
            print("Invalid player number")

    def heapCount(self, hnum):  # define number of heaps to play
        self.hcount = hnum
        self.heaps = [0] * hnum

    def heapPosCheck(self, hpos):  # check if the given heap position is valid
        if 0 <= hpos < self.hcount:
            return True
        else:
            return False

    def heapSize(self, hsize, hpos):  # define the amount in given heap
        if self.heapPosCheck(hpos):
            self.heaps[hpos] = hsize
            self.heaptotal += hsize
        else:
            print("Invalid heap position")

    def moves(self, r1, r2, r3):  # define moves (removing 2, 3 or 5 from one pile for example)
        self.move = [1, r1, r2, r3]
        # move 1 is added as a default since:
        # without it: one has to force users to input pile sizes that are divisible by moves to prevent deadlocks
        # with it: user can define any pile size or move without constraints

    def play(self, hnum, mnum):
        if self.heapPosCheck(hnum) and mnum in range(0, 3):
            if self.heaps[hnum] == 0:
                print("Invalid move! Cannot reduce an empty heap.")
                return False
            elif 0 > (self.heaps[hnum] - self.move[mnum]):
                print("Invalid move! Heap cannot be reduced beyond zero!")
                return False
            else:
                self.heaps[hnum] -= self.move[mnum]
                self.heaptotal -= self.move[mnum]
                self.turncount += 1
                return True
        else:
            print("Invalid move!")
            return False

    def gameover(self):
        if self.heaptotal == 0:
            return True
        else:
            return False


while True:
    nplay = input("Type number of players: ")
    if nplay.isdigit():
        gamestart = NIMgame(int(nplay))
        nplay = int(nplay)
        break
    else:
        print("Input is not a digit!")

while True:
    nheaps = input("Type number of heaps to play: ")
    if nheaps.isdigit():
        gamestart.heapCount(int(nheaps))
        nheaps = int(nheaps)
        break
    else:
        print("Input is not a digit!")

while True:
    nmoves = input("Type 3 moves seperated by space: ")
    templist = nmoves.split()
    checker = True
    for i in templist:
        if not i.isdigit():
            checker = False
    if checker:
        gamestart.moves(int(templist[0]), int(templist[1]), int(templist[2]))
        break
    else:
        print("One of the inputs is not a digit!")


for i in range(nheaps):
    while gamestart.heaps[i] == 0:
        while True:
            nhsize = input("Type heap size for heap " + str(i) + " :")
            if nhsize.isdigit():
                gamestart.heapSize(int(nhsize), i)
                break
            else:
                print("Input is not a digit!")

print("########## LET THE GAMES BEGIN ##########")

while not gamestart.gameover():
    for i in range(nheaps):
        print("Heap " + str(i) + ": " + str(gamestart.heaps[i]))
    for i in range(4):
        print("Move " + str(i) + ": " + str(gamestart.move[i]))
    while True:
        player = input("Player " + str(gamestart.turncount % int(nplay)) + " type heap number and move number: ")
        templist = player.split()
        if templist[0].isdigit() and templist[1].isdigit:
            checker = gamestart.play(int(templist[0]), int(templist[1]))
            if checker:
                break
        else:
            print("One of the inputs is not a digit!")

print("Game over! Player " + str((gamestart.turncount - 1) % int(nplay)) + " lost the game!")

