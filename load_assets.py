import pygame as pg
from screen import *
import copy
import os 

KING_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_king_1x_ns.png')), (80, 80))
KING_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_king_1x_ns.png')), (80, 80))
QUEEN_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_queen_1x_ns.png')), (80, 80))
QUEEN_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_queen_1x_ns.png')), (80, 80))
BISHOP_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_bishop_1x_ns.png')), (80, 80))
BISHOP_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_bishop_1x_ns.png')), (80, 80))
KNIGHT_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_knight_1x_ns.png')), (80, 80))
KNIGHT_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_knight_1x_ns.png')), (80, 80))
ROOK_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_rook_1x_ns.png')), (80, 80))
ROOK_B_IMG= pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_rook_1x_ns.png')), (80, 80))
PAWN_W_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'w_pawn_1x_ns.png')), (80, 80))
PAWN_B_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'b_pawn_1x_ns.png')), (80, 80))
WHITE_CELL_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'square brown light_1x_ns.png')), (100, 100)) 
BLACK_CELL_IMG = pg.transform.smoothscale(pg.image.load(os.path.join('assets/1x', 'square brown dark_1x_ns.png')), (100, 100)) 


piece_colors = {1 : "white", 0: "black"}

class Colors:
    dark_green = (85, 107, 47)
    light_green = (107, 142, 35) 
    silver = (128,128,128)   
    def __init():
        pass

class Img:
    def __init__(self, image):
        self.img = image
        self.enhanced_img = self.highlight(copy.copy(image))
        self.enhance = False
        self.last_move = False
        self.last_move_img = self.get_last_move_img(copy.copy(image))

    def highlight(self, image):
        image.fill(Colors.silver) 
        return image

    def show_img(self, pos):
        if(self.enhance):
            screen_.blit(self.enhanced_img, pos)
        else:
            if self.last_move:
                screen_.blit(self.last_move_img, pos)
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
