# VUB - Techniques of AI Project        #
# Further Improvements                  #
# By: Deniz Alp ATUN - 0552182          #

# Donezo List
# -----------
# Game init scaled to more than two heaps
# Tree init is scaled


# To-Do List
# -----------
# 0- SCALE EVERYTHING TO NOT BE LIMITED BY TWO HEAPS
# 0.1 - Check tree_grow function, and modulerasie it!
# 1- Find a way to not store max turn in node object
# 2- Seperate tree functions from minimax functions
# 3- Check current tree implementation and traversing
# 4- Find a better way to do exhaustive DFS for minimax

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
        self.mindex = len(move)
        self.hindex = len(heaps)

    def nodegen(self, heapin, movein):
        check = heapin - movein
        if check < 0:
            return None
        else:
            return check

    def init_tree(self, depth_lim, turnmax):  # Tricky bit of initialisation
        for i in range(len(self.root.val)):
            for j in range(len(self.move)):
                leaftest = []
                for k in range(len(self.root.val)):
                    if not k == i:
                        leaftest.append(self.root.val[k])  # To consider varying heaps, append not touched heaps

                test = self.nodegen(self.root.val[i], self.move[j])  # generates result of move
                if test is None:            # if move is invalid, leaftest is flushed to 0
                    leaftest = 0
                else:                       # if move valid, insert to proper location
                    leaftest.insert(i, int(test))

                if leaftest != 0:           # check if leaftest is a flushed one, not then create a node
                    leafnew = Node(leaftest)
                    leafnew.isturnMax = not turnmax
                    leafnew.parent = self.root
                    if len(leaftest) > 0 and all(p == 0 for p in leaftest):  # check if it is a leaf node or not
                        leafnew.isleaf = True                                # this may be redundant, will think later
                    self.root.leaf.append(leafnew)
        for i in range(len(self.root.leaf)):    # after initialisation, pass to a painful recursive function
            self.tree_grow(self.root.leaf[i], 0, depth_lim)

    def tree_grow(self, node_in, curr_depth, depth_lim):
        curr_depth += 1
        if (node_in is not None) and (curr_depth < depth_lim):
            for i in range(len(node_in.val)):
                for j in range(len(self.move)):
                    leaftest = []
                    for k in range(len(node_in.val)):
                        if not k == i:
                            leaftest.append(node_in.val[k])

                    test = self.nodegen(node_in.val[i], self.move[j])
                    if test is None:
                        leaftest = 0
                    else:
                        leaftest.insert(i, int(test))

                    if leaftest != 0:
                        leafnew = Node(leaftest)
                        leafnew.isturnMax = not node_in.isturnMax
                        leafnew.parent = node_in
                        if len(leaftest) > 0 and all(p == 0 for p in leaftest):
                            leafnew.isleaf = True
                        node_in.leaf.append(leafnew)

            for i in range(len(node_in.leaf)):
                self.tree_grow(node_in.leaf[i], curr_depth, depth_lim)

        if (node_in is not None) and (curr_depth == depth_lim):
            for i in range(len(node_in.val)):
                for j in range(len(self.move)):
                    leaftest = []
                    for k in range(len(node_in.val)):
                        if not k == i:
                            leaftest.append(node_in.val[k])

                    test = self.nodegen(node_in.val[i], self.move[j])
                    if test is None:
                        leaftest = 0
                    else:
                        leaftest.insert(i, int(test))

                    if leaftest != 0:
                        leafnew = Node(leaftest)
                        leafnew.isturnMax = not node_in.isturnMax
                        leafnew.parent = node_in
                        if len(leaftest) > 0 and all(p == 0 for p in leaftest):
                            leafnew.isleaf = True
                        node_in.leaf.append(leafnew)
                    else:
                        node_in.isleaf = True
                        break

# ///////////////// THIS IS WHERE I LEFT --- THIS IS WHERE I LEFT --- THIS IS WHERE I LEFT   \\\\\\\\\\\\\\\\\\\\\\\\\

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
