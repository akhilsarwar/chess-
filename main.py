import os
import pygame as pg
import math
from load_assets import *
from objects import *
from screen import Screen
from selection import Selection


class Play:
    def __init__(self, board, player_no):
        self.isturn = player_no 
        self.player_color = piece_colors[player_no]
        self.player_no = player_no
        self.check_thrown = False
        self.initialize_pieces(board)

    def initialize_pieces(self, board):
        global pieces
        if self.player_color == 'white':
            pieces['king_' + self.player_color[0]] = []
            pieces['king_' + self.player_color[0]].append(King(KING[self.player_color[0]], self.player_color, (3, 7)))
            board.cells[3][7].change_piece(pieces['king_' + self.player_color[0]][0])

            pieces['king_' + piece_colors[not self.player_no][0]] = []
            pieces['king_' + piece_colors[not self.player_no][0]].append(King(KING[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (3, 0)))
            board.cells[3][0].change_piece(pieces['king_' + piece_colors[not self.player_no][0]][0])

            pieces['queen_' + self.player_color[0]] = []
            pieces['queen_' + self.player_color[0]].append(Queen(QUEEN[self.player_color[0]], self.player_color, (4, 7)))
            board.cells[4][7].change_piece(pieces['queen_' + self.player_color[0]][0])

            pieces['queen_' + piece_colors[not self.player_no][0]] = []
            pieces['queen_' + piece_colors[not self.player_no][0]].append(Queen(QUEEN[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (4, 0)))
            board.cells[4][0].change_piece(pieces['queen_' + piece_colors[not self.player_no][0]][0])


            pieces['bishop_' + self.player_color[0]] = []
            pieces['bishop_' + piece_colors[not self.player_no][0]] = []
            pieces['bishop_' + self.player_color[0]].append(Bishop(BISHOP[self.player_color[0]], self.player_color, (2, 7)))
            board.cells[2][7].change_piece(pieces['bishop_' + self.player_color[0]][0])
            pieces['bishop_' + self.player_color[0]].append(Bishop(BISHOP[self.player_color[0]], self.player_color, (5, 7)))
            board.cells[5][7].change_piece(pieces['bishop_' + self.player_color[0]][1])
            pieces['bishop_' + piece_colors[not self.player_no][0]].append(Bishop(BISHOP[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (2, 0)))
            board.cells[2][0].change_piece(pieces['bishop_' + piece_colors[not self.player_no][0]][0])
            pieces['bishop_' + piece_colors[not self.player_no][0]].append(Bishop(BISHOP[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (5, 0)))
            board.cells[5][0].change_piece(pieces['bishop_' + piece_colors[not self.player_no][0]][1])

            pieces['rook_' + self.player_color[0]] = []
            pieces['rook_' + piece_colors[not self.player_no][0]] = []
            pieces['rook_' + self.player_color[0]].append(Rook(ROOK[self.player_color[0]], self.player_color, (0, 7)))
            board.cells[0][7].change_piece(pieces['rook_' + self.player_color[0]][0])
            pieces['rook_' + self.player_color[0]].append(Rook(ROOK[self.player_color[0]], self.player_color, (7, 7)))
            board.cells[7][7].change_piece(pieces['rook_' + self.player_color[0]][1])
            pieces['rook_' + piece_colors[not self.player_no][0]].append(Rook(ROOK[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (0, 0)))
            board.cells[0][0].change_piece(pieces['rook_' + piece_colors[not self.player_no][0]][0])
            pieces['rook_' + piece_colors[not self.player_no][0]].append(Rook(ROOK[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7, 0)))
            board.cells[7][0].change_piece(pieces['rook_' + piece_colors[not self.player_no][0]][1])


            pieces['knight_' + self.player_color[0]] = []
            pieces['knight_' + piece_colors[not self.player_no][0]] = []
            pieces['knight_' + self.player_color[0]].append(Knight(KNIGHT[self.player_color[0]], self.player_color, (1, 7)))
            board.cells[1][7].change_piece(pieces['knight_' + self.player_color[0]][0])
            pieces['knight_' + self.player_color[0]].append(Knight(KNIGHT[self.player_color[0]], self.player_color, (6, 7)))
            board.cells[6][7].change_piece(pieces['knight_' + self.player_color[0]][1])
            pieces['knight_' + piece_colors[not self.player_no][0]].append(Knight(KNIGHT[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (1, 0)))
            board.cells[1][0].change_piece(pieces['knight_' + piece_colors[not self.player_no][0]][0])
            pieces['knight_' + piece_colors[not self.player_no][0]].append(Knight(KNIGHT[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (6, 0)))
            board.cells[6][0].change_piece(pieces['knight_' + piece_colors[not self.player_no][0]][1])



            pieces['pawn_' + self.player_color[0]] = []
            for i in range(8):
                pieces['pawn_' + self.player_color[0]].append(Pawn(PAWN[self.player_color[0]], self.player_color, (i, 6), -1))
                board.cells[i][6].change_piece(pieces['pawn_' + self.player_color[0]][i])

            pieces['pawn_' + piece_colors[not self.player_no][0]] = []
            for i in range(8):
                pieces['pawn_' + piece_colors[not self.player_no][0]].append(Pawn(PAWN[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (i, 1), 1))
                board.cells[i][1].change_piece(pieces['pawn_' + piece_colors[not self.player_no][0]][i])



        else:

            pieces['king_' + self.player_color[0]] = []
            pieces['king_' + self.player_color[0]].append(King(KING[self.player_color[0]], self.player_color, (7 - 3, 7 - 0)))
            board.cells[7 - 3][7 - 0].change_piece(pieces['king_' + self.player_color[0]][0])

            pieces['king_' + piece_colors[not self.player_no][0]] = []
            pieces['king_' + piece_colors[not self.player_no][0]].append(King(KING[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 3, 7 - 7)))
            board.cells[7 - 3][7 - 7].change_piece(pieces['king_' + piece_colors[not self.player_no][0]][0])


            pieces['queen_' + self.player_color[0]] = []
            pieces['queen_' + self.player_color[0]].append(Queen(QUEEN[self.player_color[0]], self.player_color, (7 - 4, 7 - 0)))
            board.cells[7 - 4][7 - 0].change_piece(pieces['queen_' + self.player_color[0]][0])

            pieces['queen_' + piece_colors[not self.player_no][0]] = []
            pieces['queen_' + piece_colors[not self.player_no][0]].append(Queen(QUEEN[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 4, 7 - 7)))
            board.cells[7 - 4][7 - 7].change_piece(pieces['queen_' + piece_colors[not self.player_no][0]][0])


            pieces['bishop_' + self.player_color[0]] = []
            pieces['bishop_' + piece_colors[not self.player_no][0]] = []
            pieces['bishop_' + self.player_color[0]].append(Bishop(BISHOP[self.player_color[0]], self.player_color, (7 - 2, 7 - 0)))
            board.cells[7 - 2][7 - 0].change_piece(pieces['bishop_' + self.player_color[0]][0])
            pieces['bishop_' + self.player_color[0]].append(Bishop(BISHOP[self.player_color[0]], self.player_color, (7 - 5, 7 - 0)))
            board.cells[7 - 5][7 - 0].change_piece(pieces['bishop_' + self.player_color[0]][1])
            pieces['bishop_' + piece_colors[not self.player_no][0]].append(Bishop(BISHOP[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 2, 7 - 7)))
            board.cells[7 - 2][7 - 7].change_piece(pieces['bishop_' + piece_colors[not self.player_no][0]][0])
            pieces['bishop_' + piece_colors[not self.player_no][0]].append(Bishop(BISHOP[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 5, 7 - 7)))
            board.cells[7 - 5][7 - 7].change_piece(pieces['bishop_' + piece_colors[not self.player_no][0]][1])


            pieces['rook_' + self.player_color[0]] = []
            pieces['rook_' + piece_colors[not self.player_no][0]] = []
            pieces['rook_' + self.player_color[0]].append(Rook(ROOK[self.player_color[0]], self.player_color, (7 - 0, 7 - 0)))
            board.cells[7 - 0][7 - 0].change_piece(pieces['rook_' + self.player_color[0]][0])
            pieces['rook_' + self.player_color[0]].append(Rook(ROOK[self.player_color[0]], self.player_color, (7 - 7, 7 - 0)))
            board.cells[7 - 7][7- 0].change_piece(pieces['rook_' + self.player_color[0]][1])
            pieces['rook_' + piece_colors[not self.player_no][0]].append(Rook(ROOK[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 0, 7 - 7)))
            board.cells[7 - 0][7 - 7].change_piece(pieces['rook_' + piece_colors[not self.player_no][0]][0])
            pieces['rook_' + piece_colors[not self.player_no][0]].append(Rook(ROOK[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 7, 7 - 7)))
            board.cells[7 - 7][7 - 7].change_piece(pieces['rook_' + piece_colors[not self.player_no][0]][1])


            pieces['knight_' + self.player_color[0]] = []
            pieces['knight_' + piece_colors[not self.player_no][0]] = []
            pieces['knight_' + self.player_color[0]].append(Knight(KNIGHT[self.player_color[0]], self.player_color, (7 - 1, 7 - 0)))
            board.cells[7 - 1][7 - 0].change_piece(pieces['knight_' + self.player_color[0]][0])
            pieces['knight_' + self.player_color[0]].append(Knight(KNIGHT[self.player_color[0]], self.player_color, (7 - 6, 7 - 0)))
            board.cells[7 - 6][7 - 0].change_piece(pieces['knight_' + self.player_color[0]][1])
            pieces['knight_' + piece_colors[not self.player_no][0]].append(Knight(KNIGHT[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 1, 7 - 7)))
            board.cells[7 - 1][7 - 7].change_piece(pieces['knight_' + piece_colors[not self.player_no][0]][0])
            pieces['knight_' + piece_colors[not self.player_no][0]].append(Knight(KNIGHT[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - 6, 7 - 7)))
            board.cells[7 - 6][7 - 7].change_piece(pieces['knight_' + piece_colors[not self.player_no][0]][1])


            pieces['pawn_' + self.player_color[0]] = []
            for i in range(8):
                pieces['pawn_' + self.player_color[0]].append(Pawn(PAWN[self.player_color[0]], self.player_color, (7 - i, 7 - 1), -1))
                board.cells[7 - i][7 - 1].change_piece(pieces['pawn_' + self.player_color[0]][i])

            pieces['pawn_' + piece_colors[not self.player_no][0]] = []
            for i in range(8):
                pieces['pawn_' + piece_colors[not self.player_no][0]].append(Pawn(PAWN[piece_colors[not self.player_no][0]], piece_colors[not self.player_no], (7 - i, 7 - 6), 1))
                board.cells[7 - i][7 - 6].change_piece(pieces['pawn_' + piece_colors[not self.player_no][0]][i])

    def change_turn(self):
        if self.isturn:
            self.isturn = False
        else:
            self.isturn = True

    

def show_pieces(board, screen):
    for i in range(len(board.cells)):
        for j in range(len(board.cells[0])):
            if board.cells[i][j].piece != '':
                board.cells[i][j].piece.show(screen)

def debug(board):
    for i in board.cells:
        for j in i:
            print(j.piece, end = ', ')
        print('\n')



board = ''
play = ''
select = ''

def main(player_no):
    
    global board, play, select

    pg.init()
    pg.display.set_caption('Chess')
    print('shdbsjhb')
    screen_ = pg.display.set_mode((600, 600))

    board = Board()
    play = Play(board, player_no)
    select = Selection()

    debug(board)

    start = True
    while start:

        board.show_board(screen_)
        show_pieces(board,screen_)
        select.highlight_rect(board)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                select.selection_action(board, play)
        pg.display.update()
           
if __name__ == "__main__":
    main(1)

