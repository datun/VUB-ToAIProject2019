# VUB - Techniques of AI Project        #
# Start: 2019/04/10                     #
# By: Deniz Alp ATUN - 0552182          #


class Node(object):
    def __init__(self, val):
        self.parent = None
        self.leaf = []
        self.val = val
        self.visited = False
        self.isleaf = False
        self.isturnMax = True
        self.score = 0


class NIMTree(object):
    def __init__(self, heaps, move, maxstart):  # init the NIM game
        self.root = Node(heaps)
        self.root.isturnMax = maxstart
        self.move = move
        self.initialise = False

    def nim_nodegen(self, heaps, movein, index):
        if index < len(self.move):
            check = heaps[0] - movein
            if check < 0:
                return 0
            else:
                result = [check, heaps[1]]
        else:
            check = heaps[1] - movein
            if check < 0:
                return 0
            else:
                result = [heaps[0], check]
        return result

    def init_nimtree_gen(self, node_in, depth_lim, turnmax):
        if not self.initialise:
            for i in range(len(self.move) * len(self.root.val)):
                leaftest = self.nim_nodegen(node_in.val, self.move[i % len(self.move)], i)
                if leaftest != 0:
                    leafnew = Node(leaftest)
                    leafnew.isturnMax = not turnmax
                    leafnew.parent = self.root
                    if leaftest == [0, 0]:
                        leafnew.isleaf = True
                    self.root.leaf.append(leafnew)
            self.initialise = True
            for i in range(len(self.root.leaf)):
                self.nim_treegen(self.root.leaf[i], 0, depth_lim)

    def nim_treegen(self, node_in, curr_depth, depth_lim):
        curr_depth += 1
        if (node_in is not None) and (curr_depth < depth_lim):
            for i in range(len(self.move) * len(node_in.val)):
                leaftest = self.nim_nodegen(node_in.val, self.move[i % len(self.move)], i)
                if leaftest != 0:
                    leafnew = Node(leaftest)
                    leafnew.isturnMax = not node_in.isturnMax
                    leafnew.parent = node_in
                    if leaftest == [0, 0]:
                        leafnew.isleaf = True
                    node_in.leaf.append(leafnew)
            for i in range(len(node_in.leaf)):
                self.nim_treegen(node_in.leaf[i], curr_depth, depth_lim)

        if (node_in is not None) and (curr_depth == depth_lim):
            for i in range(len(self.move) * len(node_in.val)):
                leaftest = self.nim_nodegen(node_in.val, self.move[i % len(self.move)], i)
                if leaftest != 0:
                    leafnew = Node(leaftest)
                    leafnew.parent = node_in
                    leafnew.isturnMax = not node_in.isturnMax
                    leafnew.isleaf = True
                    node_in.leaf.append(leafnew)
                else:
                    node_in.isleaf = True
                    break

    @staticmethod
    def traverse(node_in, index):
        if len(node_in.leaf) != 0:
            if (node_in.val[0] == 0) and (node_in.val[1] == 0):
                return False
            if index in range(len(node_in.leaf)):
                return node_in.leaf[index]

    '''
    # Use something similar to this to further cleanup minimaxmap function!
    def visitedprocessor(self, node_in, turn):
        if len(node_in.leaf) != 0:
            for i in node_in.leaf:
                if not i.visited:
                    turn += 1
                    return i

        if node_in.visited:
            turn -= 1
            return node_in.parent
        if node_in is None:
            return
    '''

    def minimaxmap(self):  # For now we visited only the left most node
        i = self.traverse(self.root, 0)
        j = None
        turn = not self.root.isturnMax
        while i:
            j = i
            i = self.traverse(i, 0)
            turn = not turn

        # we've traversed to the left most leaf.

        while j is not None:  # If we haven't reached roots parent
            if j.visited:
                if len(j.leaf) != 0:
                    for i in j.leaf:
                        if not i.visited:
                            j = i
                            turn = not turn
                            break
                if j.visited:
                    j = j.parent
                    turn = not turn
                if j is None:
                    break
            else:
                if j.isleaf:
                    if j.isturnMax:  # if it is MAX turn
                        j.score = casedetecter(j.val, self.root.val, self.move, True)
                        j.visited = True
                    else:  # if it is MIN turn
                        j.score = casedetecter(j.val, self.root.val, self.move, False)
                        j.visited = True
                else:
                    check = 0
                    for i in j.leaf:
                        if i.visited:
                            check += 1
                    if check != len(j.leaf):
                        for i in j.leaf:
                            if not i.visited:
                                j = i
                                turn = not turn
                                break

                    if check == len(j.leaf):
                        if j.isturnMax:  # if it is MAX turn
                            for i in j.leaf:
                                if j.score == 0:
                                    j.score = i.score
                                    continue
                                else:
                                    j.score = max(j.score, i.score)
                                j.visited = True
                        else:  # if it is MIN turn
                            for i in j.leaf:
                                if j.score == 0:
                                    j.score = i.score
                                    continue
                                else:
                                    j.score = min(j.score, i.score)
                                j.visited = True


def casedetecter(heapnow, heapinit, movelist, turnmax):
    if min(heapinit) == 0 and max(heapinit) != 0:
        result = utilcase2(max(heapnow), max(movelist), turnmax)
    elif abs(heapinit[0] - heapinit[1]) <= max(movelist):
        result = utilcase1(heapnow, turnmax)
    else:  # it should only check case 3, it satisfies initial condition
        if abs(heapnow[0] - heapnow[1]) <= max(movelist):  # checks if we've passed heap[0] == heap[1] while DFS
            result = utilcase1(heapnow, turnmax)    # if passed, it is back to case1. Else case2.
        else:
            result = utilcase3(heapnow, max(movelist), turnmax)
    return result


def utilcase1(heaps, turnmax):
    if heaps == [0, 0]:
        utilres = 100
    elif not (heaps[0] ^ heaps[1]):
        utilres = -10
    else:
        utilres = 20

    if turnmax:
        return utilres
    else:
        return -utilres


def utilcase2(theheap, maxmove, turnmax):
    if theheap == 0:
        utilres = 100
    elif theheap % (maxmove+1):
        utilres = -10
    else:
        utilres = 20

    if turnmax:
        return utilres
    else:
        return -utilres


def utilcase3(heaps, maxmove, turnmax):
    if heaps[0] == heaps[1]:
        utilres = 100
    elif max(heaps) % (maxmove+1):
        utilres = -10
    else:
        utilres = 20

    if turnmax:
        return utilres
    else:
        return -utilres


'''
heapsTest = [2, 2]
moves = [1, 2]
test = NIMTree(heapsTest, moves, True)
test.init_nimtree_gen(test.root, 9, True)  # depth_lim cannot be 0.
test.minimaxmap()
print("Mapping Done!")
'''


# TO-DO LIST:
# -----------
# after backup, try to tidy up the code
# Scale this code for cases not restricted to 2 heaps / 2 moves
