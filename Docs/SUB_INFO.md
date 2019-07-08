# Submitted Project Information

In this project, it is aimed to implement minimax algorithm to a modified version of NIM game.

The reason I’ve chosen to use NIM game is that tic-tac-toe is almost synonymous with minimax algorithm. NIM game allows us to observe minimax algorithm with proof that it works, since NIM game has a mathematical solution one can cross-check moves with result of given solution.

## Index
* [Information about Minimax algorithm](##information-about-minimax-algorithm)
* [Information about NIM Game and solution](##information-about-NIM-game-and-solution)
* [Information about modified NIM Game and solution](##information-about-modified-NIM-Game-and-solution)
  - [Problems Caused by modification](###Problems-Caused-by-modification)
* [How proof of correct implementation is provided](##How-proof-of-correct-implementation-is-provided)
* [Addendum](##Addendum)

## Information about Minimax algorithm

Minimax algorithm is an algorithm that maximises the worst case scenario for player MAX. To do so, it is using exhaustive depth first search and assign minimax values that are assigned by utility function.

After assigning values to the given end states (one may consider them as leaf), as traversing from leaf to root occurs depending on the value of child nodes and whose turn it is on the game, either maximum or minimum of it is assigned to that current node.

## Information about NIM Game and solution

There are multiple variation of NIM games. In general, two players take turns in removing objects from distinct piles. On each turn, player can only remove objects from one pile and must remove at least one object. Goal is avoiding from being the player who takes last object, this is called misère nim game.

NIM game has been mathematically solved. Before solution, a definition of nim-sum is required: Nim-sum is XORing the heaps or in other words XORing binary values of heaps.

Solution to game is always finishing a turn with nim-sum of 0. This is always possible if a given turn is not starting with nim-sum of 0, if that is the case, until other player makes a mistake it is impossible to win.

## Information about modified NIM Game and solution
In this project we are using modified version of a NIM game. Restrictions are as follows:  
* Two piles only 
* Four object removing moves, two default (1 and 2) and two user inputted (can be same moves).

### Problems Caused by modification
The restriction of removing moves mean that it is not easy to reach nim-sum of 0 state.  
Meaning that game can be separated into two different states.  
Before reaching nim-sum zero (B⊕0) and After reaching nim-sum zero (A⊕0).

This means that when game is in state of A⊕0, utility function must be used.

If we are in the state of B⊕0, then we need to use an evaluation function.  
Purpose of evaluation function is to observe the current state it is in, find closest nim-sum zero state and evaluate on how many turns one player can reach that state and which player is that.

Since the game is limited to two heaps, closest nim-sum zero state is when heaps are equal.

Pushing the not ideal case concept, another state is one heap is emptied and other is full.  
For this case the winning strategy is being the first player who leaves 1 object on the board.  
Another wording is being first player who reaches max(Move-List)+1 state in the heaps.  
(This case is also known as Subtraction game)

**Conclusion**  
3 cases to consider:  
*Case (1)* - Case of nim-sum zero state is reachable  
*Case (2)* - Case of one heap is empty (Subtraction game – variation of NIM)  
*Case (3)* - Case of nim-sum zero state is unreachable

Aside for considering these cases, since basis is still NIM game solution is still checking whether player is on nim-sum zero state or not.

## How proof of correct implementation is provided

While players are making choices, an output is written to a text file depending on the case game is in. Below are the outputs that are included in every step and why they are included.
* Current node
* Current nodes utility function result without minimax value: (modulo or nim-sum result) To understand the state player is in
* Available node choices and their minimax value
* The node they’ve chosen to proceed
* Chosen nodes utility function result without minimax value: (modulo or nim-sum result) To check if choice is correct and minimax is correct accordingly.

Due to the nature of NIM game, positions are binary. They are either a winning positions or losing positions. The only case that contradicts with this statement is **Case (3).**  
This allows us to see if any given move is best move among the others or not.  
Also, utility functions include a score 20 for whenever there is a suboptimal play to be made.  
Finally, NIM game states that as long as you do not start from nim-sum zero position first player ALWAYS wins and in the case of nim-sum zero position, first player ALWAYS loses.  
This also allows us to compare the known result with the output of our code and see where it went wrong.

## Addendum

* Cases are scoring the state of the given heap to create the minimax mapping. Score for correct play is +- 10, wrong play +- 20, terminal state +- 100.  
Meaning that output should never encounter +-20 if everything is correct.
* In Case 3, most optimal play would cause a loop that eventually creates a Case 2. Because of that utility function is modified so that their goal is to reach nim-sum zero state instead of winning the game.


