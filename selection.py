import pygame as pg
from funcs import cell_coord

class Selection:
    def __init__(self):
        self.is_selected = False
        self.active_piece = ''
        self.current_block = (-1, -1)

    def selection_action(self, board):
        if self.is_selected:
            coord = cell_coord()
#            if board.cells[coord[0]][coord[1]].piece == '':
#                if move(self.active_piece, coord, board):
#                    self.is_selected = False
#            else:
#                if move(self.active_piece, coord, board):
#                    self.is_selected 
            if self.same_color_select(board, coord):
                board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
                self.active_piece = board.cells[coord[0]][coord[1]].piece
                self.current_block = coord

            else:
                if self.active_piece.move(board, coord):
                    self.is_selected = False
                    board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
        else:
            coord = cell_coord()
            if board.cells[coord[0]][coord[1]].piece != '':
                self.is_selected = True
                self.current_block = coord 
                self.active_piece = board.cells[coord[0]][coord[1]].piece

    
    def highlight_rect(self, board):

        if self.is_selected:
            board.cells[self.current_block[0]][self.current_block[1]].img.enhance = True
        else:
            coord = cell_coord()
            if(self.current_block == (-1, -1)):
                try:
                    board.cells[coord[0]][coord[1]].img.enhance = True
                    self.current_block = coord 
                except:
                    print("Out of Index")
            else:
                if(self.current_block != coord):
                    board.cells[self.current_block[0]][self.current_block[1]].img.enhance = False
                    try:
                        board.cells[coord[0]][coord[1]].img.enhance = True
                        self.current_block = coord 
                    except:
                        self.current_block = (-1, -1)



    def same_color_select(self, board, coord):
        obj = board.cells[coord[0]][coord[1]].piece
        if obj != '':
            if obj.color == self.active_piece.color:
                return True
        return False
