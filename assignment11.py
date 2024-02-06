#Aaron Shannon
#CS 121 T/TH

from random import choice

class Connect4(object):
    def __init__(self, width, height, window=None):
        self.width = width
        self.height = height
        self.data = []
        self.total = 0
        
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]
        
    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s +=self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width + '-\n'

        for col in range(self.width):
            s += ' ' + str(col % 10)
        s += '\n'
        return s


    def addMove(self, col, ox):
        """
        This will start by checking if ox can be placed in the column selected.
        If it can be placed, it will place it on the next available row
        """
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return self.data[row][col]
        self.data[self.height-1][col] = ox




    def allowsMove(self, col):
        """
        This will check to see if the there is ox in the column space selected.
        """
        if self.data[0][col] != ' ':
            return False
        else:
            return True




    def delMove(self,c):
        """
        This will replace the input column slot with an empty string to simulate
        deleting a move
        """
        for row in range(self.height):
            if self.data[row][c] != ' ':
                self.data[row][c] = ' '
                return




    def isFull(self):
        """
        This keeps a counter and if the counter total is the same as the width * height
        it will return True
        """
        check = self.width * self.height
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != ' ':
                    self.total = self.total + 1
        if self.total == check:
            return True
        else:
            return False




    def winsFor(self,ox):
        """
        These will check for vertical and horizontal wins
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                    self.data[row][col+1] == ox and \
                    self.data[row][col+2] == ox and \
                    self.data[row][col+3] == ox:
                    return True

        for row in range(self.height-3):
            for col in range(self.width):
                if self.data[row][col] == ox and \
                    self.data[row+1][col] == ox and \
                    self.data[row+2][col] == ox and \
                    self.data[row+3][col] == ox:
                    return True

        
        """
        These will check for forwards and backwards diagonal wins
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.data[row][col] == ox and \
                    self.data[row+1][col-1] == ox and \
                    self.data[row+2][col-2] == ox and \
                    self.data[row+3][col-3] == ox:
                    return True


        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[row][col] == ox and \
                    self.data[row+1][col+1] == ox and \
                    self.data[row+2][col+2] == ox and \
                    self.data[row+3][col+3] == ox:
                    return True
        return False

    def clear(self):
        """
        This will clear the board by replacing all elements with empty strings
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != ' ':
                    self.data[row][col] = ' '


    def hostgame(self):
        """
        This will run the game and ask for inputs for players and moves
        """
        turn = 0
        print(self)
        player1 = input('Do you want to be X or O?')
        if player1 == 'x' or player1 == 'X':
            player1 = 'X'
            player2 = 'O'

        elif player1 == 'o' or player1 == 'O':
            player1 = 'O'
            player2 = 'X'

        while self.isFull() == False:
            print(self)
            if turn % 2 == 0:
                move = int(input('Player 1 choose a coloumn from 0 - ' + str(self.width-1) + '? '))
                while self.allowsMove(move) == False:
                    move = int(input('Sorry, please try another move: '))
                self.addMove(move,player1)

                if self.winsFor(player1) == True:
                    print(self)
                    print('PLAYER 1 IS THE WINNER!!!!!')
                    break
                turn += 1

            elif turn % 2 != 0:
                move = int(input('Player 2 choose a coloumn from 0 - ' + str(self.width-1) + '? '))
                while self.allowsMove(move) == False:
                    move = int(input('Sorry, please try another move: '))
                self.addMove(move,player2)
                if self.winsFor(player2) == True:
                    print(self)
                    print('PLAYER 2 IS THE WINNER!!!!!')
                    break
                turn += 1

            elif self.isFull() == True:
                print(self)
                print("GAME OVER, IT'S A TIE!!!")
                break


    def playGameWith(self, aiPlayer):
        #This is set up to have a player go up against an AI player

        turn = 0
        # print(self)
        player1 = 'X'
        player2 = 'O'

        while self.isFull() == False:
            print(self)
            if turn % 2 == 0:
                move = int(input('Player 1 choose a coloumn from 0 - ' + str(self.width-1) + '? '))
                while self.allowsMove(move) == False:
                    move = int(input('Sorry, please try another move: '))
                self.addMove(move,player1)

                if self.winsFor(player1) == True:
                    print(self)
                    print('PLAYER 1 IS THE WINNER!!!!!')
                    break
                turn += 1

            elif turn % 2 != 0:
                move = aiPlayer.nextMove(self)
                self.addMove(move,player2)
                if self.winsFor(player2) == True:
                    print(self)
                    print('THE COMPUTER IS THE WINNER!!!!!')
                    break
                turn += 1

            elif self.isFull() == True:
                print(self)
                print("GAME OVER, IT'S A TIE!!!")
                break



class Player(object):
    def __init__(self, ox, tbt, ply):
        self.checker = ox
        self.tieBreakType = tbt
        self.ply = ply



    def nextMove(self, b):
        #this take in a list and pass it to the tieBreakerMove Function

        moveList = self.scoreFor(b, self.checker, self.ply)
        return self.tieBreakMove(moveList)



    def tieBreakMove(self, score):
        #this will decide on the move to be taken depending on the tieBreakType

        if self.tieBreakType == 'Left':
            #iterate through list like normal
            for i in range(len(score)):
                if score[i] == max(score):
                    return i

        elif self.tieBreakType == 'Right':
            #iterate through list from opposite direction
            reversed(score)
            for j in range(len(score)):
                if score[j] == max(score):
                    return (len(score)-1) - j

        elif self.tieBreakType == 'Random':
            randList = []
            for k in range(len(score)):
                if score[k] == max(score):
                    randList.append(k)
            return choice(randList)



    def scoreFor(self, b, ox, ply):
        #iterates through the colomns testing and scoring the moves

        colScore = 0
        scoreList = []
        oppScore = 0
        oppPiece = ' '

        if ox == 'X':
            oppPiece = 'O'
        else:
            oppPiece = 'X'


        for col in range(b.width):
            if b.allowsMove(col) == True:
                b.addMove(col, ox)
                if b.winsFor(ox) == True:
                    colScore = 100

                else:
                    if ply > 1:
                        oppScore = max(self.scoreFor(b, oppPiece, ply-1))
                        colScore = 100 - oppScore

                    else:
                        colScore = 50
                b.delMove(col)
            else:
                colScore = -1

            scoreList.append(colScore)


        return scoreList




def main():

    connect = Connect4(7,6)
    p = Player('O','Random',2)
    connect.playGameWith(p)
    #connect.hostgame()

    # connect.addMove(0,'o')
    # connect.addMove(0,'x')
    # connect.addMove(0,'o')
    # connect.addMove(0,'x')
    # connect.addMove(0,'o')
    # connect.addMove(0,'x')


    # connect.addMove(2,'o')
    # connect.addMove(2,'x')
    # connect.addMove(2,'o')

    # connect.addMove(3,'x')
    # connect.addMove(3,'x')
    # connect.addMove(3,'o')

    # connect.addMove(4,'x')
    # connect.addMove(4,'o')
    # connect.addMove(4,'x')
    # connect.addMove(4,'o')

    # connect.addMove(5,'o')
    # connect.addMove(5,'o')

    # p = Player('x', 'Random', 1)
    # print(p.nextMove(connect))
    

    print(connect)

if __name__ == '__main__':
    main() 