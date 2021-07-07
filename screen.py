import pygame as pg

class Screen:
    screen_height = 600
    screen_width = 600
    cell_dim = screen_height // 8
    fract = (8, 10)
    piece_dim = (cell_dim * fract[0]) // fract[1]
