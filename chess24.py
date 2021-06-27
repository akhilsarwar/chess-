import os
import pygame as pg
import numpy as np
import math
from pygame import mixer


pg.init()
KING_B = pg.image.load(os.path.join('images', 'king.png'))
QUEEN_B = pg.image.load(os.path.join('images', 'queen.png'))
KING_W = pg.image.load(os.path.join('images', 'king1.png'))
QUEEN_W = pg.image.load(os.path.join('images', 'queen1.png'))
BISHOP_W = pg.image.load(os.path.join('images', 'bishop1.png'))
BISHOP_B = pg.image.load(os.path.join('images', 'bishop.png'))
KNIGHT_W = pg.image.load(os.path.join('images', 'knight1.png'))
KNIGHT_B = pg.image.load(os.path.join('images', 'knight.png'))
PAWN_W = pg.image.load(os.path.join('images', 'pawn1.png'))
PAWN_B = pg.image.load(os.path.join('images', 'pawn.png'))
ROOK_W = pg.image.load(os.path.join('images', 'rook1.png'))
ROOK_B = pg.image.load(os.path.join('images', 'rook.png'))
BG_IMG = pg.transform.scale(pg.image.load(os.path.join('images', 'board 3.jpg')), (800, 800))
IND_IMG= pg.image.load(os.path.join('images', 'classic_chess.jpg'))
Font= pg.font.SysFont('impact', 70)
Font2= pg.font.SysFont('impact', 32)
MOVE=mixer.Sound(os.path.join('sound', 'move2.wav'))
#BGM=mixer.music.load(os.path.join('sound', 'BGM.mp3'))
CHECK_SOUND=mixer.Sound(os.path.join('sound', 'checkmate.wav'))

def calc_cell(pix):
    while 1:
        (mouse_x, mouse_y) = pg.mouse.get_pos()

        for i in range(8):
            for j in range(8):
                if math.sqrt(pow((pix[i] - mouse_x), 2) + pow((pix[j] - mouse_y), 2)) < 40:

                    return j, i

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                continue



def checking_pawn_w():
    
    pix=central_pixel
    for p in pawn_w:
        for item in cell:
            if p in item:

                x=p.cell_x
                y=p.cell_y
                if x-1>=0:
                    if cell[x-1][y]==' ':
                        cell[x-1][y]=p
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x][y]=p
                            cell[x-1][y]=' '

                        else:
                            cell[x][y] = p
                            cell[x - 1][y] = ' '
                            return 0

                if p.move_no==1:
                    if x-2>=0:
                        if cell[x - 1][y]== ' ':
                            if cell[x-2][y]==' ':
                                cell[x - 2][y] = p
                                cell[x][y] = ' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x][y] = p
                                    cell[x - 2][y] = ' '

                                else:
                                    cell[x][y] = p
                                    cell[x - 2][y] = ' '
                                    return 0
                if x-1>=0 and y-1>=0:
                    if cell[x-1][y-1]!=' ':
                        if cell[x-1][y-1].color!=p.color:
                            obj=cell[x-1][y-1]
                            cell[x-1][y-1]=p
                            cell[x][y]=' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y]=p
                                cell[x-1][y-1]=obj
                            else:
                                cell[x][y] = p
                                cell[x - 1][y - 1] = obj
                                return 0
                if x-1>=0 and y+1<=7:
                    if cell[x-1][y+1]!=' ':
                        if cell[x-1][y+1].color!=p.color:
                            obj=cell[x-1][y+1]
                            cell[x-1][y+1]=p
                            cell[x][y]=' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y]=p
                                cell[x-1][y+1]=obj
                            else:
                                cell[x][y] = p
                                cell[x - 1][y + 1] = obj
                                return 0

    return 1

def checking_pawn_b():
    
    pix = central_pixel
    for p in pawn_b:
        for item in cell:
            if p in item:

                x = p.cell_x
                y = p.cell_y
                if x+1<=7:
                    if cell[x + 1][y] == ' ':
                        cell[x + 1][y] = p
                        cell[x][y] = ' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                            cell[x][y] = p
                            cell[x + 1][y] = ' '

                        else:
                            cell[x][y] = p
                            cell[x + 1][y] = ' '
                            return 0
                if x+2<=7:
                    if p.move_no == 1:
                        if cell[x + 1][y] == ' ':
                            if cell[x + 2][y] == ' ':
                                cell[x + 2][y] = p
                                cell[x][y] = ' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x][y] = p
                                    cell[x + 2][y] = ' '

                                else:
                                    cell[x][y] = p
                                    cell[x + 2][y] = ' '
                                    return 0
                if x+1<=7 and y-1>=0:
                    if cell[x + 1][y - 1] != ' ':
                        if cell[x + 1][y - 1].color != p.color:
                            obj = cell[x + 1][y - 1]
                            cell[x + 1][y - 1] = p
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y] = p
                                cell[x + 1][y - 1] = obj
                            else:
                                cell[x][y] = p
                                cell[x + 1][y - 1] = obj
                                return 0
                if x+1 <=7 and y+1<=7:
                    if cell[x + 1][y + 1]!= ' ':
                        if cell[x + 1][y + 1].color != p.color:
                            obj = cell[x + 1][y + 1]
                            cell[x + 1][y + 1] = p
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y] = p
                                cell[x + 1][y + 1] = obj
                            else:
                                cell[x][y] = p
                                cell[x + 1][y + 1] = obj
                                return 0
    return  1


def checking_rook_w():

    
    pix = central_pixel
    for r in rook_w:
        block = 0
        block2 = 0
        block3 = 0
        block4 = 0
        for item in cell:
            if r in item:
                x = r.cell_x
                y = r.cell_y

                for i in range(1, 8):
                    if x - i >= 0 and block==0:
                        if cell[x - i][y] == ' ':
                            cell[x - i][y] = r
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                cell[x-i][y]=' '
                                cell[x][y]=r
                            else:
                                cell[x - i][y] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x-i][y]!=' ':
                            block = 1
                            if cell[x-i][y].color!=r.color:
                                obj = cell[x-i][y]
                                cell[x][y]=' '
                                cell[x-i][y]=r

                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                    cell[x-i][y]=obj
                                    cell[x][y]=r
                                else:
                                    cell[x - i][y] = obj
                                    cell[x][y] = r
                                    return 0

                    if x + i <= 7 and block2 == 0:
                        if cell[x + i][y] == ' ':
                            cell[x + i][y] = r
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x + i][y] = ' '
                                cell[x][y] = r
                            else:
                                cell[x + i][y] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x + i][y] != ' ':
                            block2 = 1
                            if cell[x + i][y].color != r.color:
                                obj = cell[x + i][y]
                                cell[x][y] = ' '
                                cell[x + i][y] = r

                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x + i][y] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x + i][y] = obj
                                    cell[x][y] = r
                                    return 0

                    if y + i <=7 and block3 == 0:
                        if cell[x][y+i] == ' ':
                            cell[x][y+i] = r
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y+i] = ' '
                                cell[x][y] = r
                            else:
                                cell[x][y+i] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x][y+i] != ' ':
                            block3 = 1
                            if cell[x][y+i].color != r.color:
                                obj = cell[x][y+i]
                                cell[x][y] = ' '
                                cell[x][y+i] = r

                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x][y+i] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x][y+i] = obj
                                    cell[x][y] = r
                                    return 0
                    if y - i >=0 and block4 == 0:
                        if cell[x][y-i] == ' ':
                            cell[x][y-i] = r
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y-i] = ' '
                                cell[x][y] = r
                            else:
                                cell[x][y-i] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x][y-i] != ' ':
                            block4 = 1
                            if cell[x][y-i].color != r.color:
                                obj = cell[x][y-i]
                                cell[x][y] = ' '
                                cell[x][y-i] = r

                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x][y-i] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x][y-i] = obj
                                    cell[x][y] = r
                                    return 0
    return 1


def checking_rook_b():

    
    pix = central_pixel
    for r in rook_b:
        block = 0
        block2 = 0
        block3 = 0
        block4 = 0
        for item in cell:
            if r in item:
                x = r.cell_x
                y = r.cell_y

                for i in range(1, 8):
                    if x - i >= 0 and block == 0:
                        if cell[x - i][y] == ' ':
                            cell[x - i][y] = r
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x - i][y] = ' '
                                cell[x][y] = r
                            else:
                                cell[x - i][y] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x - i][y] != ' ':
                            block = 1
                            if cell[x - i][y].color != r.color:
                                obj = cell[x - i][y]
                                cell[x][y] = ' '
                                cell[x - i][y] = r

                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x - i][y] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x - i][y] = obj
                                    cell[x][y] = r
                                    return 0

                    if x + i <= 7 and block2 == 0:
                        if cell[x + i][y] == ' ':
                            cell[x + i][y] = r
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:

                                cell[x + i][y] = ' '
                                cell[x][y] = r
                            else:
                                cell[x + i][y] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x + i][y] != ' ':
                            block2 = 1
                            if cell[x + i][y].color != r.color:
                                obj = cell[x + i][y]
                                cell[x][y] = ' '
                                cell[x + i][y] = r

                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x + i][y] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x + i][y] = obj
                                    cell[x][y] = r
                                    return 0

                    if y + i <= 7 and block3 == 0:
                        if cell[x][y + i] == ' ':
                            cell[x][y + i] = r
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y + i] = ' '
                                cell[x][y] = r
                            else:
                                cell[x][y + i] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x][y + i] != ' ':
                            block3 = 1
                            if cell[x][y + i].color != r.color:
                                obj = cell[x][y + i]
                                cell[x][y] = ' '
                                cell[x][y + i] = r

                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x][y + i] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x][y + i] = obj
                                    cell[x][y] = r
                                    return 0
                    if y - i >= 0 and block4 == 0:
                        if cell[x][y - i] == ' ':
                            cell[x][y - i] = r
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y - i] = ' '
                                cell[x][y] = r
                            else:
                                cell[x][y - i] = ' '
                                cell[x][y] = r
                                return 0
                        if cell[x][y - i] != ' ':
                            block4 = 1
                            if cell[x][y - i].color != r.color:
                                obj = cell[x][y - i]
                                cell[x][y] = ' '
                                cell[x][y - i] = r

                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x][y - i] = obj
                                    cell[x][y] = r
                                else:
                                    cell[x][y - i] = obj
                                    cell[x][y] = r
                                    return 0
    return 1

def checking_bishop_w():
    pix=central_pixel
    for b in bishop_w:
        block=0
        block2=0
        block3=0
        block4=0
        for item in cell:
            if b in item:
                x=b.cell_x
                y=b.cell_y

                for i in range(1,8):
                    if x-i >=0 and y-i>=0:
                        if block==0:
                            if cell[x-i][y-i]==' ':
                                cell[x-i][y-i]=b
                                cell[x][y]=' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                    cell[x-i][y-i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x - i][y - i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x-i][y-i]!=' ':
                                block=1
                                if cell[x-i][y-i].color!=b.color:
                                    obj=cell[x-i][y-i]
                                    cell[x-i][y-i]=b
                                    cell[x][y]=' '
                                    if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                        cell[x-i][y-i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x - i][y - i] = obj
                                        cell[x][y] = b
                                        return 0
                    if x+i <=7 and y+i<=7:
                        if block2==0:
                            if cell[x+i][y+i]==' ':
                                cell[x+i][y+i]=b
                                cell[x][y]=' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                    cell[x+i][y+i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x + i][y + i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x+i][y+i]!=' ':
                                block2=1
                                if cell[x+i][y+i].color!=b.color:
                                    obj=cell[x+i][y+i]
                                    cell[x+i][y+i]=b
                                    cell[x][y]=' '
                                    if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                        cell[x+i][y+i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x + i][y + i] = obj
                                        cell[x][y] = b
                                        return 0

                    if x-i >=0 and y+i<=7:
                        if block3==0:
                            if cell[x-i][y+i]==' ':
                                cell[x-i][y+i]=b
                                cell[x][y]=' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                    cell[x-i][y+i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x - i][y + i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x-i][y+i]!=' ':
                                block3=1
                                if cell[x-i][y+i].color!=b.color:
                                    obj=cell[x-i][y+i]
                                    cell[x-i][y+i]=b
                                    cell[x][y]=' '
                                    if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                        cell[x-i][y+i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x - i][y + i] = obj
                                        cell[x][y] = b
                                        return 0
                    if x+i <=7 and y-i>=0:
                        if block4==0:
                            if cell[x+i][y-i]==' ':
                                cell[x+i][y-i]=b
                                cell[x][y]=' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                    cell[x+i][y-i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x + i][y - i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x+i][y-i]!=' ':
                                block4=1
                                if cell[x+i][y-i].color!=b.color:
                                    obj=cell[x+i][y-i]
                                    cell[x+i][y-i]=b
                                    cell[x][y]=' '
                                    if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                                        cell[x+i][y-i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x + i][y - i] = obj
                                        cell[x][y] = b
                                        return 0


    return 1


def checking_bishop_b():
    pix=central_pixel
    for b in bishop_b:
        block=0
        block2=0
        block3=0
        block4=0
        for item in cell:
            if b in item:
                x=b.cell_x
                y=b.cell_y

                for i in range(1,8):
                    if x-i >=0 and y-i>=0:
                        if block==0:
                            if cell[x-i][y-i]==' ':
                                cell[x-i][y-i]=b
                                cell[x][y]=' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                    cell[x-i][y-i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x - i][y - i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x-i][y-i]!=' ':
                                block=1
                                if cell[x-i][y-i].color!=b.color:
                                    obj=cell[x-i][y-i]
                                    cell[x-i][y-i]=b
                                    cell[x][y]=' '
                                    if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                        cell[x-i][y-i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x - i][y - i] = obj
                                        cell[x][y] = b
                                        return 0
                    if x+i <=7 and y+i<=7:
                        if block2==0:
                            if cell[x+i][y+i]==' ':
                                cell[x+i][y+i]=b
                                cell[x][y]=' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                    cell[x+i][y+i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x + i][y + i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x+i][y+i]!=' ':
                                block2=1
                                if cell[x+i][y+i].color!=b.color:
                                    obj=cell[x+i][y+i]
                                    cell[x+i][y+i]=b
                                    cell[x][y]=' '
                                    if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                        cell[x+i][y+i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x + i][y + i] = obj
                                        cell[x][y] = b
                                        return 0

                    if x-i >=0 and y+i<=7:
                        if block3==0:
                            if cell[x-i][y+i]==' ':
                                cell[x-i][y+i]=b
                                cell[x][y]=' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                    cell[x-i][y+i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x - i][y + i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x-i][y+i]!=' ':
                                block3=1
                                if cell[x-i][y+i].color!=b.color:
                                    obj=cell[x-i][y+i]
                                    cell[x-i][y+i]=b
                                    cell[x][y]=' '
                                    if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                        cell[x-i][y+i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x - i][y + i] = obj
                                        cell[x][y] = b
                                        return 0
                    if x+i <=7 and y-i>=0:
                        if block4==0:
                            if cell[x+i][y-i]==' ':
                                cell[x+i][y-i]=b
                                cell[x][y]=' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                    cell[x+i][y-i]=' '
                                    cell[x][y]=b
                                else:
                                    cell[x + i][y - i] = ' '
                                    cell[x][y] = b
                                    return 0
                            if cell[x+i][y-i]!=' ':
                                block4=1
                                if cell[x+i][y-i].color!=b.color:
                                    obj=cell[x+i][y-i]
                                    cell[x+i][y-i]=b
                                    cell[x][y]=' '
                                    if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                        cell[x+i][y-i]=obj
                                        cell[x][y]=b
                                    else:
                                        cell[x + i][y - i] = obj
                                        cell[x][y] = b
                                        return 0


    return 1


def checking_queen_b():
    pix=central_pixel
    q=queen_b
    block = 0
    block2 = 0
    block3 = 0
    block4 = 0
    block5 = 0
    block6 = 0
    block7 = 0
    block8 = 0
    for item in cell:
        if q in item:
            x=q.cell_x
            y=q.cell_y

            for i in range(1, 8):
                if x - i >= 0 and y - i >= 0:
                    if block == 0:
                        if cell[x - i][y - i] == ' ':
                            cell[x - i][y - i] = q
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x - i][y - i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x - i][y - i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x - i][y - i] != ' ':
                            block = 1
                            if cell[x - i][y - i].color != q.color:
                                obj = cell[x - i][y - i]
                                cell[x - i][y - i] = q
                                cell[x][y] = ' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x - i][y - i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x - i][y - i] = obj
                                    cell[x][y] = q
                                    return 0
                if x + i <= 7 and y + i <= 7:
                    if block2 == 0:
                        if cell[x + i][y + i] == ' ':
                            cell[x + i][y + i] = q
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x + i][y + i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x + i][y + i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x + i][y + i] != ' ':
                            block2 = 1
                            if cell[x + i][y + i].color != q.color:
                                obj = cell[x + i][y + i]
                                cell[x + i][y + i] = q
                                cell[x][y] = ' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x + i][y + i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x + i][y + i] = obj
                                    cell[x][y] = q
                                    return 0

                if x - i >= 0 and y + i <= 7:
                    if block3 == 0:
                        if cell[x - i][y + i] == ' ':
                            cell[x - i][y + i] = q
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x - i][y + i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x - i][y + i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x - i][y + i] != ' ':
                            block3 = 1
                            if cell[x - i][y + i].color != q.color:
                                obj = cell[x - i][y + i]
                                cell[x - i][y + i] = q
                                cell[x][y] = ' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x - i][y + i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x - i][y + i] = obj
                                    cell[x][y] = q
                                    return 0
                if x + i <= 7 and y - i >= 0:
                    if block4 == 0:
                        if cell[x + i][y - i] == ' ':
                            cell[x + i][y - i] = q
                            cell[x][y] = ' '
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x + i][y - i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x + i][y - i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x + i][y - i] != ' ':
                            block4 = 1
                            if cell[x + i][y - i].color != q.color:
                                obj = cell[x + i][y - i]
                                cell[x + i][y - i] = q
                                cell[x][y] = ' '
                                if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                    cell[x + i][y - i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x + i][y - i] = obj
                                    cell[x][y] = q
                                    return 0

                if x - i >= 0 and block5 == 0:
                    if cell[x - i][y] == ' ':
                        cell[x - i][y] = q
                        cell[x][y] = ' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                            cell[x - i][y] = ' '
                            cell[x][y] = q
                        else:
                            cell[x - i][y] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x - i][y] != ' ':
                        block5 = 1
                        if cell[x - i][y].color != q.color:
                            obj = cell[x - i][y]
                            cell[x][y] = ' '
                            cell[x - i][y] = q

                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x - i][y] = obj
                                cell[x][y] = q
                            else:
                                cell[x - i][y] = obj
                                cell[x][y] = q
                                return 0

                if x + i <= 7 and block6 == 0:
                    if cell[x + i][y] == ' ':
                        cell[x + i][y] = q
                        cell[x][y] = ' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:

                            cell[x + i][y] = ' '
                            cell[x][y] = q
                        else:
                            cell[x + i][y] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x + i][y] != ' ':
                        block6 = 1
                        if cell[x + i][y].color != q.color:
                            obj = cell[x + i][y]
                            cell[x][y] = ' '
                            cell[x + i][y] = q

                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x + i][y] = obj
                                cell[x][y] = q
                            else:
                                cell[x + i][y] = obj
                                cell[x][y] = q
                                return 0

                if y + i <= 7 and block7 == 0:
                    if cell[x][y + i] == ' ':
                        cell[x][y + i] = q
                        cell[x][y] = ' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                            cell[x][y + i] = ' '
                            cell[x][y] = q
                        else:
                            cell[x][y + i] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x][y + i] != ' ':
                        block7 = 1
                        if cell[x][y + i].color != q.color:
                            obj = cell[x][y + i]
                            cell[x][y] = ' '
                            cell[x][y + i] = q

                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y + i] = obj
                                cell[x][y] = q
                            else:
                                cell[x][y + i] = obj
                                cell[x][y] = q
                                return 0
                if y - i >= 0 and block8 == 0:
                    if cell[x][y - i] == ' ':
                        cell[x][y - i] = q
                        cell[x][y] = ' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                            cell[x][y - i] = ' '
                            cell[x][y] = q
                        else:
                            cell[x][y - i] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x][y - i] != ' ':
                        block8 = 1
                        if cell[x][y - i].color != q.color:
                            obj = cell[x][y - i]
                            cell[x][y] = ' '
                            cell[x][y - i] = q

                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y) == 1:
                                cell[x][y - i] = obj
                                cell[x][y] = q
                            else:
                                cell[x][y - i] = obj
                                cell[x][y] = q
                                return 0

    return 1

def checking_queen_w():
    pix=central_pixel
    q=queen_w
    block = 0
    block2 = 0
    block3 = 0
    block4 = 0
    block5 = 0
    block6 = 0
    block7 = 0
    block8 = 0
    for item in cell:
        if q in item:
            x=q.cell_x
            y=q.cell_y

            for i in range(1, 8):
                if x - i >= 0 and y - i >= 0:
                    if block == 0:
                        if cell[x - i][y - i] == ' ':
                            cell[x - i][y - i] = q
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x - i][y - i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x - i][y - i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x - i][y - i] != ' ':
                            block = 1
                            if cell[x - i][y - i].color != q.color:
                                obj = cell[x - i][y - i]
                                cell[x - i][y - i] = q
                                cell[x][y] = ' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x - i][y - i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x - i][y - i] = obj
                                    cell[x][y] = q
                                    return 0
                if x + i <= 7 and y + i <= 7:
                    if block2 == 0:
                        if cell[x + i][y + i] == ' ':
                            cell[x + i][y + i] = q
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x + i][y + i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x + i][y + i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x + i][y + i] != ' ':
                            block2 = 1
                            if cell[x + i][y + i].color != q.color:
                                obj = cell[x + i][y + i]
                                cell[x + i][y + i] = q
                                cell[x][y] = ' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x + i][y + i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x + i][y + i] = obj
                                    cell[x][y] = q
                                    return 0

                if x - i >= 0 and y + i <= 7:
                    if block3 == 0:
                        if cell[x - i][y + i] == ' ':
                            cell[x - i][y + i] = q
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x - i][y + i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x - i][y + i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x - i][y + i] != ' ':
                            block3 = 1
                            if cell[x - i][y + i].color != q.color:
                                obj = cell[x - i][y + i]
                                cell[x - i][y + i] = q
                                cell[x][y] = ' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x - i][y + i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x - i][y + i] = obj
                                    cell[x][y] = q
                                    return 0
                if x + i <= 7 and y - i >= 0:
                    if block4 == 0:
                        if cell[x + i][y - i] == ' ':
                            cell[x + i][y - i] = q
                            cell[x][y] = ' '
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x + i][y - i] = ' '
                                cell[x][y] = q
                            else:
                                cell[x + i][y - i] = ' '
                                cell[x][y] = q
                                return 0
                        if cell[x + i][y - i] != ' ':
                            block4 = 1
                            if cell[x + i][y - i].color != q.color:
                                obj = cell[x + i][y - i]
                                cell[x + i][y - i] = q
                                cell[x][y] = ' '
                                if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                    cell[x + i][y - i] = obj
                                    cell[x][y] = q
                                else:
                                    cell[x + i][y - i] = obj
                                    cell[x][y] = q
                                    return 0

                if x - i >= 0 and block5 == 0:
                    if cell[x - i][y] == ' ':
                        cell[x - i][y] = q
                        cell[x][y] = ' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                            cell[x - i][y] = ' '
                            cell[x][y] = q
                        else:
                            cell[x - i][y] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x - i][y] != ' ':
                        block5 = 1
                        if cell[x - i][y].color != q.color:
                            obj = cell[x - i][y]
                            cell[x][y] = ' '
                            cell[x - i][y] = q

                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x - i][y] = obj
                                cell[x][y] = q
                            else:
                                cell[x - i][y] = obj
                                cell[x][y] = q
                                return 0

                if x + i <= 7 and block6 == 0:
                    if cell[x + i][y] == ' ':
                        cell[x + i][y] = q
                        cell[x][y] = ' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:

                            cell[x + i][y] = ' '
                            cell[x][y] = q
                        else:
                            cell[x + i][y] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x + i][y] != ' ':
                        block6 = 1
                        if cell[x + i][y].color != q.color:
                            obj = cell[x + i][y]
                            cell[x][y] = ' '
                            cell[x + i][y] = q

                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x + i][y] = obj
                                cell[x][y] = q
                            else:
                                cell[x + i][y] = obj
                                cell[x][y] = q
                                return 0

                if y + i <= 7 and block7 == 0:
                    if cell[x][y + i] == ' ':
                        cell[x][y + i] = q
                        cell[x][y] = ' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                            cell[x][y + i] = ' '
                            cell[x][y] = q
                        else:
                            cell[x][y + i] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x][y + i] != ' ':
                        block7 = 1
                        if cell[x][y + i].color != q.color:
                            obj = cell[x][y + i]
                            cell[x][y] = ' '
                            cell[x][y + i] = q

                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y + i] = obj
                                cell[x][y] = q
                            else:
                                cell[x][y + i] = obj
                                cell[x][y] = q
                                return 0
                if y - i >= 0 and block8 == 0:
                    if cell[x][y - i] == ' ':
                        cell[x][y - i] = q
                        cell[x][y] = ' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                            cell[x][y - i] = ' '
                            cell[x][y] = q
                        else:
                            cell[x][y - i] = ' '
                            cell[x][y] = q
                            return 0
                    if cell[x][y - i] != ' ':
                        block8 = 1
                        if cell[x][y - i].color != q.color:
                            obj = cell[x][y - i]
                            cell[x][y] = ' '
                            cell[x][y - i] = q

                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x][y - i] = obj
                                cell[x][y] = q
                            else:
                                cell[x][y - i] = obj
                                cell[x][y] = q
                                return 0

    return 1


def checking_knight_w():
    pix=central_pixel
    for k in knight_w:
        for item in cell:
            if k in item:
                x=k.cell_x
                y=k.cell_y


                if x+1<=7 and y+2<=7:
                    if cell[x+1][y+2]==' ':
                        cell[x+1][y+2]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x+1][y+2]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 1][y + 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+1][y+2]!=' ':
                        if cell[x+1][y+2].color!=k.color:
                            obj=cell[x+1][y+2]
                            cell[x][y]=' '
                            cell[x+1][y+2]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x+1][y+2]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 1][y + 2] = obj
                                cell[x][y] = k
                                return 0

                if x+1<=7 and y-2>=0:
                    if cell[x+1][y-2]==' ':
                        cell[x+1][y-2]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x+1][y-2]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 1][y - 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+1][y-2]!=' ':
                        if cell[x+1][y-2].color!=k.color:
                            obj=cell[x+1][y-2]
                            cell[x][y]=' '
                            cell[x+1][y-2]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x+1][y-2]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 1][y - 2] = obj
                                cell[x][y] = k
                                return 0

                if x-1>=0 and y+2<=7:
                    if cell[x-1][y+2]==' ':
                        cell[x-1][y+2]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x-1][y+2]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 1][y + 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-1][y+2]!=' ':
                        if cell[x-1][y+2].color!=k.color:
                            obj=cell[x-1][y+2]
                            cell[x][y]=' '
                            cell[x-1][y+2]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x-1][y+2]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 1][y + 2] = obj
                                cell[x][y] = k
                                return 0

                if x-1>=0 and y-2>=0:
                    if cell[x-1][y-2]==' ':
                        cell[x-1][y-2]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x-1][y-2]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 1][y - 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-1][y-2]!=' ':
                        if cell[x-1][y-2].color!=k.color:
                            obj=cell[x-1][y-2]
                            cell[x][y]=' '
                            cell[x-1][y-2]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x-1][y-2]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 1][y - 2] = obj
                                cell[x][y] = k
                                return 0
                if x+2<=7 and y+1<=7:
                    if cell[x+2][y+1]==' ':
                        cell[x+2][y+1]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x+2][y+1]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 2][y + 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+2][y+1]!=' ':
                        if cell[x+2][y+1].color!=k.color:
                            obj=cell[x+2][y+1]
                            cell[x][y]=' '
                            cell[x+2][y+1]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x+2][y+1]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 2][y + 1] = obj
                                cell[x][y] = k
                                return 0
                if x+2<=7 and y-1>=0:
                    if cell[x+2][y-1]==' ':
                        cell[x+2][y-1]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x+2][y-1]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 2][y - 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+2][y-1]!=' ':
                        if cell[x+2][y-1].color!=k.color:
                            obj=cell[x+2][y-1]
                            cell[x][y]=' '
                            cell[x+2][y-1]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x+2][y-1]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 2][y - 1] = obj
                                cell[x][y] = k
                                return 0
                if x-2>=0 and y+1<=7:
                    if cell[x-2][y+1]==' ':
                        cell[x-2][y+1]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x-2][y+1]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 2][y + 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-2][y+1]!=' ':
                        if cell[x-2][y+1].color!=k.color:
                            obj=cell[x-2][y+1]
                            cell[x][y]=' '
                            cell[x-2][y+1]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x-2][y+1]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 2][y + 1] = obj
                                cell[x][y] = k
                                return 0

                if x-2>=0 and y-1>=0:
                    if cell[x-2][y-1]==' ':
                        cell[x-2][y-1]=k
                        cell[x][y]=' '
                        if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y)==1:
                            cell[x-2][y-1]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 2][y - 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-2][y-1]!=' ':
                        if cell[x-2][y-1].color!=k.color:
                            obj=cell[x-2][y-1]
                            cell[x][y]=' '
                            cell[x-2][y-1]=k
                            if king_w.check(cell, pix, king_w.cell_x, king_w.cell_y) == 1:
                                cell[x-2][y-1]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 2][y - 1] = obj
                                cell[x][y] = k
                                return 0


    return 1


def checking_knight_b():
    pix=central_pixel
    for k in knight_b:
        for item in cell:
            if k in item:
                x=k.cell_x
                y=k.cell_y


                if x+1<=7 and y+2<=7:
                    if cell[x+1][y+2]==' ':
                        cell[x+1][y+2]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x+1][y+2]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 1][y + 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+1][y+2]!=' ':
                        if cell[x+1][y+2].color!=k.color:
                            obj=cell[x+1][y+2]
                            cell[x][y]=' '
                            cell[x+1][y+2]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x+1][y+2]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 1][y + 2] = obj
                                cell[x][y] = k
                                return 0

                if x+1<=7 and y-2>=0:
                    if cell[x+1][y-2]==' ':
                        cell[x+1][y-2]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x+1][y-2]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 1][y - 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+1][y-2]!=' ':
                        if cell[x+1][y-2].color!=k.color:
                            obj=cell[x+1][y-2]
                            cell[x][y]=' '
                            cell[x+1][y-2]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x+1][y-2]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 1][y - 2] = obj
                                cell[x][y] = k
                                return 0

                if x-1>=0 and y+2<=7:
                    if cell[x-1][y+2]==' ':
                        cell[x-1][y+2]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x-1][y+2]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 1][y + 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-1][y+2]!=' ':
                        if cell[x-1][y+2].color!=k.color:
                            obj=cell[x-1][y+2]
                            cell[x][y]=' '
                            cell[x-1][y+2]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x-1][y+2]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 1][y + 2] = obj
                                cell[x][y] = k
                                return 0

                if x-1>=0 and y-2>=0:
                    if cell[x-1][y-2]==' ':
                        cell[x-1][y-2]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x-1][y-2]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 1][y - 2] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-1][y-2]!=' ':
                        if cell[x-1][y-2].color!=k.color:
                            obj=cell[x-1][y-2]
                            cell[x][y]=' '
                            cell[x-1][y-2]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x-1][y-2]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 1][y - 2] = obj
                                cell[x][y] = k
                                return 0
                if x+2<=7 and y+1<=7:
                    if cell[x+2][y+1]==' ':
                        cell[x+2][y+1]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x+2][y+1]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 2][y + 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+2][y+1]!=' ':
                        if cell[x+2][y+1].color!=k.color:
                            obj=cell[x+2][y+1]
                            cell[x][y]=' '
                            cell[x+2][y+1]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x+2][y+1]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 2][y + 1] = obj
                                cell[x][y] = k
                                return 0
                if x+2<=7 and y-1>=0:
                    if cell[x+2][y-1]==' ':
                        cell[x+2][y-1]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x+2][y-1]=' '
                            cell[x][y]=k
                        else:
                            cell[x + 2][y - 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x+2][y-1]!=' ':
                        if cell[x+2][y-1].color!=k.color:
                            obj=cell[x+2][y-1]
                            cell[x][y]=' '
                            cell[x+2][y-1]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x+2][y-1]=obj
                                cell[x][y]=k
                            else:
                                cell[x + 2][y - 1] = obj
                                cell[x][y] = k
                                return 0
                if x-2>=0 and y+1<=7:
                    if cell[x-2][y+1]==' ':
                        cell[x-2][y+1]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x-2][y+1]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 2][y + 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-2][y+1]!=' ':
                        if cell[x-2][y+1].color!=k.color:
                            obj=cell[x-2][y+1]
                            cell[x][y]=' '
                            cell[x-2][y+1]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x-2][y+1]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 2][y + 1] = obj
                                cell[x][y] = k
                                return 0

                if x-2>=0 and y-1>=0:
                    if cell[x-2][y-1]==' ':
                        cell[x-2][y-1]=k
                        cell[x][y]=' '
                        if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                            cell[x-2][y-1]=' '
                            cell[x][y]=k
                        else:
                            cell[x - 2][y - 1] = ' '
                            cell[x][y] = k
                            return 0
                    elif cell[x-2][y-1]!=' ':
                        if cell[x-2][y-1].color!=k.color:
                            obj=cell[x-2][y-1]
                            cell[x][y]=' '
                            cell[x-2][y-1]=k
                            if king_b.check(cell, pix, king_b.cell_x, king_b.cell_y)==1:
                                cell[x-2][y-1]=obj
                                cell[x][y]=k
                            else:
                                cell[x - 2][y - 1] = obj
                                cell[x][y] = k
                                return 0


    return 1

def checking_king_w():
    pix=central_pixel
    K=king_w
    if K==king_w:
        x=K.cell_x
        y=K.cell_y

        if x+1<=7:
            if cell[x+1][y]==' ':
                cell[x+1][y]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x+1, y)==1:
                    cell[x+1][y]=' '
                    cell[x][y]=K
                else:
                    cell[x + 1][y] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x+1][y]!=' ':
                if cell[x+1][y].color!=K.color:
                    obj=cell[x+1][y]
                    cell[x+1][y]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x + 1, y) == 1:
                        cell[x+1][y]=obj
                        cell[x][y]=K
                    else:
                        cell[x + 1][y] = obj
                        cell[x][y] = K
                        return 0
        if x-1>=0:
            if cell[x-1][y]==' ':
                cell[x-1][y]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x-1, y)==1:
                    cell[x-1][y]=' '
                    cell[x][y]=K
                else:
                    cell[x - 1][y] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y]!=' ':
                if cell[x-1][y].color!=K.color:
                    obj=cell[x-1][y]
                    cell[x-1][y]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x - 1, y) == 1:
                        cell[x-1][y]=obj
                        cell[x][y]=K
                    else:
                        cell[x - 1][y] = obj
                        cell[x][y] = K
                        return 0
        if y+1<=7:
            if cell[x][y+1]==' ':
                cell[x][y+1]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x, y+1)==1:
                    cell[x][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x][y+1]!=' ':
                if cell[x][y+1].color!=K.color:
                    obj=cell[x][y+1]
                    cell[x][y+1]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x, y+1) == 1:
                        cell[x][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x][y+1] = obj
                        cell[x][y] = K
                        return 0
        if y-1>=0:
            if cell[x][y-1]==' ':
                cell[x][y-1]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x, y-1)==1:
                    cell[x][y-1]=' '
                    cell[x][y]=K
                else:
                    cell[x][y-1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x][y-1]!=' ':
                if cell[x][y-1].color!=K.color:
                    obj=cell[x][y-1]
                    cell[x][y-1]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x, y-1) == 1:
                        cell[x][y-1]=obj
                        cell[x][y]=K
                    else:
                        cell[x][y-1] = obj
                        cell[x][y] = K
                        return 0
        if y+1<=7 and x+1<=7:
            if cell[x+1][y+1]==' ':
                cell[x+1][y+1]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x+1, y+1)==1:
                    cell[x+1][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x+1][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x+1][y+1]!=' ':
                if cell[x+1][y+1].color!=K.color:
                    obj=cell[x+1][y+1]
                    cell[x+1][y+1]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x+1, y+1) == 1:
                        cell[x+1][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x+1][y+1] = obj
                        cell[x][y] = K
                        return 0

        if y - 1 >=0 and x + 1 <= 7:
            if cell[x + 1][y - 1] == ' ':
                cell[x + 1][y - 1] = K
                cell[x][y] = ' '
                if king_w.check(cell, pix, x + 1, y - 1) == 1:
                    cell[x + 1][y - 1] = ' '
                    cell[x][y] = K
                else:
                    cell[x + 1][y - 1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x + 1][y - 1] != ' ':
                if cell[x + 1][y - 1].color != K.color:
                    obj = cell[x + 1][y - 1]
                    cell[x + 1][y - 1] = K
                    cell[x][y] = ' '
                    if king_w.check(cell, pix, x + 1, y - 1) == 1:
                        cell[x + 1][y - 1] = obj
                        cell[x][y] = K
                    else:
                        cell[x + 1][y - 1] = obj
                        cell[x][y] = K
                        return 0


        if y+1<=7 and x-1>=0:
            if cell[x-1][y+1]==' ':
                cell[x-1][y+1]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x-1, y+1)==1:
                    cell[x-1][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x-1][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y+1]!=' ':
                if cell[x-1][y+1].color!=K.color:
                    obj=cell[x-1][y+1]
                    cell[x-1][y+1]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x-1, y+1) == 1:
                        cell[x-1][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x-1][y+1] = obj
                        cell[x][y] = K
                        return 0
        if y-1>=0 and x-1>=0:
            if cell[x-1][y-1]==' ':
                cell[x-1][y-1]=K
                cell[x][y]=' '
                if king_w.check(cell, pix, x-1, y-1)==1:
                    cell[x-1][y-1]=' '
                    cell[x][y]=K
                else:
                    cell[x-1][y-1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y-1]!=' ':
                if cell[x-1][y-1].color!=K.color:
                    obj=cell[x-1][y-1]
                    cell[x-1][y-1]=K
                    cell[x][y]=' '
                    if king_w.check(cell, pix, x-1, y-1) == 1:
                        cell[x-1][y-1]=obj
                        cell[x][y]=K
                    else:
                        cell[x-1][y-1] = obj
                        cell[x][y] = K
                        return 0
    return 1
def checking_king_b():
    pix=central_pixel
    K=king_b
    if K== king_b:
        x=K.cell_x
        y=K.cell_y

        if x+1<=7:
            if cell[x+1][y]==' ':
                cell[x+1][y]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x+1, y)==1:
                    cell[x+1][y]=' '
                    cell[x][y]=K
                else:
                    cell[x + 1][y] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x+1][y]!=' ':
                if cell[x+1][y].color!=K.color:
                    obj=cell[x+1][y]
                    cell[x+1][y]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x + 1, y) == 1:
                        cell[x+1][y]=obj
                        cell[x][y]=K
                    else:
                        cell[x + 1][y] = obj
                        cell[x][y] = K
                        return 0
        if x-1>=0:
            if cell[x-1][y]==' ':
                cell[x-1][y]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x-1, y)==1:
                    cell[x-1][y]=' '
                    cell[x][y]=K
                else:
                    cell[x - 1][y] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y]!=' ':
                if cell[x-1][y].color!=K.color:
                    obj=cell[x-1][y]
                    cell[x-1][y]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x - 1, y) == 1:
                        cell[x-1][y]=obj
                        cell[x][y]=K
                    else:
                        cell[x - 1][y] = obj
                        cell[x][y] = K
                        return 0
        if y+1<=7:
            if cell[x][y+1]==' ':
                cell[x][y+1]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x, y+1)==1:
                    cell[x][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x][y+1]!=' ':
                if cell[x][y+1].color!=K.color:
                    obj=cell[x][y+1]
                    cell[x][y+1]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x, y+1) == 1:
                        cell[x][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x][y+1] = obj
                        cell[x][y] = K
                        return 0
        if y-1>=0:
            if cell[x][y-1]==' ':
                cell[x][y-1]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x, y-1)==1:
                    cell[x][y-1]=' '
                    cell[x][y]=K
                else:
                    cell[x][y-1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x][y-1]!=' ':
                if cell[x][y-1].color!=K.color:
                    obj=cell[x][y-1]
                    cell[x][y-1]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x, y-1) == 1:
                        cell[x][y-1]=obj
                        cell[x][y]=K
                    else:
                        cell[x][y-1] = obj
                        cell[x][y] = K
                        return 0
        if y+1<=7 and x+1<=7:
            if cell[x+1][y+1]==' ':
                cell[x+1][y+1]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x+1, y+1)==1:
                    cell[x+1][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x+1][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x+1][y+1]!=' ':
                if cell[x+1][y+1].color!=K.color:
                    obj=cell[x+1][y+1]
                    cell[x+1][y+1]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x+1, y+1) == 1:
                        cell[x+1][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x+1][y+1] = obj
                        cell[x][y] = K
                        return 0

        if y - 1 >=0 and x + 1 <= 7:
            if cell[x + 1][y - 1] == ' ':
                cell[x + 1][y - 1] = K
                cell[x][y] = ' '
                if king_b.check(cell, pix, x + 1, y - 1) == 1:
                    cell[x + 1][y - 1] = ' '
                    cell[x][y] = K
                else:
                    cell[x + 1][y - 1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x + 1][y - 1] != ' ':
                if cell[x + 1][y - 1].color != K.color:
                    obj = cell[x + 1][y - 1]
                    cell[x + 1][y - 1] = K
                    cell[x][y] = ' '
                    if king_b.check(cell, pix, x + 1, y - 1) == 1:
                        cell[x + 1][y - 1] = obj
                        cell[x][y] = K
                    else:
                        cell[x + 1][y - 1] = obj
                        cell[x][y] = K
                        return 0


        if y+1<=7 and x-1>=0:
            if cell[x-1][y+1]==' ':
                cell[x-1][y+1]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x-1, y+1)==1:
                    cell[x-1][y+1]=' '
                    cell[x][y]=K
                else:
                    cell[x-1][y+1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y+1]!=' ':
                if cell[x-1][y+1].color!=K.color:
                    obj=cell[x-1][y+1]
                    cell[x-1][y+1]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x-1, y+1) == 1:
                        cell[x-1][y+1]=obj
                        cell[x][y]=K
                    else:
                        cell[x-1][y+1] = obj
                        cell[x][y] = K
                        return 0
        if y-1>=0 and x-1>=0:
            if cell[x-1][y-1]==' ':
                cell[x-1][y-1]=K
                cell[x][y]=' '
                if king_b.check(cell, pix, x-1, y-1)==1:
                    cell[x-1][y-1]=' '
                    cell[x][y]=K
                else:
                    cell[x-1][y-1] = ' '
                    cell[x][y] = K
                    return 0
            elif cell[x-1][y-1]!=' ':
                if cell[x-1][y-1].color!=K.color:
                    obj=cell[x-1][y-1]
                    cell[x-1][y-1]=K
                    cell[x][y]=' '
                    if king_b.check(cell, pix, x-1, y-1) == 1:
                        cell[x-1][y-1]=obj
                        cell[x][y]=K
                    else:
                        cell[x-1][y-1] = obj
                        cell[x][y] = K
                        return 0
    return 1


def check_mate_w():

    val = checking_queen_w()
    print(val)
    if val == 0:
        return 0
    val=checking_pawn_w()
    print(val)
    if val==0:
        return 0
    val=checking_rook_w()
    print(val)
    if val==0:
        return 0
    val = checking_bishop_w()
    print(val)
    if val == 0:
        return 0
    val = checking_knight_w()
    print(val)
    if val == 0:
        return 0
    val = checking_king_w()
    print(val)
    if val == 0:
        return 0

    return 1

def check_mate_b():
    val = checking_knight_b()
    print(val)
    if val == 0:
        return 0
    val = checking_queen_b()
    print(val)
    if val == 0:
        return 0
    val=checking_pawn_b()
    print(val)
    if val==0:
        return 0
    val=checking_rook_b()
    print(val)
    if val==0:
        return 0
    val = checking_bishop_b()
    print(val)
    if val == 0:
        return 0
    val = checking_king_b()
    print(val)
    if val == 0:
        return 0

    return 1






class King:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x=cell_x
        self.cell_y=cell_y
        self.color = color

    def show_white(self, screen):
        screen.blit(KING_W, (self.x, self.y))

    def show_black(self, screen):
        screen.blit(KING_B, (self.x, self.y))

    def move(self, cell, pixel,kings):
        Y = self.cell_y
        X = self.cell_x
        k=1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = calc_cell(pixel)
                    if cell[x][y] == ' ' or cell[x][y].color != self.color:
                        
                        if (x, y) in [(self.cell_x, self.cell_y-1), (self.cell_x, self.cell_y+1),
                                      (self.cell_x-1, self.cell_y), (self.cell_x+1, self.cell_y),
                                    (self.cell_x-1, self.cell_y-1), (self.cell_x-1, self.cell_y+1),
                                    (self.cell_x+1, self.cell_y+1), (self.cell_x+1, self.cell_y-1)]:
                            if cell[x][y] == ' ':
                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32

                                cell[x][y] = self

                                if self.cover(cell, pixel, kings, X, Y) == 1:
                                    print('You cant move')
                                    return 1

                                else:
                                    mixer.Sound.play(MOVE)
                                    return 0
                            elif cell[x][y].color != self.color:
                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32
                                obj = cell[x][y]
                                obj.x = 1500
                                obj.y = 1500
                                cell[x][y] = self
                                if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                    return 1
                                mixer.Sound.play(MOVE)
                                return 0
                        else:
                            return 1
                    else:
                        return 1

    def cover(self, cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:

                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x = X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x = self.cell_x
                    obj.cell_y = self.cell_y
                    obj.x = pixel[self.cell_y] - 32
                    obj.y = pixel[self.cell_x] - 32
                    self.cell_x = X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1


    def check(self, cell, pixel, cell_x, cell_y):
        check_value=0
        
        

        #diagoanal attack
        for i in range(1,8):
            if cell_x + i <= 7 and cell_y + i <= 7:
                if cell[cell_x+i][cell_y+i] != ' ' and cell[cell_x+i][cell_y+i].color != self.color:
                    if cell[cell_x+1][cell_y+1] in pawn_w :

                        check_value = 1
                        return check_value
                    if cell[cell_x+i][cell_y+i] in [queen_w, queen_b]:
                        check_value=1
                        return  check_value
                    if cell[cell_x+i][cell_y+i] in bishop_w or cell[cell_x+i][cell_y+i] in bishop_b:
                        check_value=1
                        return  check_value
                    if cell[cell_x + 1][cell_y + 1] == king_w or cell[cell_x + 1][cell_y + 1] == king_b:
                        check_value = 1
                        return check_value
                    else:
                        break
                if cell[cell_x + i][cell_y + i] != ' ' and cell[cell_x + i][cell_y + i].color == self.color:
                    break

        for i in range(1,8):
            if cell_x-i>=0 and cell_y-i>=0:
                if cell[cell_x-i][cell_y-i] != ' ' and cell[cell_x-i][cell_y-i].color != self.color:
                    if  cell[cell_x - 1][cell_y - 1] in pawn_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y - i] in [queen_w, queen_b]:

                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y - i] in bishop_w or  cell[cell_x - i][cell_y - i] in bishop_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x - 1][cell_y - 1] == king_w or cell[cell_x - 1][cell_y - 1] == king_b:
                        check_value = 1
                        return check_value
                    else:
                        break
                elif cell[cell_x-i][cell_y-i] != ' ' and cell[cell_x-i][cell_y-i].color == self.color:

                    break

        for i in range(1,8):
            if cell_x-i>=0 and cell_y+i <= 7:
                if cell[cell_x-i][cell_y+i] != ' ' and cell[cell_x-i][cell_y+i].color != self.color:
                    if  cell[cell_x - 1][cell_y + 1] in pawn_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y +i] in [queen_w,queen_b]:
                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y + i] in bishop_w or cell[cell_x - i][cell_y + i] in  bishop_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x - 1][cell_y + 1] == king_w or cell[cell_x - 1][cell_y + 1] == king_b:
                        check_value = 1
                        return check_value
                    else:
                        break
                if cell[cell_x - i][cell_y + i] != ' ' and cell[cell_x - i][cell_y + i].color == self.color:
                    break
        for i in range(1,8):
            if cell_x+i <= 7 and cell_y-i >= 0:
                if cell[cell_x+i][cell_y-i] != ' ' and cell[cell_x+i][cell_y-i].color != self.color:
                    if cell[cell_x + 1][cell_y - 1] in pawn_w :
                        check_value = 1
                        return check_value
                    if cell[cell_x + i][cell_y - i] in [queen_w ,queen_b]:
                        check_value = 1
                        return check_value
                    if cell[cell_x + i][cell_y - i] in bishop_w or cell[cell_x + i][cell_y - i] in  bishop_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x + 1][cell_y - 1] == king_w or cell[cell_x + 1][cell_y - 1] == king_b:
                        check_value = 1
                        return check_value
                    else:
                        break
                if cell[cell_x + i][cell_y - i] != ' ' and cell[cell_x + i][cell_y - i].color == self.color:
                    break


        #vertical or horizontal attack
        for i in range(1,8):
            if cell_x+i < 8:
                if cell[cell_x + i][cell_y] != ' ' and cell[cell_x + i][cell_y].color != self.color:
                    if cell[cell_x + 1][cell_y] == king_w or cell[cell_x + 1][cell_y] == king_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x + i][cell_y] == queen_b or cell[cell_x + i][cell_y] == queen_w:
                        check_value = 1
                        return check_value
                    if cell[cell_x + i][cell_y] in rook_b or cell[cell_x + i][cell_y]  in rook_w:
                        check_value=1
                        return check_value
                    else:
                        break

                if cell[cell_x + i][cell_y] != ' ' and cell[cell_x + i][cell_y].color == self.color:
                    break

        for i in range(1,8):
            if cell_x-i>=0:
                if cell[cell_x - i][cell_y] != ' ' and cell[cell_x - i][cell_y].color != self.color:
                    if cell[cell_x - 1][cell_y] == king_w or cell[cell_x - 1][cell_y] == king_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y] == queen_b or cell[cell_x - i][cell_y] == queen_w:
                        check_value = 1
                        return check_value
                    if cell[cell_x - i][cell_y] in rook_b or cell[cell_x - i][cell_y] in rook_w:
                        check_value=1
                        return check_value
                    else:
                        break
                if cell[cell_x - i][cell_y] != ' ' and cell[cell_x - i][cell_y].color == self.color:
                    break

        for i in range(1,8):
            if cell_y+i < 8:
                if cell[cell_x][cell_y+i] != ' ' and cell[cell_x][cell_y+i].color != self.color:
                    if cell[cell_x][cell_y+1] == king_w or cell[cell_x][cell_y+1] == king_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x][cell_y+i] == queen_b or cell[cell_x][cell_y+i] == queen_w:
                        check_value = 1
                        return check_value
                    if cell[cell_x][cell_y+i] in rook_b or cell[cell_x][cell_y+i] in rook_w:
                        check_value=1
                        return check_value
                    else:
                        break
                if cell[cell_x][cell_y + i] != ' ' and cell[cell_x][cell_y + i].color == self.color:
                    break

        for i in range(1,8):
            if cell_y-i >= 0:
                if cell[cell_x][cell_y-i] != ' ' and cell[cell_x][cell_y-i].color != self.color:
                    if cell[cell_x][cell_y - 1] == king_w or cell[cell_x][cell_y - 1] == king_b:
                        check_value = 1
                        return check_value
                    if cell[cell_x][cell_y - i] == queen_b or cell[cell_x][cell_y - i] == queen_w:
                        check_value = 1
                        return check_value
                    if cell[cell_x][cell_y - i] in rook_b or cell[cell_x][cell_y - i] in rook_w:
                        check_value = 1
                        return check_value
                    else:
                        break
                if cell[cell_x][cell_y - i] != ' ' and cell[cell_x][cell_y - i].color == self.color:
                    break

        #horse attack
        k=cell_x
        l=cell_y

        if k-2>=0 and l-1>=0:

            if cell[k-2][l-1] in knight_w or cell[k-2][l-1] in knight_b:
                if self.color!=cell[k-2][l-1].color:
                    check_value=1
                    return check_value

        if k - 2 >= 0 and l + 1 < 8:

            if cell[k - 2][l + 1] in knight_w or cell[k - 2][l + 1] in knight_b:
                if self.color != cell[k - 2][l + 1].color:
                    check_value = 1
                    return check_value
        if k + 2 < 8 and l - 1 >= 0:

            if cell[k + 2][l - 1] in knight_w or cell[k + 2][l - 1] in knight_b:
                if self.color != cell[k + 2][l - 1].color:
                    check_value = 1
                    return check_value

        if k + 2 < 8 and l + 1 < 8:

            if cell[k + 2][l + 1] in knight_w or cell[k + 2][l + 1] in knight_b:
                if self.color != cell[k + 2][l + 1].color:
                    check_value = 1
                    return check_value

        if k - 1 >= 0 and l + 2 < 8:

            if cell[k - 1][l + 2] in knight_w or cell[k - 1][l + 2] in knight_b:
                if self.color != cell[k - 1][l + 2].color:
                    check_value = 1
                    return check_value

        if k - 1 >= 0 and l - 2 >=0:

            if cell[k - 1][l - 2] in knight_w or cell[k - 1][l - 2] in knight_b:
                if self.color != cell[k - 1][l - 2].color:
                    check_value = 1
                    return check_value
        if k + 1 < 8 and l + 2 < 8:

            if cell[k + 1][l + 2] in knight_w or cell[k + 1][l + 2] in knight_b:
                if self.color != cell[k + 1][l + 2].color:
                    check_value = 1
                    return check_value
        if k + 1 <8 and l - 2 >=0:

            if cell[k + 1][l - 2] in knight_w or cell[k + 1][l - 2] in knight_b:
                if self.color != cell[k + 1][l - 2].color:
                    check_value = 1
                    return check_value

        return check_value


class Pawn:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.move_no=1
        self.color=color


    def show_white(self, screen):
        screen.blit(PAWN_W, (self.x, self.y))

    def show_black(self, screen):
        screen.blit(PAWN_B, (self.x, self.y))

    def move(self, cell, pixel, kings):
        Y = self.cell_y
        X = self.cell_x
        k = 1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    (x, y) = calc_cell(pixel)
                    if cell[x][y] == ' ':

                        


                        if self.color == 'b':
                            if self.move_no ==1:
                                if (x, y) in [(self.cell_x + 1, self.cell_y)]:
                                    cell[self.cell_x][self.cell_y] = ' '
                                    self.cell_y = y
                                    self.cell_x = x
                                    self.y = pixel[x] - 32
                                    self.x = pixel[y] - 32

                                    cell[x][y] = self
                                    if self.cover(cell, pixel, kings, X, Y) == 1:
                                        print('You cant move')
                                        return 1

                                    else:
                                        mixer.Sound.play(MOVE)
                                        self.move_no += 1
                                        return 0

                                elif (x, y) in [(self.cell_x + 2, self.cell_y)]:
                                    if cell[self.cell_x+1][self.cell_y] == ' ':
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32

                                        cell[x][y] = self
                                        if self.cover(cell, pixel, kings, X, Y) == 1:
                                            print('You cant move')
                                            return 1

                                        else:
                                            mixer.Sound.play(MOVE)
                                            self.move_no += 1
                                            return 0
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if (x, y) == (self.cell_x + 1, self.cell_y):
                                    cell[self.cell_x][self.cell_y] = ' '
                                    self.cell_y = y
                                    self.cell_x = x
                                    self.y = pixel[x] - 32
                                    self.x = pixel[y] - 32

                                    cell[x][y] = self
                                    if self.cover(cell, pixel, kings, X, Y) == 1:
                                        print('You cant move')
                                        return 1

                                    else:
                                        mixer.Sound.play(MOVE)
                                        return 0
                                else:
                                    return 1
                        elif self.color=='w':

                            if self.move_no == 1:
                                if (x, y) in [(self.cell_x - 1, self.cell_y)]:
                                    cell[self.cell_x][self.cell_y] = ' '
                                    self.cell_y = y
                                    self.cell_x = x
                                    self.y = pixel[x] - 32
                                    self.x = pixel[y] - 32

                                    cell[x][y] = self
                                    if self.cover(cell, pixel, kings, X, Y) == 1:
                                        print('You cant move')
                                        return 1

                                    else:
                                        mixer.Sound.play(MOVE)
                                        self.move_no += 1
                                        return 0
                                elif (x, y) in [(self.cell_x - 2, self.cell_y)]:
                                    if cell[self.cell_x - 1][self.cell_y] == ' ':
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32

                                        cell[x][y] = self
                                        if self.cover(cell, pixel, kings, X, Y) == 1:
                                            print('You cant move')
                                            return 1

                                        else:
                                            mixer.Sound.play(MOVE)
                                            self.move_no += 1
                                            return 0
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if (x, y) == (self.cell_x - 1, self.cell_y):
                                    cell[self.cell_x][self.cell_y] = ' '
                                    self.cell_y = y
                                    self.cell_x = x
                                    self.y = pixel[x] - 32
                                    self.x = pixel[y] - 32

                                    cell[x][y] = self
                                    if self.cover(cell, pixel, kings, X, Y) == 1:
                                        print('You cant move')
                                        return 1

                                    else:
                                        mixer.Sound.play(MOVE)
                                        return 0
                                else:
                                    return 1

                    elif self.color != cell[x][y].color:
                        if self.color == 'b':
                            if (x,y) in [(self.cell_x + 1, self.cell_y-1), (self.cell_x + 1, self.cell_y + 1)]:
                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32
                                obj = cell[x][y]
                                obj.x = 1500
                                obj.y = 1500
                                cell[x][y] = self
                                if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                    return 1
                                mixer.Sound.play(MOVE)
                                return 0
                            else:
                                return 1
                        elif self.color == 'w':
                            if (x, y) in [(self.cell_x -1, self.cell_y +1), (self.cell_x - 1, self.cell_y - 1)]:
                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32
                                obj = cell[x][y]
                                obj.x = 1500
                                obj.y = 1500
                                cell[x][y] = self
                                if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                    return 1
                                mixer.Sound.play(MOVE)
                                return 0
                            else:
                                return 1
                    else:
                        return 1
    def cover(self,cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:
                
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x=X
                    self.cell_y=Y
                    self.y= pixel[X]-32
                    self.x = pixel[Y]-32
                    cell[X][Y]=self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x=self.cell_x
                    obj.cell_y=self.cell_y
                    obj.x=pixel[self.cell_y]-32
                    obj.y=pixel[self.cell_x]-32
                    self.cell_x=X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1




class Queen:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.color = color

    def show_white(self, screen):
        screen.blit(QUEEN_W, (self.x, self.y))

    def show_black(self, screen):
        screen.blit(QUEEN_B, (self.x, self.y))

    def move(self, cell, pixel,kings):
        Y = self.cell_y
        X = self.cell_x
        k=1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    (x, y)=calc_cell(pixel)
                    if cell[x][y] == ' ' or cell[x][y].color != self.color:
                        
                        

                        for n in range(1,8):
                            if (x, y) in [(self.cell_x, self.cell_y + n), (self.cell_x, self.cell_y - n),
                                          (self.cell_x + n, self.cell_y), (self.cell_x - n, self.cell_y),
                                          (self.cell_x - n, self.cell_y - n), (self.cell_x + n, self.cell_y + n),
                                          (self.cell_x + n, self.cell_y - n), (self.cell_x - n, self.cell_y + n)]:

                                diff_x= x - self.cell_x
                                diff_y = y - self.cell_y
                                flag = 0
                                for i in range(1, abs(diff_x)):
                                    if diff_x>0 and diff_y==0:
                                        if cell[self.cell_x+i][self.cell_y] != ' ':
                                            flag=1
                                            break
                                    if diff_x >0 and diff_y>0:
                                        if cell[self.cell_x + i][self.cell_y + i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x < 0 and diff_y == 0:
                                        if cell[self.cell_x - i][self.cell_y] != ' ':
                                            flag = 1
                                            break
                                    if diff_x < 0 and diff_y < 0:
                                        if cell[self.cell_x - i][self.cell_y - i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x ==0 and diff_y > 0:
                                        if cell[self.cell_x][self.cell_y + i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x == 0 and diff_y < 0:
                                        if cell[self.cell_x][self.cell_y - i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x > 0 and diff_y < 0:
                                        if cell[self.cell_x + i][self.cell_y - i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x < 0 and diff_y > 0:
                                        if cell[self.cell_x - i][self.cell_y + i] != ' ':
                                            flag = 1
                                            break

                                if flag==1:
                                    return 1
                                else:
                                    if cell[x][y]==' ':
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32

                                        cell[x][y] = self

                                        if self.cover(cell, pixel, kings, X, Y) == 1:
                                            print('You cant move')
                                            return 1

                                        else:
                                            mixer.Sound.play(MOVE)
                                            return 0
                                    elif cell[x][y].color != self.color:
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32
                                        obj=cell[x][y]
                                        obj.x=1500
                                        obj.y=1500
                                        cell[x][y] = self
                                        if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                            return 1
                                        mixer.Sound.play(MOVE)
                                        return 0






                    else:
                        return 1
    def cover(self,cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:
                
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x=X
                    self.cell_y=Y
                    self.y= pixel[X]-32
                    self.x = pixel[Y]-32
                    cell[X][Y]=self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x=self.cell_x
                    obj.cell_y=self.cell_y
                    obj.x=pixel[self.cell_y]-32
                    obj.y=pixel[self.cell_x]-32
                    self.cell_x=X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1


class Bishop:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.color = color

    def show_white(self, screen):
        screen.blit(BISHOP_W, (self.x, self.y))


    def show_black(self, screen):
        screen.blit(BISHOP_B, (self.x, self.y))

    def move(self, cell, pixel, kings):
        Y = self.cell_y
        X = self.cell_x
        k=1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    (x, y)=calc_cell(pixel)
                    if cell[x][y] == ' ' or cell[x][y].color != self.color:
                        
                        

                        for n in range(1,8):
                            if (x, y) in [(self.cell_x - n, self.cell_y - n), (self.cell_x + n, self.cell_y + n),
                                          (self.cell_x + n, self.cell_y - n), (self.cell_x - n, self.cell_y + n)]:
                                diff_x = x - self.cell_x
                                diff_y = y - self.cell_y
                                flag = 0

                                for i in range(1, abs(diff_x)):

                                    if diff_x >0 and diff_y>0:
                                        if cell[self.cell_x + i][self.cell_y + i] != ' ':
                                            flag = 1
                                            break

                                    if diff_x < 0 and diff_y < 0:
                                        if cell[self.cell_x - i][self.cell_y - i] != ' ':
                                            flag = 1
                                            break


                                    if diff_x > 0 and diff_y < 0:
                                        if cell[self.cell_x + i][self.cell_y - i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x < 0 and diff_y > 0:
                                        if cell[self.cell_x - i][self.cell_y + i] != ' ':
                                            flag = 1
                                            break

                                if flag==1:
                                    return 1
                                else:
                                    if cell[x][y] == ' ':
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32
                                        cell[x][y] = self

                                        if self.cover(cell, pixel, kings, X, Y) == 1:
                                            print('You cant move')
                                            return 1

                                        else:
                                            mixer.Sound.play(MOVE)
                                            return 0

                                    elif cell[x][y].color != self.color:
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32
                                        obj = cell[x][y]
                                        obj.x = 1500
                                        obj.y = 1500
                                        cell[x][y] = self
                                        if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                            return 1
                                        mixer.Sound.play(MOVE)
                                        return 0
                    else:
                        return 1
    def cover(self,cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:
                
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x=X
                    self.cell_y=Y
                    self.y= pixel[X]-32
                    self.x = pixel[Y]-32
                    cell[X][Y]=self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x=self.cell_x
                    obj.cell_y=self.cell_y
                    obj.x=pixel[self.cell_y]-32
                    obj.y=pixel[self.cell_x]-32
                    self.cell_x=X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1





class Rook:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.color = color

    def show_black(self, screen):
        screen.blit(ROOK_B, (self.x, self.y))

    def show_white(self, screen):
        screen.blit(ROOK_W, (self.x, self.y))

    def move(self, cell, pixel, kings):
        Y = self.cell_y
        X = self.cell_x
        k=1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    (x, y)=calc_cell(pixel)
                    if cell[x][y] == ' ' or cell[x][y].color != self.color:
                        
                        


                        for n in range(1,8):
                            if (x, y) in [(self.cell_x, self.cell_y + n), (self.cell_x, self.cell_y - n),
                                          (self.cell_x + n, self.cell_y), (self.cell_x - n, self.cell_y)]:
                                
                                diff_x= x - self.cell_x
                                diff_y = y - self.cell_y
                                flag = 0
                                for i in range(1, abs(diff_x)):
                                    if diff_x>0 and diff_y==0:
                                        if cell[self.cell_x+i][self.cell_y] != ' ':
                                            flag=1
                                            break

                                    if diff_x < 0 and diff_y == 0:
                                        if cell[self.cell_x - i][self.cell_y] != ' ':
                                            flag = 1
                                            break

                                    if diff_x ==0 and diff_y > 0:
                                        if cell[self.cell_x][self.cell_y + i] != ' ':
                                            flag = 1
                                            break
                                    if diff_x == 0 and diff_y < 0:
                                        if cell[self.cell_x][self.cell_y - i] != ' ':
                                            flag = 1
                                            break

                                if flag == 1:
                                    return 1
                                else:
                                    if cell[x][y] == ' ':
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32
                                        cell[x][y] = self
                                        if self.cover(cell, pixel, kings, X, Y) == 1:
                                            print('You cant move')
                                            return 1

                                        else:
                                            mixer.Sound.play(MOVE)
                                            return 0


                                    elif cell[x][y].color != self.color:
                                        cell[self.cell_x][self.cell_y] = ' '
                                        self.cell_y = y
                                        self.cell_x = x
                                        self.y = pixel[x] - 32
                                        self.x = pixel[y] - 32
                                        obj = cell[x][y]
                                        obj.x = 1500
                                        obj.y = 1500
                                        cell[x][y] = self
                                        if self.cover2(cell, pixel, kings, X, Y, obj) == 1:
                                            return 1
                                        mixer.Sound.play(MOVE)
                                        return 0

                    else:
                        return 1
    def cover(self,cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:
                
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x=X
                    self.cell_y=Y
                    self.y= pixel[X]-32
                    self.x = pixel[Y]-32
                    cell[X][Y]=self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x=self.cell_x
                    obj.cell_y=self.cell_y
                    obj.x=pixel[self.cell_y]-32
                    obj.y=pixel[self.cell_x]-32
                    self.cell_x=X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1


class Knight:
    def __init__(self, x, y, cell_x, cell_y, color):
        self.x = x
        self.y = y
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.color = color

    def show_white(self, screen):
        screen.blit(KNIGHT_W, (self.x, self.y))

    def show_black(self, screen):
        screen.blit(KNIGHT_B, (self.x, self.y))

    def move(self, cell, pixel, kings):
        Y=self.cell_y
        X=self.cell_x
        k=1
        while k:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    (x, y)=calc_cell(pixel)
                    if cell[x][y] == ' ' or cell[x][y].color != self.color:
                        
                        

                        if (x, y) in [(self.cell_x - 1, self.cell_y - 2), (self.cell_x - 1, self.cell_y + 2),
                                    (self.cell_x + 1, self.cell_y - 2), (self.cell_x + 1, self.cell_y + 2),
                                    (self.cell_x + 2, self.cell_y - 1), (self.cell_x + 2, self.cell_y + 1),
                                    (self.cell_x - 2, self.cell_y - 1), (self.cell_x - 2, self.cell_y + 1)]:
                            if cell[x][y] == ' ':

                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32
                                cell[x][y] = self

                                
                                if self.cover(cell, pixel, kings, X, Y)==1:
                                    print('You cant move')
                                    return 1

                                else:
                                    mixer.Sound.play(MOVE)
                                    return 0

                            elif cell[x][y].color != self.color and cell[x][y] not in kings:
                                cell[self.cell_x][self.cell_y] = ' '
                                self.cell_y = y
                                self.cell_x = x
                                self.y = pixel[x] - 32
                                self.x = pixel[y] - 32
                                obj = cell[x][y]
                                obj.x = 1500
                                obj.y = 1500
                                cell[x][y] = self
                                if self.cover2(cell, pixel, kings, X, Y, obj)==1:
                                    return 1
                                mixer.Sound.play(MOVE)
                                return 0
                        else:
                            return 1
                    else:
                        return 1



    def cover(self,cell, pixel, kings, X, Y):
        for kg in kings:
            if kg.color == self.color:
                
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = ' '
                    self.cell_x=X
                    self.cell_y=Y
                    self.y= pixel[X]-32
                    self.x = pixel[Y]-32
                    cell[X][Y]=self
                    return 1

    def cover2(self, cell, pixel, kings, X, Y, obj):
        for kg in kings:
            if kg.color == self.color:
                if kg.check(cell, pixel, kg.cell_x, kg.cell_y) != 0:
                    cell[self.cell_x][self.cell_y] = obj
                    obj.cell_x=self.cell_x
                    obj.cell_y=self.cell_y
                    obj.x=pixel[self.cell_y]-32
                    obj.y=pixel[self.cell_x]-32
                    self.cell_x=X
                    self.cell_y = Y
                    self.y = pixel[X] - 32
                    self.x = pixel[Y] - 32
                    cell[X][Y] = self
                    return 1





class Textbox:
    def __init__(self, color, x, y, length, breadth, text, txt_color):
        self.color=color
        self.x=x
        self.y=y
        self.l=length
        self.b=breadth
        self.txt=text
        self.txt_c=txt_color

    def act_box(self, screen, posx, posy):
        if posx > self.x and posx < (self.x + self.l):
            if posy > self.y and posy < (self.y + self.b):
                    pg.draw.rect(screen, (0,0,0), (self.x, self.y, self.l, self.b), 0)
                    txt=Font2.render(self.txt, True, self.txt_c)
                    screen.blit(txt, (self.x + (self.l-txt.get_width())/2, self.y + (self.b-txt.get_height())/2))
                    return

        pg.draw.rect(screen, self.color, (self.x, self.y, self.l, self.b), 1)
        txt = Font2.render(self.txt, True, self.txt_c)
        screen.blit(txt, (self.x + (self.l - txt.get_width()) / 2, self.y + (self.b - txt.get_height()) / 2))

    def selection(self, posx,posy):
        if posx>self.x and posx<(self.x+self.l):
            if posy>self.y and posy<(self.y+self.b):

                return 1,self
        return 0,self



def draw_rectangle(screen):
    posx, posy =pg.mouse.get_pos()
    val=100000
    for i in range(8):
        for j in range (8):
            if math.sqrt(pow(central_pixel[i]-posx, 2) + pow(central_pixel[j]-posy, 2)) < val:
                val=math.sqrt(pow(central_pixel[i]-posx, 2) + pow(central_pixel[j]-posy, 2))
                cx=central_pixel[i]
                cy=central_pixel[j]
    pg.draw.rect(screen, (0, 0, 220), (cx - 35, cy - 35 , 75, 75), 5)





king_b = King(408, 84, 0, 4, 'b')
king_w = King(408, 652, 7, 4, 'w')
kings =[king_w, king_b]


queen_b = Queen(327, 84, 0, 3, 'b')
queen_w = Queen(327, 652, 7, 3, 'w')



rook_b=[]
rook_w=[]
rook_b.append(Rook(84, 84, 0, 0, 'b'))
rook_b.append(Rook(652, 84, 0, 7, 'b'))
rook_w.append(Rook(84, 652, 7, 0, 'w'))
rook_w.append(Rook(652, 652, 7, 7, 'w'))


bishop_w=[]
bishop_b=[]
bishop_b.append((Bishop(246, 84, 0, 2, 'b')))
bishop_b.append((Bishop(489, 84, 0, 5, 'b')))
bishop_w.append((Bishop(246, 651, 7, 2, 'w')))
bishop_w.append((Bishop(489, 651, 7, 5, 'w')))


knight_w = []
knight_b = []
knight_b.append((Knight(165, 84, 0, 1, 'b')))
knight_b.append((Knight(570, 84, 0, 6, 'b')))
knight_w.append((Knight(165, 651, 7, 1, 'w')))
knight_w.append((Knight(570, 651, 7, 6, 'w')))


pawn_w=[]
pawn_b=[]
coordx=84
coordy_b=165
coordy_w= 570
y_no=0

for i in range (8):
    pawn_w.append(Pawn(coordx, coordy_w, 6, y_no, 'w'))
    pawn_b.append((Pawn(coordx, coordy_b, 1, y_no, 'b')))
    coordx += 81
    y_no+=1

central_pixel = [115, 196, 277, 358, 439, 520, 601, 682]
cell = [[rook_b[0], knight_b[0], bishop_b[0], queen_b, king_b, bishop_b[1], knight_b[1], rook_b[1]],
        [pawn_b[0], pawn_b[1], pawn_b[2], pawn_b[3], pawn_b[4], pawn_b[5], pawn_b[6], pawn_b[7]],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [pawn_w[0], pawn_w[1], pawn_w[2], pawn_w[3], pawn_w[4], pawn_w[5], pawn_w[6], pawn_w[7]],
        [rook_w[0], knight_w[0], bishop_w[0], queen_w, king_w, bishop_w[1], knight_w[1], rook_w[1]]]



tb=Textbox((255, 255, 255), 550,300 , 200, 60, 'NEW GAME', (255, 0, 0))
qu=Textbox((255, 255, 255), 550,400 , 200, 60, 'QUIT', (255, 0, 0))


def show_index(screen):
  text= Font.render('CHESS24', True, (211,211,211))
  screen.blit(text, (530, 65))
  posx, posy= pg.mouse.get_pos()
  tb.act_box(screen,posx, posy)
  qu.act_box(screen, posx, posy)

def show_check(screen):
    if king_w.check(cell, central_pixel, king_w.cell_x, king_w.cell_y)==1:
        check_val = check_mate_w()
        if check_val == 1:
            mixer.Sound.play(CHECK_SOUND)
            text2 = Font2.render('CHECKMATE', True, (220, 0, 0))
            text3= Font2.render('BLACK WINS', True, (0, 0, 0))
            screen.blit(text2, (300, 360))
            screen.blit(text3, (280, 390))
        else:
            text=Font2.render('CHECK', True, (0, 0, 0))
            screen.blit(text, (0, 0))


    elif king_b.check(cell, central_pixel, king_b.cell_x, king_b.cell_y)==1:
        check_val = check_mate_b()
        if check_val == 1:
            mixer.Sound.play(CHECK_SOUND)
            text2 = Font2.render('CHECKMATE', True, (220, 0, 0))
            text3 = Font2.render('WHITE WINS', True, (0, 0, 0))
            screen.blit(text2, (300, 360))
            screen.blit(text3, (280, 390))
        else:
            text = Font2.render('CHECK', True, (255, 255, 255))
            screen.blit(text, (0, 0))






def main():
    screen = pg.display.set_mode((1280, 800))
    value=1
    pg.display.set_caption('Chess')
#    mixer.music.play(-1)

    index=1
    turn =1
    quiting=1
    while value:

        while index:
            screen.blit(IND_IMG, (0, 0))
            show_index(screen)


            for event in pg.event.get():
                if event.type==pg.MOUSEBUTTONDOWN:
                    for obj in [tb, qu]:

                        posx, posy=pg.mouse.get_pos()

                        num, obtype=obj.selection(posx, posy)
                        if obtype == tb and num==1:
                            mixer.music.stop()
                            index=0
                        elif obtype == qu and num==1:
                            index=0
                            value =0
                            quiting=0
                            break
                        else:
                            continue


                if event.type == pg.QUIT:
                    index=0
                    value=0
                    quiting=0
            pg.display.update()
        if quiting==0:
            break

        drawing_rect = 0



        #print(pg.mouse.get_pos())
        screen.blit(BG_IMG, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                value = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                flag=1


                while flag:
                    print(cell)
                    cell_x, cell_y = calc_cell(central_pixel)

                    if cell[cell_x][cell_y] != ' ' and turn % 2!=0:

                        obj = cell[cell_x][cell_y]
                        if obj.color=='w':
                            ret_value= obj.move(cell, central_pixel, kings)

                            if ret_value != 1:
                                turn+=1
                                flag=0
                                break
                            else:
                                break


                        elif obj.color=='b':
                            break

                    elif cell[cell_x][cell_y] != ' ' and turn % 2==0:
                        obj = cell[cell_x][cell_y]
                        if obj.color == 'b':
                            ret_value = obj.move(cell, central_pixel, kings)
                            if ret_value != 1:
                                turn += 1
                                flag = 0
                                break
                            else:
                                break

                        elif obj.color == 'w':
                            break

                    elif cell[cell_x][cell_y] == ' ':
                        break


        draw_rectangle(screen)
        show_check(screen)

        for i in range(8):
            pawn_w[i].show_white(screen)
            pawn_b[i].show_black(screen)



        for i in range(2):
            rook_b[i].show_black(screen)
            rook_w[i].show_white(screen)
            bishop_w[i].show_white(screen)
            bishop_b[i].show_black(screen)
            knight_b[i].show_black(screen)
            knight_w[i].show_white(screen)

        king_w.show_white(screen)
        king_b.show_black(screen)
        queen_w.show_white(screen)
        queen_b.show_black(screen)




        pg.display.update()

    pg.quit()

main()



#squre size -81
#total table size = 648=81*8
