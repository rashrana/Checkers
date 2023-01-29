""" Final Project
Module: Board.py
Student Name: Prashant Rana
Student ID: 00804232
Description: Checkers Game
Python Version: 3.10.6S"""

import copy
from Piece import Piece

class Board:
    # boardStructure = [
    #     ['R','B','R','B','R','B','R','B'],
    #     ['B','R','B','R','B','R','B','R'],
    #     ['R','B','R','B','R','B','R','B'],
    #     ['B','R','B','R','B','R','B','R'],
    #     ['R','B','R','B','R','B','R','B'],
    #     ['B','R','B','R','B','R','B','R'],
    #     ['R','B','R','B','R','B','R','B'],
    #     ['B','R','B','R','B','R','B','R'],
    #     ]
    boardStructure = [
        ['.','B','.','B','.','B','.','B'],
        ['B','.','B','.','B','.','B','.'],
        ['.','B','.','B','.','B','.','B'],
        ['B','.','B','.','B','.','B','.'],
        ['.','B','.','B','.','B','.','B'],
        ['B','.','B','.','B','.','B','.'],
        ['.','B','.','B','.','B','.','B'],
        ['B','.','B','.','B','.','B','.'],
        ]
    row = {'A':0, 'B':1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    col = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
    def __init__(self):
        self.pieces = []
        self.turn = 'x'
        """Initialize x pieces"""
        for rowind,row in enumerate(Board.boardStructure[:3]):
            for colind,col in enumerate(row):
                if col == 'B':
                    piece = Piece(rowind, colind, 'x')
                    self.pieces.append(piece)

        """Initialize o pieces"""
        for rowind,row in enumerate(Board.boardStructure[5:]):
            for colind,col in enumerate(row):
                if col == 'B':
                    piece = Piece(rowind + 5, colind, 'o')
                    self.pieces.append(piece)

    """Prints the board to the console"""
    def printBoard(self):
        boardcopy = copy.deepcopy(Board.boardStructure)
        for piece in self.pieces:
            if piece.isKinged:
                boardcopy[piece.locRow][piece.locCol] = piece.pcType.upper()
            else:
                boardcopy[piece.locRow][piece.locCol] = piece.pcType
        print("*******************************************")
        print("   1   2   3   4   5   6   7   8")
        for index,row in enumerate(boardcopy):
            rowKeys = [item for item in Board.row.keys()]
            curRow = rowKeys[index]
            print(curRow+ "- " + " | ".join(row))
            if index != 7:
                print("   --+---+---+---+---+---+---+---")
        print("\n*******************************************n")

    """Returns the string representation of the board"""
    def getBoardString(self):
        fileString = ""
        boardcopy = copy.deepcopy(Board.boardStructure)
        for piece in self.pieces:
            if piece.isKinged:
                boardcopy[piece.locRow][piece.locCol] = piece.pcType.upper()
            else:
                boardcopy[piece.locRow][piece.locCol] = piece.pcType
        fileString += "*******************************************\n"
        fileString += "   1 2 3 4 5 6 7 8\n"
        for index,row in enumerate(boardcopy):
            rowKeys = [item for item in Board.row.keys()]
            curRow = rowKeys[index]
            fileString += curRow+ "- " + " ".join(row) + "\n"
        fileString += "*******************************************\n\n"
        return fileString

        
    """Returns row and column of given user input cell, 
        if invalid, returns both as None"""
    def getRowcol(self, cell):
        cell = cell.split("-")
        if len(cell) != 2:
            return None, None
        else:
            rowKeys = [item for item in Board.row.keys()]
            colKeys = [item for item in Board.col.keys()]
            if cell[0] in rowKeys and cell[1] in colKeys:
                return Board.row[cell[0]], Board.col[cell[1]]
            else:
                return None, None

    """Returns piece at given row, col location"""
    def getPiece(self, row, col):
        piece = None
        for item in self.pieces:
            if item.locRow == row and item.locCol == col:
                piece = item
                break
        return piece

    """Checks if any piece is at given row, col location"""
    def checkPiece(self, row, col):
        for item in self.pieces:
            if item.locRow == row and item.locCol == col:
                piece = item
                return True
        return False

    """Checks if the jump made by kinged piece is valid"""
    def checkKingedHop(self, piece, row = None, col = None):
        hopPiece1 = self.getPiece(piece.locRow - 1, piece.locCol - 1)
        hopPiece2 = self.getPiece(piece.locRow - 1, piece.locCol + 1)
        hopPiece3 = self.getPiece(piece.locRow + 1, piece.locCol - 1)
        hopPiece4 = self.getPiece(piece.locRow + 1, piece.locCol + 1)
        if row and col:
            if (((piece.locRow - 2 == row and piece.locCol - 2 == col) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                ((piece.locRow - 2 == row and piece.locCol + 2 == col) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType)) or
                ((piece.locRow + 2 == row and piece.locCol - 2 == col) and (hopPiece3 != None and hopPiece3.pcType != piece.pcType)) or
                ((piece.locRow + 2 == row and piece.locCol + 2 == col) and (hopPiece4 != None and hopPiece4.pcType != piece.pcType))):
                return True
            else:
                return False
        else:
            hopPiece1 = self.getPiece(piece.locRow - 1, piece.locCol - 1)
            hopPiece2 = self.getPiece(piece.locRow - 1, piece.locCol + 1)
            hopPiece3 = self.getPiece(piece.locRow + 1, piece.locCol - 1)
            hopPiece4 = self.getPiece(piece.locRow + 1, piece.locCol + 1)
            if ((self.checkForValidSpace(piece.locRow - 2, piece.locCol - 2) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                (self.checkForValidSpace(piece.locRow - 2, piece.locCol + 2) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType)) or
                (self.checkForValidSpace(piece.locRow + 2, piece.locCol - 2) and (hopPiece3 != None and hopPiece3.pcType != piece.pcType)) or
                (self.checkForValidSpace(piece.locRow + 2, piece.locCol + 2) and (hopPiece4 != None and hopPiece4.pcType != piece.pcType))):
                return True
            else:
                return False

    """Checks if jump made by piece type x is valid"""
    def checkxHop(self, piece, row = None, col = None):
        if row and col:
            hopPiece1 = self.getPiece(piece.locRow + 1, piece.locCol - 1)
            hopPiece2 = self.getPiece(piece.locRow + 1, piece.locCol + 1)
            if (((piece.locRow + 2 == row and piece.locCol - 2 == col) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                ((piece.locRow + 2 == row and piece.locCol + 2 == col) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType))):
                return True
            else:
                return False
        else:
            hopPiece1 = self.getPiece(piece.locRow + 1, piece.locCol - 1)
            hopPiece2 = self.getPiece(piece.locRow + 1, piece.locCol + 1)
            if ((self.checkForValidSpace(piece.locRow + 2, piece.locCol - 2) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                (self.checkForValidSpace(piece.locRow + 2, piece.locCol + 2) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType))):
                return True
            else:
                return False

    """Checks if jump made by piece type o is valid"""
    def checkoHop(self, piece, row = None, col = None):
        if row and col:
            hopPiece1 = self.getPiece(piece.locRow - 1, piece.locCol - 1)
            hopPiece2 = self.getPiece(piece.locRow - 1, piece.locCol + 1)
            if (((piece.locRow - 2 == row and piece.locCol - 2 == col) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                ((piece.locRow - 2 == row and piece.locCol + 2 == col) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType))):
                return True
            else:
                return False
        else:
            hopPiece1 = self.getPiece(piece.locRow - 1, piece.locCol - 1)
            hopPiece2 = self.getPiece(piece.locRow - 1, piece.locCol + 1)
            if ((self.checkForValidSpace(piece.locRow - 2, piece.locCol - 2) and (hopPiece1 != None and hopPiece1.pcType != piece.pcType)) or
                (self.checkForValidSpace(piece.locRow - 2, piece.locCol + 2) and (hopPiece2 != None and hopPiece2.pcType != piece.pcType))):
                return True
            else:
                return False

    """Checks if next move is available for a piece"""
    def checkNextMove(self, piece):
        if piece.isKinged:
            if ((self.checkForValidSpace(piece.locRow - 1, piece.locCol - 1)) or
                (self.checkForValidSpace(piece.locRow - 1, piece.locCol + 1)) or
                (self.checkForValidSpace(piece.locRow + 1, piece.locCol - 1)) or
                (self.checkForValidSpace(piece.locRow + 1, piece.locCol + 1))):
                return True
            else:
                return False
        elif piece.pcType == 'x':
            if ((self.checkForValidSpace(piece.locRow + 1, piece.locCol - 1)) or
                (self.checkForValidSpace(piece.locRow + 1, piece.locCol + 1))):
                return True
            else:
                return False
        elif piece.pcType == 'o':
            if ((self.checkForValidSpace(piece.locRow - 1, piece.locCol - 1)) or
                (self.checkForValidSpace(piece.locRow - 1, piece.locCol + 1))):
                return True
            else:
                return False
        else:
            return False

    """Validate following scenarios:
    - if any piece is at destination, if present Invalid Destination
    - if is kinged, can move forward backward and hop only one opposite piece
    - if is not kinged, check piece type,
        - if x, can move forward and can hop only one opposite piece, i.e. start cell: A2, Dest cell: B1
        - if o, can move backward and can hop only opposite one piece, i.e. start cell: H1, Dest cell: G2"""
    def validateDestination(self, row, col, piece):
        if(self.checkForValidSpace(row, col) == False):
            return False
        if piece.isKinged:
            """For move one step forward or backward"""
            if ((piece.locRow - 1 == row and piece.locCol - 1 == col) or
                (piece.locRow - 1 == row and piece.locCol + 1 == col) or
                (piece.locRow + 1 == row and piece.locCol - 1 == col) or
                (piece.locRow + 1 == row and piece.locCol + 1 == col)):
                return True
            """For hoping over opponent piece"""
            return self.checkKingedHop(piece, row, col)
        elif piece.pcType == 'x':
            """For move one step forward"""
            if ((piece.locRow + 1 == row and piece.locCol - 1 == col) or
                (piece.locRow + 1 == row and piece.locCol + 1 == col)):
                return True
            """For hoping over opponent piece"""
            return self.checkxHop(piece, row, col)
        elif piece.pcType == 'o':
            """For move one step forward"""
            if ((piece.locRow - 1 == row and piece.locCol - 1 == col) or
                (piece.locRow - 1 == row and piece.locCol + 1 == col)):
                return True
            """For hoping over opponent piece"""
            return self.checkoHop(piece, row, col)

        

    """To move a piece, starting Cell and Destination Cell is given
    first get piece at Starting Cell
    - if No piece, Invalid Move
    else Check the type of piece, 
    - if other players piece, Invalid Move
    - Validate destination Cell and move"""
    def movePiece(self, startCell, endCell):
        row, col = self.getRowcol(startCell)
        if row == None or col == None:
            print("Invalid Starting Cell!")
            return False
        piece = self.getPiece(row, col)
        if piece == None:
            print("No piece available at starting Cell!")
            return False
        
        if piece.pcType != self.turn:
            print("Invalid player piece selected!")
            return False
        
        endrow, endcol = self.getRowcol(endCell)
        if endrow == None or endcol == None:
            print("Invalid Destination Cell!")
            return False
        # if(self.validateDestination(endrow, endcol, piece)):
        #     piece.moveForwardBackward(endrow,endcol)
        #     return piece
        if (self.makeHop(piece, endrow, endcol)):
            return piece
        else:
            print("Invalid Destination")
            return False

    """Checks whether the given row, col location is an empty space
        firstly check if row and col is valid
        then check if it's an empty space"""
    def checkForValidSpace(self, row, col):
        if row in Board.row.values() and col in Board.col.values():
            status = self.checkPiece(row, col)
            if status == False:
                return True
            else:
                return False
        else:
            return False

    """Check if next hop is available, if it's available then it's the same player's turn"""
    def checkForNextHop(self, piece):
        if piece.isKinged:
            return self.checkKingedHop(piece)
        elif piece.pcType == 'x':
            return self.checkxHop(piece)
        elif piece.pcType == 'o':
            return self.checkoHop(piece)

    """Hop a piece to a given destination
        firstly, check if the dest is valid, and empty
        then check piece iskinged or not
        - if yes, then check it's hoping over opponent piece
            - if true then hop
            - else if it's moving a step forward/backward, then move
            - else invalid move
        - else if, piece type is x, then check if it's hoping forward over opponent piece
            - if true then hop
            - else if it's moving a step forward, then move
            - else invalid move
        - else if, piece type is y, then check if it's hoping backward over opponent piece
            - if true then hop
            - else if it's moving a step backward, then move
            - else invalid move"""
    def makeHop(self, piece, row, col):
        # row, col = self.getRowcol(dest)
        if row == None or col == None or self.checkForValidSpace(row, col) == False:
            print("Invalid Destination Cell!")
            return False
        if piece.isKinged:
            if(self.checkKingedHop(piece, row, col)):
                hoppedPieceRow = (piece.locRow + row) / 2
                hoppedPieceCol = (piece.locCol + col) / 2
                hoppedPiece = self.getPiece(hoppedPieceRow, hoppedPieceCol)
                hoppedPiece.killed()
                self.pieces.remove(hoppedPiece)
                piece.moveForwardBackward(row, col)
                return True
            else:
                """For move one step forward or backward"""
                if ((piece.locRow - 1 == row and piece.locCol - 1 == col) or
                    (piece.locRow - 1 == row and piece.locCol + 1 == col) or
                    (piece.locRow + 1 == row and piece.locCol - 1 == col) or
                    (piece.locRow + 1 == row and piece.locCol + 1 == col)):
                    piece.moveForwardBackward(row, col)
                    return True
                else:
                    print("Invalid Destination Cell!")
                    return False
        elif piece.pcType == 'x':
            if(self.checkxHop(piece, row, col)):
                hoppedPieceRow = (piece.locRow + row) / 2
                hoppedPieceCol = (piece.locCol + col) / 2
                hoppedPiece = self.getPiece(hoppedPieceRow, hoppedPieceCol)
                hoppedPiece.killed()
                self.pieces.remove(hoppedPiece)
                piece.moveForwardBackward(row, col)
                return True
            else:
                """For move one step forward"""
                if ((piece.locRow + 1 == row and piece.locCol - 1 == col) or
                (piece.locRow + 1 == row and piece.locCol + 1 == col)):
                    piece.moveForwardBackward(row, col)
                    return True
                else:
                    print("Invalid Destination Cell!")
                    return False
        elif piece.pcType == 'o':
            if(self.checkoHop(piece, row, col)):
                hoppedPieceRow = (piece.locRow + row) / 2
                hoppedPieceCol = (piece.locCol + col) / 2
                hoppedPiece = self.getPiece(hoppedPieceRow, hoppedPieceCol)
                hoppedPiece.killed()
                self.pieces.remove(hoppedPiece)
                piece.moveForwardBackward(row, col)
                return True
            else:
                """For move one step backward"""
                if ((piece.locRow - 1 == row and piece.locCol - 1 == col) or
                (piece.locRow - 1 == row and piece.locCol + 1 == col)):
                    piece.moveForwardBackward(row, col)
                    return True
                else:
                    print("Invalid Destination Cell!")
                    return False
            
        
        
