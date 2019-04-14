# VUB - Techniques of AI Project        #
# Start: 2019/04/10                     #
# By: Deniz Alp ATUN (github.com/mivvv) #


class NIMgame(object):
    def __init__(self, pnum):  # init the NIM game
        if pnum > 0:
            self.playercount = pnum
            self.hcount = 0
            self.heaps = []
            self.move = []
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
        self.move = [r1, r2, r3]

    def play(self, hnum, mnum):
        if self.heapPosCheck(hnum) and mnum in range(0, 3):
            if self.heaps[hnum] == 0:
                print("Heap is empty, invalid move!")
            elif 0 > (self.heaps[hnum] - self.move[mnum]):
                print("Invalid move! Heap cannot be reduced beyond zero!")
            else:
                self.heaps[hnum] -= self.move[mnum]
                self.heaptotal -= self.move[mnum]
                self.turncount += 1
        else:
            print("Invalid move!")

    def gameover(self):
        if self.heaptotal == 0:
            return True
        else:
            return False


nplay = input("Type number of players: ")
gamestart = NIMgame(int(nplay))
temp = input("Type number of heaps to play: ")
nheaps = int(temp)
gamestart.heapCount(nheaps)
for i in range(nheaps):
    nhsize = input("Type heap size for heap " + str(i) + " :")
    gamestart.heapSize(int(nhsize), i)
nmoves = input("Type 3 moves seperated by space: ")
templist = nmoves.split()
gamestart.moves(int(templist[0]), int(templist[1]), int(templist[2]))

print("########## LET THE GAMES BEGIN ##########")

while not gamestart.gameover():
    for i in range(nheaps):
        print("Heap " + str(i) + ": " + str(gamestart.heaps[i]))
    for i in range(3):
        print("Move " + str(i) + ": " + str(gamestart.move[i]))

    player = input("Player " + str(gamestart.turncount % int(nplay)) + " type heap number and move number: ")
    templist = player.split()
    gamestart.play(int(templist[0]), int(templist[1]))

# Fix the move choices to
# EITHER prevent deadlock moves ( moves 2-3-5 prevents end game of heap size 1 )
# OR due to deadlocks if there is no other move to make consider it as endgame
