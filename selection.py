import pygame as pg
from funcs import cell_coord

class Selection:
    def __init__(self):
        self.is_selected = False
        self.selected_piece = ''
        self.current_block = (-1, -1)

    def change_selection(self, board):
        if self.is_selected:
            coord = cell_coord()
            if board.cells[coord[0]][coord[1]].piece == '':
                self.is_selected = False
            else:
                print(self.current_block)
                board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
                self.current_block = coord
        else:
            coord = cell_coord()
            if board.cells[coord[0]][coord[1]].piece != '':
                self.is_selected = True
                self.current_block = coord 

    
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
