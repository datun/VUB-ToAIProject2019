# VUB - Techniques of AI Project        #
# Further Improvements                  #
# By: Deniz Alp ATUN - 0552182          #


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
