from load_assets import *
import copy
from screen import *
from funcs import cell_coord
from funcs import centralize_coordinates
from funcs import rival_color


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

    def move(self, board, to):
        x, y = to[0], to[1]
        valid_ = False
        if abs(x - self.pos[0]) == abs(y - self.pos[1]):
            if abs(x - self.pos[0]) == 1:
                valid_ = True
        elif x == self.pos[0]:
            if abs(y - self.pos[1]) == 1:
                valid_ = True
        elif y == self.pos[1]:
            if abs(x - self.pos[0]) == 1:
                valid_ = True

        if valid_:
            if isfree(self, to, board):
                shift_piece(self, to, board)
                return True
            elif isrival(self, to, board) and not isking(to, board):
                shift_piece(self, to, board)
                return True
        return False
    
    def in_check(self, board):
        #check vertical attacks
        if vertical_attack(board):
            return True

        #check horizontal attacks
        elif diagonal_attack(board):
            return True

        #check horse attacks
        elif horse_attack(board):
            return True

        return False



    def horse_attack(self, board):
        x, y  = self.pos[0], self.pos[1]
        riv_color = rival_color(self)

        if self.check_horse(x + 1, y + 2, riv_color):
            return True
        elif self.check_horse(x + 1, y - 2, riv_color):
            return True
        elif self.check_horse(x - 1, y + 2, riv_color):
            return True
        elif self.check_horse(x - 1, y - 2, riv_color):
            return True
        elif self.check_horse(x + 2, y + 1, riv_color):
            return True
        elif self.check_horse(x + 2, y - 1, riv_color):
            return True
        elif self.check_horse(x - 2, y + 1, riv_color):
            return True
        elif self.check_horse(x - 2, y - 1, riv_color):
            return True

        return False



    def check_horse(self, x, y, riv_color):
        if x >=0 and x < 8 and y >= 0 and y < 8:
            if board.cells[x][y].piece != '':
                if isrival(self, to, board):
                    if rival in pieces['knight_' + riv_color]:
                        return True
        return False


    def diagonal_attack(self, board):
        x, y  = self.pos[0], self.pos[1]
        riv_color = rival_color(self)
        if self.check_diagonal(board, x, y, -1, 1, riv_color):
            return True
        elif self.check_diagonal(board, x, y, 1, -1, riv_color):
            return True
        elif self.check_diagonal(board, x, y, 1, 1, riv_color):
            return True
        elif self.check_diagonal(board, x, y, -1, -1, riv_color):
            return True
        return False


    def check_diagonal(self, board, x, y, add_x, add_y, riv_color):
        for i in range(1, 8):
            x_ = x + add_x * i
            y_ = y + add_y * i
            if x_  >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
                if board.cells[x_][y_].piece != '':
                    if isrival(self, to, board):
                        rival = board.cells[x_][y_].piece
                        if i == 1 and rival in pieces['pawn_' + riv_color]:
                            if pawn_attack(board, rival, riv_color):
                                return True
                        elif rival in pieces['queen_' + riv_color] or rival in pieces['bishop_' + riv_color]:
                            return True
                        else:
                            break
                    break
        return False

    def pawn_attack(self, board, rival, riv_color):
        if rival.pos[1] == self.pos[1] - rival.pawn_dir[riv_color]:
            return True
        else:
            return False
        


    def vertical_attack(self, board):
        x, y  = self.pos[0], self.pos[1]
        riv_color = rival_color(self)
        if self.check_vert(board, x, y, -1, 0, riv_color):
            return True
        elif self.check_vert(board, x, y, 1, 0, riv_color):
            return True
        elif self.check_vert(board, x, y, 0, -1, riv_color):
            return True
        elif self.check_vert(board, x, y, 0, 1, riv_color):
            return True
        return False

    def check_vert(self, board, x, y, add_x, add_y, riv_color):
        for i in range(1, 8):
            x_ = x + add_x * i
            y_ = y + add_y * i
            if x_  >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
                if board.cells[x_][y_].piece != '':
                    if isrival(self, to, board):
                        rival = board.cells[x_][y_].piece
                        if i == 1 and rival in pieces['king_' + riv_color]:
                            return True
                        elif rival in pieces['queen_' + riv_color] or rival in pieces['rook_' + riv_color]:
                            return True
                        else:
                            break
                    break
        return False



class Queen:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

    def move(self, board, to):
        x, y = to[0], to[1]
        valid_ = (abs(x - self.pos[0]) == abs(y - self.pos[1])) or (x == self.pos[0] or y == self.pos[1])
        if valid_:
            if not obstacle(self.pos, to, board):
                if isfree(self, to, board):
                    shift_piece(self, to, board)
                    return True
                elif isrival(self, to, board) and not isking(to, board):
                    shift_piece(self, to, board)
                    return True
        return False


class Bishop:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

    def move(self, board, to):
        x, y = to[0], to[1]
        valid_ = abs(x - self.pos[0]) == abs(y - self.pos[1])
        if valid_:
            if not obstacle(self.pos, to, board):
                if isfree(self, to, board):
                    shift_piece(self, to, board)
                    return True
                elif isrival(self, to, board) and not isking(to, board):
                    shift_piece(self, to, board)
                    return True
        return False


class Knight:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

    def move(self, board, to):
        x, y = to[0], to[1]
        valid_ = (abs(x - self.pos[0]) == 1 and abs(y - self.pos[1])) == 2 or (abs(x - self.pos[0]) == 2 and abs(y - self.pos[1]) == 1)
        if valid_:
            if isfree(self, to, board):
                shift_piece(self, to, board)
                return True
            elif isrival(self, to, board) and not isking(to, board):
                shift_piece(self, to, board)
                return True
        return False



class Rook:
    def __init__ (self, img, color, pos):
        self.img = Img(img)
        self.color = color
        self.pos = pos
        self.alive = True

    def show(self):
        if self.alive:
            self.img.show_img(centralize_coordinates(self.pos[0]*100, self.pos[1]* 100))

    def move(self, board, to):
        if to[0] == self.pos[0] or to[1] == self.pos[1]:
            if not obstacle(self.pos, to, board):
                if isfree(self, to, board):
                    shift_piece(self, to, board)
                    return True
                elif isrival(self, to, board) and not isking(to, board):
                    shift_piece(self, to, board)
                    return True
        return False
        

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
                if isfree(self, to, board) and not obstacle(self.pos, to, board):
                   shift_piece(self, to, board)
                   self.move_no += 1
                   return True
            elif to[1] == self.pos[1] + 2 * self.pawn_dir[self.color] and self.move_no == 0:
                #pawn 2 step forward
                if isfree(self, to, board) and not obstacle(self.pos, to, board):
                    shift_piece(self, to, board)
                    self.move_no +=1
                    return True
        else:
            #pawn diagonal cut
            if to[1] == self.pos[1] + self.pawn_dir[self.color] and (to[0] == self.pos[0] - 1 or to[0] == self.pos[0] + 1):
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

def obstacle(fr, to, board):
    diff_x = to[0] - fr[0];
    diff_y = to[1] - fr[1];

    diag = abs(diff_x) == abs(diff_y)
    vert = diff_x == 0 or diff_y == 0
    assert diag or vert

    if diag:
        for i in range(1, abs(diff_x)):
            if diff_x < 0 and diff_y < 0:
                if board.cells[to[0] + i][to[1] + i].piece != '':
                    return True
            elif diff_x < 0 and diff_y > 0:
                if board.cells[to[0] + i][to[1] - i].piece != '':
                    return True
            elif diff_x > 0 and diff_y < 0:
                if board.cells[to[0] - i][to[1] + i].piece != '':
                    return True
            elif diff_x > 0 and diff_y > 0:
                if board.cells[to[0] - i][to[1] - i].piece != '':
                    return True
        return False
    elif vert:
        if diff_x == 0:
            for i in range(1, abs(diff_y)):
                if diff_y < 0:
                    if board.cells[to[0]][to[1] + i].piece != '':
                        return True
                else:
                    if board.cells[to[0]][to[1] - i].piece != '':
                        return True

        else:
            for i in range(1, abs(diff_x)):
                if diff_x < 0:
                    if board.cells[to[0] + i][to[1]].piece != '':
                        return True
                else:
                    if board.cells[to[0] - i][to[1]].piece != '':
                        return True
        return False


