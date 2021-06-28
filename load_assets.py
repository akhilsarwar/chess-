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


class Img:
    enhance = False
    def __init__(self, image):
        self.img = image
        self.enhanced_img = self.highlight(copy.copy(image))

    def highlight(self, image):
        image.fill((128, 128, 128), special_flags=pg.BLEND_RGB_ADD) 
        return image
    def show_img(self, pos):
        if(self.enhance):
            screen_.blit(self.enhanced_img, pos)
        else:
            screen_.blit(self.img, pos)

    def change_enhance(self):
        if self.enhance:
            self.enhance = False
        else:
            self.enhance = True
