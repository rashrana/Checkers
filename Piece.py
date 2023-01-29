""" Final Project
Module: Piece.py
Student Name: Prashant Rana
Student ID: 00804232
Description: Checkers Game
Python Version: 3.10.6S"""

class Piece:
    def __init__(self,row, col, type):
        self.pcType = type
        self.locRow = row
        self.locCol = col
        self.isKinged = False
        self.isAlive = True
    
    """Returns the type of the piece"""
    def getType(self):
        return self.pcType
    
    """Sets the type of the piece"""
    def setType(self, pctype):
        self.pcType = pctype

    """Kills a piece and removes itself from the board"""
    def killed(self):
        self.isAlive = False
        self.locRow = None
        self.locCol = None

    """Piece is kinged and can move both direction"""
    def kinged(self):
        self.isKinged = True
    
    """Moves at the given location - Can be referred as setLocation"""
    def moveForwardBackward(self,row, col):
        self.locRow = row
        self.locCol = col


