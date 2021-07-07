import pygame as pg
from screen import Screen, screen_
import copy
import os 

cell_size = (Screen.cell_dim, Screen.cell_dim)
piece_size = (Screen.piece_dim, Screen.piece_dim)

KING_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_king_1x_ns.png')), piece_size)
KING_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_king_1x_ns.png')), piece_size)
QUEEN_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_queen_1x_ns.png')), piece_size)
QUEEN_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_queen_1x_ns.png')), piece_size)
BISHOP_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_bishop_1x_ns.png')), piece_size)
BISHOP_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_bishop_1x_ns.png')), piece_size)
KNIGHT_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_knight_1x_ns.png')), piece_size)
KNIGHT_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_knight_1x_ns.png')), piece_size)
ROOK_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_rook_1x_ns.png')), piece_size)
ROOK_B_IMG= pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_rook_1x_ns.png')), piece_size)
PAWN_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_pawn_1x_ns.png')), piece_size)
PAWN_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_pawn_1x_ns.png')), piece_size)
WHITE_CELL_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'square brown light_1x_ns.png')), cell_size) 
BLACK_CELL_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'square brown dark_1x_ns.png')), cell_size) 


KING = {'w' : KING_W_IMG, 'b' : KING_B_IMG}
QUEEN = {'b' : QUEEN_B_IMG, 'w' : QUEEN_W_IMG}
BISHOP = {'w': BISHOP_W_IMG, 'b' : BISHOP_B_IMG}
KNIGHT = {'w' : KNIGHT_W_IMG, 'b' : KNIGHT_B_IMG}
ROOK = {'w' : ROOK_W_IMG, 'b': ROOK_B_IMG}
PAWN = {'w' : PAWN_W_IMG, 'b' : PAWN_B_IMG}
CELL = {'w': WHITE_CELL_IMG, 'b': BLACK_CELL_IMG}


piece_colors = {1 : "white", 0: "black"}

class Colors:
    dark_green = (85, 107, 47)
    light_green = (107, 142, 35) 
    silver = (128,128,128)   
    red = (178, 34, 34)
    def __init():
        pass

class Img:
    def __init__(self, image):
        self.img = image
        self.enhanced_img = self.highlight(copy.copy(image))
        self.enhance = False
        self.last_move = False
        self.in_check = False
        self.last_move_img = self.get_last_move_img(copy.copy(image))
        self.check_img = self.get_check_img(copy.copy(image))

    def highlight(self, image):
        image.fill(Colors.silver) 
        return image

    def show_img(self, pos):
        if(self.enhance):
            screen_.blit(self.enhanced_img, pos)
        elif self.last_move:
            screen_.blit(self.last_move_img, pos)
        elif self.in_check:
            screen_.blit(self.check_img, pos)
        else:
            screen_.blit(self.img, pos)

    def change_enhance(self):
        if self.enhance:
            self.enhance = False
        else:
            self.enhance = True

    def get_last_move_img(self, image):
         image.fill(Colors.light_green)   
         return image

    def get_check_img(self, image):
        image.fill(Colors.red)
        return image
