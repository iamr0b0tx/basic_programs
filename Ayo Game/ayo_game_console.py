import random

class ayoGame:
    ayoBoard = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]   

    Id = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]

    listOfPlayers = ["player1","player2"]    #list of players
    game_over = True   #this tracks the game
    
    def __init__(self):
        print("!!!Ayo Game!!!")
        print("This is the Ayo board")

        #this shows the board
        self.displayBoard()
        
        print("This are the numbers for play")
        self.displayBoard(self.Id)

        #this gets the player names
        self.begin_game()

    def begin_game(self):
        #this prvides the choice of single player agains the computer or multiplayer
        choice = input("Type in 's' for single player and 'm' for multiplayer: ").lower()
        while choice != 's' and choice != 'm':
            choice = input("Type in  's' for single player and 'm' for multiplayer: ").lower()

        if choice == 's':
            self.listOfPlayers[0] = input("Type in your name: ").lower()
            self.listOfPlayers[1] = "computer"
            
        else:
            for player_index in range(len(self.listOfPlayers)):
                self.listOfPlayers[player_index] = input("type in a name for player %d: "%(player_index+1)).lower()
                
        self.piecesWon = {player:0 for player in self.listOfPlayers}   #initializes the score board
        self.currentPlayer = self.listOfPlayers[0]  #sets the current player

        #shows the board before the play
        self.displayBoard(self.ayoBoard)

        self.getMove()    #play
        
    def getMove(self):
        if self.game_over:

            #if the computer is the first player run move for the minmax
            if self.currentPlayer == "computer":
                self.play()
                
            else:
                pick = input("type in pick position(according to Id [1-6]) for %s: "%(self.currentPlayer)) #pick a hole to pack
                while type(pick) != int:
                    try:
                        pick = int(pick)
                    except Exception as excep:
                        print("Please Type in a Valid Input!!!")
                        pick = input("type in pick position(according to Id [1-6]) for %s: "%(self.currentPlayer))
                        
                self.play(pick)
                
        else:
            print("Game Over!")

    def displayBoard(self, List=False):
        li = []
        if List == False: List = self.ayoBoard.copy()
        for i in range(2):
            li.append(List[0:6])
            List.reverse()
            
        print("")
        for x in li:
            print(x)
        print("")


    def play(self, pick=False, run_mm=True):
        pick -= 1
        if self.listOfPlayers.index(self.currentPlayer) == 1:
            pick = 5 - pick
            pick += 6

        #if cumputer is playing and the minmax is false---run the minmax
        if self.currentPlayer == "computer" and run_mm:
            input("press Enter for computer to play")
            b = self.ayoBoard.copy()
            r = minmax(5, self.currentPlayer, b, self.piecesWon.copy())
            pick = r[0]
            print(r)
##            if self.currentPlayer == "computer":
##                while play(pick, b, self.currentPlayer, self.piecesWon.copy())[0] == False:
##                    pick = random.randint(1,7)

            print("\n!!!computer packed Hole %d!!!\n"%(pick))
            input("press Enter to continue")        
            #use the minmax move
            self.play(pick, False)
            
        else:
            #packs the seed in the selected position
            hand = self.ayoBoard[pick]
            self.ayoBoard[pick] = 0

            #move to the next hole
            p = (pick - 1)%12

            #if the hand packs empty hole----play again to pack
            if hand == 0:
                print("Empty Hole, Play again!")
                self.getMove()
                
            else:
                while hand:
                    #drop in hole
                    self.ayoBoard[p] += 1
                    hand -= 1

                    #if hand is empty        
                    if hand == 0:
                        w = p
                        
                        #while the hole ---piecesWon are 2 0r 3, in opponents territory keep packing
                        while self.ayoBoard[w] in [2,3] and (w in range((6*((self.listOfPlayers.index(self.currentPlayer)+1)%2)),(6*(((self.listOfPlayers.index(self.currentPlayer)+1)%2)+1)),1)):
                            self.piecesWon[self.currentPlayer] += self.ayoBoard[w]
                            self.ayoBoard[w] = 0
                            w = (w + 1)%12

                        #if the last hole dropped in is not empty pack again
                        if self.ayoBoard[p] > 1:
                            hand += self.ayoBoard[p]
                            self.ayoBoard[p] = 0

                    #if not show board to track game state       
                    self.displayBoard()
                    
                    #move    
                    p = (p - 1)%12

                    #this condition checks for end of game---if diff[player1 and player2] > piecesWon left or board is empty or opponent unable to play
                    li = [x for x in self.piecesWon.values()]
                    nextPlayer = self.listOfPlayers[(self.listOfPlayers.index(self.currentPlayer)+1)%2]
                    if sum(self.ayoBoard) == 0 or (sum(self.ayoBoard[(6*(self.listOfPlayers.index(nextPlayer))):(6*(self.listOfPlayers.index(nextPlayer)+1))]) == 0) or abs(li[0] - li[1]) > sum(self.ayoBoard):
                        self.ayoBoard = [0 for a in range(12)]

                        #check for max----winner
                        x = 0
                        for p in self.piecesWon:
                            if self.piecesWon[p] > x:
                                x = self.piecesWon[p]
                                value = p
                            print("%s has %s piece(s)"%(p, self.piecesWon[p]))
                        print("Game Over, ",end="")
                        if(self.piecesWon[self.listOfPlayers[(self.listOfPlayers.index(value)+1)%2]] == x):
                            print("!!!DRAW!!!")
                        else:
                            print("{} wins the game!".format(value))

                        #sets the hand empty and game state False---Game over
                        hand = 0
                        self.game_over = False

                print(self.piecesWon)
                self.currentPlayer = self.listOfPlayers[(self.listOfPlayers.index(self.currentPlayer)+1)%2]
                if ("computer" in self.listOfPlayers):
                    if (self.listOfPlayers[(self.listOfPlayers.index(self.currentPlayer)+1)%2] == "computer"):
                        self.getMove()
                        
                    else:
                        self.play()
                else:
                    self.getMove()
                    
                
                        
def minmax(depth, currentPlayer, board, piecesWon, xx=False):
    li = []
    p = []
    listOfPlayers = [x for x in piecesWon.keys()]
    
    nextPlayer = listOfPlayers[((listOfPlayers.index(currentPlayer)+1)%2)]
    #if the board False, break
    if board == [0,0,0,0,0,0,0,0,0,0,0,0]:
        return xx, piecesWon

    #if the depth is reached break the recursion
    if depth < 1:
        return xx, piecesWon
    
    else:
        for x in range(1,7,1):
            playReturn = play(x, board.copy(), currentPlayer, piecesWon.copy())
            
            #creates branches based on the move for assumed moves
            if playReturn[0] != False:
                li.append((x, currentPlayer, minmax(depth-1, nextPlayer, playReturn[0].copy(), playReturn[1].copy(), x)[-1]))
                
                p.append(x)

        #this checks the min and max scores relative to the computer
        w = [move[2]["computer"] for move in li]
        
        if currentPlayer == "computer":
            m = 0
            for x in w:
                if x > m:
                    m = x
        else:
            m = 200
            for x in w:
                if x < m:
                    m = x

        if len(w) > 0:
            return li[w.index(m)][0], li[w.index(m)][2]
        else:
            return xx, piecesWon
            
def play(pick, board, currentPlayer, piecesWon):
    listOfPlayers = [x for x in piecesWon.keys()]
    pick -= 1
    if currentPlayer == "computer":
        pick = 5 - pick
        pick += 6

    #packs the seed in the selected position
    hand = board[pick]
    board[pick] = 0

    #move to the next hole
    i = (pick - 1)%12

    #if empty hole----play again to pack
    if hand == 0:
        return False, piecesWon
    
    else:
        while hand:
            #drop in hole
            board[i] += 1
            hand -= 1

            #if hand is empty        
            if hand == 0:
                ii = i  #check for win
                while board[ii] in [2,3] and ((currentPlayer == "computer" and ii in [0,1,2,3,4,5]) or (currentPlayer != "computer" and ii in [6,7,8,9,10,11])):
                    piecesWon[currentPlayer] += board[ii]
                    board[ii] = 0
                    ii = (ii + 1)%12

                #if the last hole dropped in is not empty pick again
                if board[i] > 1:
                    hand += board[i]
                    board[i] = 0

            i = (i - 1)%12

            #this condition checks for end of game
            li = [x for x in piecesWon.values()]
            nextPlayer = listOfPlayers[(listOfPlayers.index(currentPlayer)+1)%2]
            if sum(board) == 0 or (sum(board[(6*(listOfPlayers.index(nextPlayer))):(6*(listOfPlayers.index(nextPlayer)+1))]) == 0) or abs(li[0] - li[1]) > sum(board):
                board = [0 for a in range(12)]

        return board, piecesWon


if __name__ == "__main__":
    AYOGAMEINIT = ayoGame()
