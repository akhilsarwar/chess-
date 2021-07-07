import pygame as pg

def cell_coord(Screen):
    x, y  = pg.mouse.get_pos()
    ind_x = x // (Screen.screen_width // 8)
    ind_y = y // (Screen.screen_height // 8)
    return (ind_x, ind_y)


def centralize_coordinates(x, y, Screen):
    return (x + (Screen.cell_dim - Screen.piece_dim) // 2, y + (Screen.cell_dim - Screen.piece_dim) // 2)

def rival_color(obj):
    if obj.color == 'white':
        return 'black'
    else:
        return 'white'

