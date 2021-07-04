import pygame as pg
from utility.funcs import cell_coord
from objects import pieces
from checkmate import checkmate
from load_assets import piece_colors

class Selection:
    def __init__(self):
        self.is_selected = False
        self.active_piece = ''
        self.current_block = (-1, -1)

    def selection_action(self, board, play):
        if play.isturn:
            if self.is_selected:
                coord = cell_coord()

                #if the seleceted_block is of the same color as previously selected block
                if self.same_color_select(board, coord):
                    board.cells[self.current_block[0]][self.current_block[1]].img.change_enhance()
                    self.active_piece = board.cells[coord[0]][coord[1]].piece
                    self.current_block = coord

                #if the selected_block is a blank or rival color
                #moves only if it is a valid block
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
                        if check_incheck(piece_colors[not (play.player_no)], board):
                            if checkmate(piece_colors[not (play.player_no)], board):
                                print('CHECKMATE')
                            else:
                                print('Move possible')

            #if no block is currently selected 
            else:
                coord = cell_coord()
                if board.cells[coord[0]][coord[1]].piece != '' and board.cells[coord[0]][coord[1]].piece.color == play.player_color:
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
    
    def alter_lastmove_highlight(self, last_move, board):
        if last_move:
            at = last_move['obj'].pos
            board.cells[at[0]][at[1]].alter_lastmove_state(board)



def check_incheck(color, board):
    if pieces['king_' + color[0]][0].in_check(board):
        return True
    else:
        return False
