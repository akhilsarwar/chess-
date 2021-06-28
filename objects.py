from load_assets import *
import copy
from screen import *
from funcs import cell_coord
from funcs import centralize_coordinates


dead = []
pieces  = dict()

class Board:
    cells = []
    def __init__ (self):
        for i in range(8):
            row = []
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        row.append(Cell(copy.copy(BLACK_CELL_IMG), 'black', (i, j)))
                    else:
                        row.append(Cell(copy.copy(WHITE_CELL_IMG), 'white', (i, j)))
                else:
                    if j % 2 == 0:
                        row.append(Cell(copy.copy(WHITE_CELL_IMG), 'white', (i, j)))
                    else:
                        row.append(Cell(copy.copy(BLACK_CELL_IMG), 'black', (i, j)))
            self.cells.append(row)
    
    def show_board(self):
        for i in range(8):
            for j in range(8):
                self.cells[i][j].show_cell()

class Cell:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.piece = ''

    def show_cell(self):
        self.img.show_img((self.pos[0] * 100, self.pos[1] * 100))

    def change_piece(self, new_piece = ''):
        self.piece = new_piece

class King:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True
    
    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

class Queen:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

class Bishop:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

class Knight:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

class Rook:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

class Pawn:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True
        self.move_no = 0
        self.pawn_dir = {"white": -1, "black" : 1}

    def show(self):
        if self.alive:
                self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

    def move(self, board, to):
        #pawn can move either forward 1 or 2 steps or it can cut diagonally forward if the opposite color is not self.color
        if to[0] == self.pos[0]:
            #pawn vertically forward
            if to[1] == self.pos[1] + self.pawn_dir[self.color]:
                #pawn one step forward
                if isfree(self, to, board):
                   shift_piece(self, to, board)
                   self.move_no += 1
                   return True
            elif to[1] == self.pos[1] + 2 * self.pawn_dir[self.color] and self.move_no == 0:
                #pawn 2 step forward
                if isfree(self, to, board):
                    shift_piece(self, to, board)
                    self.move_no +=1
                    return True
        else:
            #pawn diagonal cut
            if to[1] == self.pos[1] + self.pawn_dir[self.color]:
                if isrival(self, to, board) and not isking(to, board):
                    shift_piece(self, to, board)
                    self.move_no += 1
                    return True
        return False
                




def shift_piece(obj, to, board):
    pos_now = obj.pos
    board.cells[pos_now[0]][pos_now[1]].piece = ''

    if isrival(obj, to, board):
        obj_to = board.cells[to[0]][to[1]].piece
        dead.append(obj_to)
        obj_to.alive = False
        board.cells[to[0]][to[1]].piece = ''
        #TODO: haven't changed the position of dead pieces 

    board.cells[to[0]][to[1]].piece = obj
    obj.pos = to


def isrival(obj, to, board):
    if board.cells[to[0]][to[1]].piece != '':
        obj_to = board.cells[to[0]][to[1]].piece
        if obj_to.color != obj.color:
            return True
    return False

def isfree(obj, to, board):
    if board.cells[to[0]][to[1]].piece == '':
        return True
    return False

def isking(to, board):
    obj_to = board.cells[to[0]][to[1]].piece
    if obj_to not in pieces['king_w'] and obj_to not in pieces['king_b']:
        return False
    else:
        return True

