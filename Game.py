""" Final Project
Module: Game.py
Student Name: Prashant Rana
Student ID: 00804232
Description: Checkers Game
Python Version: 3.10.6S"""

import datetime as dt
from Board import Board
import copy
class Game:
    def __init__(self):
        self.player1 = ''
        self.player2 = ''
        self.fileName = ''
        self.status = 'running'
        self.lastMove = None
        
    """Main menu of our game"""
    def menu(self):
        self.player1 = input("Enter Player 1's Name: ")
        while (self.player1 == ''):
            self.player1 = input("Invalid entry for Player 1\'s Name Please Input a Valid Name: ")
        self.player2 = input("Enter Player 2's Name: ")
        while (self.player2 == ''):
            self.player2 = input("Invalid entry for Player 2\'s Name Please Input a Valid Name: ")
        date = dt.datetime.now()
        self.fileName = self.player1 + "_" + self.player2 + "_" + date.strftime("%d_%m_%y_%H_%M_%S_%p") + ".txt"
        begin = input("Begin game play?(Y/N): ")
        while (begin.upper() != 'Y' and begin.upper() != 'N'):
            print("Invalid Entry!")
            begin = input("Begin game play?(Y/N): ")
        if begin.upper() == 'Y':
            print("GAME START")
            self.board = Board()
            self.board.printBoard()
        else:
            end = input("Do you want to quit the game?(Y/N): ")
            while (end.upper() != 'Y' and end.upper() != 'N'):
                print("Invalid Entry!")
            if begin == 'Y':
                print("Quiting Game!")
                exit(0)
            else:
                print("GAME START")
                self.board = Board()
                self.board.printBoard()

    """Checks if given multijump is valid"""
    def checkMultiJump(self, moves):
        """Check if intermediate cell matches in both current and upcoming move
            i.e. for multijump 'x' moves from A-2 to C-4 then 2nd move should start from C-4"""
        for ind in range(1, len(moves) - 1):
            move1 = moves[ind - 1].split(",")[1]
            move2 = moves[ind].split(",")[0]
            if move1 != move2:
                return False
        """if all steps are valid jumps"""
        for move in moves:
            move1 = move.split(",")[0]
            move2 = move.split(",")[1]
            row1,col1 = self.board.getRowcol(move1)
            row2,col2 = self.board.getRowcol(move2)
            if ((row1 + 2 == row2 and col1 + 2 == col2) or
                (row1 + 2 == row2 and col1 - 2 == col2) or
                (row1 - 2 == row2 and col1 + 2 == col2) or
                (row1 - 2 == row2 and col1 - 2 == col2)):
                continue
            else:
                return False
        """jumped over piece should be opponents piece"""
        for move in moves:
            move1 = move.split(",")[0]
            move2 = move.split(",")[1]
            row1,col1 = self.board.getRowcol(move1)
            row2,col2 = self.board.getRowcol(move2)
            row3 = (row1 + row2)/2
            col3 = (col1 + col2)/2 
            piece = self.board.getPiece(row3,col3)
            if (piece == None or (piece and self.board.turn == piece.pcType)):
                return False
        return True

    """Gets move from user, validates, moves and writes log to log file"""
    def getNextMove(self):
        """Save a copy of previous pieces to revert back if invalid move"""
        piecescopy = copy.deepcopy(self.board.pieces)
        if (self.board.turn == 'x'):
            moves = input(f"Player {self.player1} Please Enter Your Move(x piece): ").upper().split(";")
            if len(moves) > 1:
                if (self.checkMultiJump(moves) == False):
                    return print("Invalid MultiJump!")
            for nextMove in moves:
                move = nextMove.split(",")
                if len(move) == 2:
                    piece = self.board.movePiece(move[0],move[1])
                    if (piece):
                        if piece.isKinged == False and piece.locRow == 7:
                            piece.kinged()
                        self.lastMove = move
                        # while(self.board.checkForNextHop(piece)):
                        #     newDest = input(f"{self.player1} Please Enter Your Next Destination for Piece({piece.locRow},{piece.locCol}): ")
                        #     self.board.makeHop(piece, newDest)
                        self.writeLogToFile(self.player1, move)
                    else:
                        self.board.pieces = piecescopy
                        return
                else:
                    return print("Invalid input! No start and end cell!")
            self.board.turn = 'o'
        elif (self.board.turn == 'o'):
            moves = input(f"Player {self.player2} Please Enter Your Move(o piece): ").upper().split(";")
            if len(moves) > 1:
                if (self.checkMultiJump(moves) == False):
                    return print("Invalid MultiJump!")
            for nextMove in moves:
                move = nextMove.split(",")
                if len(move) == 2:
                    piece = self.board.movePiece(move[0],move[1])
                    if (piece):
                        if piece.isKinged == False and piece.locRow == 0:
                            piece.kinged()
                        self.lastMove = move
                        self.lastMove = move
                        # while(self.board.checkForNextHop(piece)):
                        #     newDest = input(f"{self.player2} Please Enter Your Next Destination for Piece({piece.locRow},{piece.locCol}): ")
                        #     self.board.makeHop(piece, newDest)
                        self.writeLogToFile(self.player2, move)
                    else:
                        self.board.pieces = piecescopy
                        return
                else:
                    return print("Invalid input! No start and end cell!")
            self.board.turn = 'x'

    """if no pieces left of one catagory then opponent is the winner"""
    def checkPieces(self):
        xPieces = [piece for piece in self.board.pieces if piece.pcType == 'x']
        oPieces = [piece for piece in self.board.pieces if piece.pcType == 'o']
        if len(xPieces) == 0:
            print(f"{self.player2} won!")
            with open(self.fileName,'a') as logFile:
                logFile.write(f"{self.player2} won!\n")
            self.status = 'winner'
            exit(0)
        elif len(oPieces) == 0:
            print(f"{self.player1} won!")
            with open(self.fileName,'a') as logFile:
                logFile.write(f"{self.player1} won!\n")
            self.status = 'winner'
            exit(0)

    """"Check if Next Move is available for upcoming player, if no then other player is the winner"""
    def checkNextMoveAvailable(self):
        piecesToCheck = [piece for piece in self.board.pieces if piece.pcType.upper() == self.board.turn.upper()]
        for piece in piecesToCheck:
            if(self.board.checkForNextHop(piece) or self.board.checkNextMove(piece)):
                return True
        if self.board.turn == 'x':
            print(f"{self.player2} won!")
            with open(self.fileName,'a') as logFile:
                logFile.write(f"{self.player2} won!\n")
            self.status = 'winner'
            exit(0)
        else:
            print(f"{self.player1} won!")
            with open(self.fileName,'a') as logFile:
                logFile.write(f"{self.player1} won!\n")
            self.status = 'winner'
            exit(0)
        return False

    """Function to write log file"""
    def writeLogToFile(self, player, move):
        with open(self.fileName,'a') as logFile:
            logFile.write(f"{player} moved {move[0]} -> {move[1]}\n")
            logFile.write(f"{self.board.getBoardString()}")

    """Run game until ending condition meets"""
    def runGame(self):
        while(self.status == 'running'):
            print("For consecutive jump give moves seperated by \';\'")
            print("ex: C-2,E-4;E-4,G-2")
            self.getNextMove()
            self.board.printBoard()
            self.checkPieces()
            self.checkNextMoveAvailable()

if __name__ == '__main__':
    game = Game()
    game.menu()
    game.runGame()