import os
import pygame as pg
import math
from load_assets import *
from objects import *

pg.init()

screen_width_ = 800
screen_height_ = 800
screen_ = pg.display.set_mode((screen_width_, screen_height_))

pieces  = dict()

def initialize_pieces(board):
    global pieces
    pieces['king_w'] = []
    pieces['king_w'].append(King(KING_W_IMG, 'white', centralize_coordinates(board.cells[3][7].pos[0],board.cells[3][7].pos[1]))
    )
    pieces['king_b'] = []
    pieces['king_b'].append(King(KING_B_IMG, 'black', centralize_coordinates(board.cells[3][0].pos[0], board.cells[3][0].pos[1])))
    pieces['queen_w'] = []
    pieces['queen_w'].append(Queen(QUEEN_W_IMG, 'white', centralize_coordinates(board.cells[4][7].pos[0], board.cells[4][7].pos[1])))
    pieces['queen_b'] = []
    pieces['queen_b'].append(Queen(QUEEN_B_IMG, 'black', centralize_coordinates(board.cells[4][0].pos[0], board.cells[4][0].pos[1])))
    pieces['bishop_w'] = []
    pieces['bishop_w'].append(Bishop(BISHOP_W_IMG, 'white', centralize_coordinates(board.cells[2][7].pos[0], board.cells[2][7].pos[1])))
    pieces['bishop_w'].append(Bishop(BISHOP_W_IMG, 'white', centralize_coordinates(board.cells[5][7].pos[0], board.cells[5][7].pos[1])))
    pieces['bishop_b'] = []
    pieces['bishop_b'].append(Bishop(BISHOP_B_IMG, 'black', centralize_coordinates(board.cells[2][0].pos[0], board.cells[2][0].pos[1])))
    pieces['bishop_b'].append(Bishop(BISHOP_B_IMG, 'black', centralize_coordinates(board.cells[5][0].pos[0], board.cells[5][0].pos[1])))
    pieces['rook_w'] = []
    pieces['rook_b'] = []
    pieces['rook_w'].append(Rook(ROOK_W_IMG, 'white', centralize_coordinates(board.cells[0][7].pos[0], board.cells[0][7].pos[1])))
    pieces['rook_w'].append(Rook(ROOK_W_IMG, 'white', centralize_coordinates(board.cells[7][7].pos[0], board.cells[7][7].pos[1])))
    pieces['rook_b'].append(Rook(ROOK_B_IMG, 'black', centralize_coordinates(board.cells[0][0].pos[0], board.cells[0][0].pos[1])))
    pieces['rook_b'].append(Rook(ROOK_B_IMG, 'black', centralize_coordinates(board.cells[7][0].pos[0], board.cells[7][0].pos[1])))
    pieces['knight_w'] = []
    pieces['knight_b'] = []
    pieces['knight_w'].append(Knight(KNIGHT_W_IMG, 'white', centralize_coordinates(board.cells[1][7].pos[0], board.cells[1][7].pos[1])))
    pieces['knight_w'].append(Knight(KNIGHT_W_IMG, 'white', centralize_coordinates(board.cells[6][7].pos[0], board.cells[6][7].pos[1])))
    pieces['knight_b'].append(Knight(KNIGHT_B_IMG, 'black', centralize_coordinates(board.cells[1][0].pos[0], board.cells[1][0].pos[1])))
    pieces['knight_b'].append(Knight(KNIGHT_B_IMG, 'black', centralize_coordinates(board.cells[6][0].pos[0], board.cells[6][0].pos[1])))
    pieces['pawn_w'] = []
    for i in range(8):
        pieces['pawn_w'].append(Pawn(PAWN_W_IMG, 'white', centralize_coordinates(board.cells[i][6].pos[0], board.cells[i][6].pos[1])))
    pieces['pawn_b'] = []
    for i in range(8):
        pieces['pawn_b'].append(Pawn(PAWN_B_IMG, 'black', centralize_coordinates(board.cells[i][1].pos[0], board.cells[i][1].pos[1])))

    

def show_piece(piece_list):
    for p in piece_list:
        p.show()
def show_pieces():
    show_piece(pieces['king_w'])
    show_piece(pieces['king_b'])
    show_piece(pieces['queen_w'])
    show_piece(pieces['queen_b'])
    show_piece(pieces['bishop_w'])
    show_piece(pieces['bishop_b'])
    show_piece(pieces['rook_b'])
    show_piece(pieces['rook_w'])
    show_piece(pieces['knight_b'])
    show_piece(pieces['knight_w'])
    show_piece(pieces['pawn_w'])
    show_piece(pieces['pawn_b'])

def centralize_coordinates(x, y):
    return (x + 10, y + 10)



def main():
    board = Board()
    initialize_pieces(board)
    pg.display.set_caption('Chess')
    play = True
    while play:
#        SCREEN.fill((255, 255, 255))
        board.show_board()
        show_pieces()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        pg.display.update()
           
if __name__ == "__main__":
    main()

