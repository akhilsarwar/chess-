import pygame as pg
from funcs import cell_coord
from objects import pieces
from checkmate import checkmate

class Selection:
    def __init__(self):
        self.is_selected = False
        self.active_piece = ''
        self.current_block = (-1, -1)

    def selection_action(self, board, play):
        if self.is_selected:
            coord = cell_coord()
            if self.same_color_select(board, coord):
                board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
                self.active_piece = board.cells[coord[0]][coord[1]].piece
                self.current_block = coord

            else:
                lastmove = board.last_move
                if self.active_piece.move(board, coord):
                    print(board.last_move)
                    self.is_selected = False
                    board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
                    play.change_turn()
                    self.alter_lastmove_highlight(lastmove, board)
                    self.alter_lastmove_highlight(board.last_move, board)
                    #checking whether a checkmate is possible at this stage of the game
                    if check_incheck(play.turn, board):
                        if checkmate(play.turn, board):
                            print('CHECKMATE')
                        else:
                            print('Move possible')
        else:
            coord = cell_coord()
            if board.cells[coord[0]][coord[1]].piece != '' and board.cells[coord[0]][coord[1]].piece.color == play.turn:
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
    
    def alter_lastmove_highlight(self, obj, board):
        if obj != '':
            at = obj.pos
            board.cells[at[0]][at[1]].alter_lastmove_state(board)



def check_incheck(color, board):
    if pieces['king_' + color[0]][0].in_check(board):
        return True
    else:
        return False
