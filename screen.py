import pygame as pg

class Screen:
    screen_height = 400
    screen_width = 400
    cell_dim = screen_height // 8
    fract = (8, 10)
    piece_dim = (cell_dim * fract[0]) // fract[1]

screen_ = pg.display.set_mode((Screen.screen_width, Screen.screen_height))


