from load_assets import *
from main import screen_width_
from main import screen_width_
from main import screen_

class Board:
    cells = []
    def __init__ (self):
        for i in range(8):
            row = []
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        row.append(Cell(BLACK_CELL_IMG, 'black', (i * 100, j * 100)))
                    else:
                        row.append(Cell(WHITE_CELL_IMG, 'white', (i * 100, j * 100)))
                else:
                    if j % 2 == 0:
                        row.append(Cell(WHITE_CELL_IMG, 'white', (i * 100, j * 100)))
                    else:
                        row.append(Cell(BLACK_CELL_IMG, 'black', (i * 100, j * 100)))
            self.cells.append(row)
    
    def show_board(self):
        for i in range(8):
            for j in range(8):
                self.cells[i][j].show_cell()

class Cell:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show_cell(self):
        screen_.blit(self.img, self.pos)

class King:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos
    
    def show(self):
        screen_.blit(self.img, self.pos)

class Queen:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show(self):
        screen_.blit(self.img, self.pos)

class Bishop:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show(self):
        screen_.blit(self.img, self.pos)

class Knight:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show(self):
        screen_.blit(self.img, self.pos)

class Rook:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show(self):
        screen_.blit(self.img, self.pos)

class Pawn:
    def __init__ (self, img, color, pos):
        self.img = img
        self.color = color
        self.pos = pos

    def show(self):
        screen_.blit(self.img, self.pos)
