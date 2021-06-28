import os
import pygame as pg
import math
from load_assets import *
from objects import *
from screen import *
from selection import Selection

pg.init()

class Play:
    def __init__(self, board):
        self.turn = 'white'
        self.initialize_pieces(board)


    def initialize_pieces(self, board):
        global pieces
        pieces['king_w'] = []
        pieces['king_w'].append(King(KING_W_IMG, 'white', (3, 7)))
        board.cells[3][7].change_piece(pieces['king_w'][0])

        pieces['king_b'] = []
        pieces['king_b'].append(King(KING_B_IMG, 'black', (3, 0)))
        board.cells[3][0].change_piece(pieces['king_b'][0])

        pieces['queen_w'] = []
        pieces['queen_w'].append(Queen(QUEEN_W_IMG, 'white', (4, 7)))
        board.cells[4][7].change_piece(pieces['queen_w'][0])

        pieces['queen_b'] = []
        pieces['queen_b'].append(Queen(QUEEN_B_IMG, 'black', (4, 0)))
        board.cells[4][0].change_piece(pieces['queen_b'][0])

        pieces['bishop_w'] = []
        pieces['bishop_b'] = []
        pieces['bishop_w'].append(Bishop(BISHOP_W_IMG, 'white', (2, 7)))
        board.cells[2][7].change_piece(pieces['bishop_w'][0])
        pieces['bishop_w'].append(Bishop(BISHOP_W_IMG, 'white', (5, 7)))
        board.cells[5][7].change_piece(pieces['bishop_w'][1])
        pieces['bishop_b'].append(Bishop(BISHOP_B_IMG, 'black', (2, 0)))
        board.cells[2][0].change_piece(pieces['bishop_b'][0])
        pieces['bishop_b'].append(Bishop(BISHOP_B_IMG, 'black', (5, 0)))
        board.cells[5][0].change_piece(pieces['bishop_b'][1])


        pieces['rook_w'] = []
        pieces['rook_b'] = []
        pieces['rook_w'].append(Rook(ROOK_W_IMG, 'white', (0, 7)))
        board.cells[0][7].change_piece(pieces['rook_w'][0])
        pieces['rook_w'].append(Rook(ROOK_W_IMG, 'white', (7, 7)))
        board.cells[7][7].change_piece(pieces['rook_w'][1])
        pieces['rook_b'].append(Rook(ROOK_B_IMG, 'black', (0, 0)))
        board.cells[0][0].change_piece(pieces['rook_b'][0])
        pieces['rook_b'].append(Rook(ROOK_B_IMG, 'black', (7, 0)))
        board.cells[7][0].change_piece(pieces['rook_b'][1])


        pieces['knight_w'] = []
        pieces['knight_b'] = []
        pieces['knight_w'].append(Knight(KNIGHT_W_IMG, 'white', (1, 7)))
        board.cells[1][7].change_piece(pieces['knight_w'][0])
        pieces['knight_w'].append(Knight(KNIGHT_W_IMG, 'white', (6, 7)))
        board.cells[6][7].change_piece(pieces['knight_w'][1])
        pieces['knight_b'].append(Knight(KNIGHT_B_IMG, 'black', (1, 0)))
        board.cells[1][0].change_piece(pieces['knight_b'][0])
        pieces['knight_b'].append(Knight(KNIGHT_B_IMG, 'black', (6, 0)))
        board.cells[6][0].change_piece(pieces['knight_b'][1])


        pieces['pawn_w'] = []
        for i in range(8):
            pieces['pawn_w'].append(Pawn(PAWN_W_IMG, 'white', (i, 6)))
            board.cells[i][6].change_piece(pieces['pawn_w'][i])

        pieces['pawn_b'] = []
        for i in range(8):
            pieces['pawn_b'].append(Pawn(PAWN_B_IMG, 'black', (i, 1)))
            board.cells[i][1].change_piece(pieces['pawn_b'][i])

    def change_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    

def show_pieces(board):
    for i in range(len(board.cells)):
        for j in range(len(board.cells[0])):
            if board.cells[i][j].piece != '':
                board.cells[i][j].piece.show()

def debug(board):
    for i in board.cells:
        for j in i:
            print(j.piece, end = ', ')
        print('\n')

def main():

    pg.display.set_caption('Chess')

    board = Board()
    play = Play(board)
    select = Selection()
    debug(board)

    start = True
    while start:

        board.show_board()
        show_pieces(board)
        select.highlight_rect(board)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                select.selection_action(board, play)
        pg.display.update()
           
if __name__ == "__main__":
    main()

