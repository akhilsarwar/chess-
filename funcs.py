import pygame as pg

def cell_coord():
    x, y  = pg.mouse.get_pos()
    ind_x = x // 100
    ind_y = y // 100
    return (ind_x, ind_y)


def centralize_coordinates(x, y):
    return (x + 10, y + 10)
