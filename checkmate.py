from objects import pieces, isrival, isfree, dead

def checkmate(color, board):
    for i in range(8):
        for j in range(8):
            obj = board.cells[i][j].piece
            if obj != '' and obj.color == color:
                if obj.type == 'pawn':
                    if check_pawn(obj, color, board):
                        print('use ' + str(obj))
                        return False
                elif obj.type == 'bishop':
                    if check_bishop(obj, color, board):
                        print('use ' + str(obj))
                        return False
                elif obj.type == 'knight':
                    if check_knight(obj, color, board):
                        print('use ' + str(obj))
                        return False
                elif obj.type == 'rook':
                    if check_rook(obj, color, board):
                        print('use ' + str(obj))
                        return False
                elif obj.type == 'queen':
                    if check_queen(obj, color, board):
                        print('use ' + str(obj))
                        return False
                elif obj.type == 'king':
                    if check_king(obj, color, board):
                        print('use ' + str(obj))
                        return False
    return True

def check_pawn(obj, color, board):
    #TODO: not done 
    go_forw = True
    x, y = obj.pos[0], obj.pos[1]
    x_ = x
    y_ = y + obj.pawn_dir
    if y_ >= 0 and y_ < 8:
        if isfree(obj, (x_, y_), board):
            if shift_check(obj, (x_, y_), board):
                return True
        else:
            go_forw = False

    if go_forw:
        x_ = x
        y_ = y + 2 *  obj.pawn_dir
        if y_ >= 0 and y_ < 8:
            if isfree(obj, (x_, y_), board):
                if shift_check(obj, (x_, y_), board):
                    return True
    
    x_ = x - 1
    y_ = y + obj.pawn_dir
    if x_ >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
        if isrival(obj, (x_, y_), board):
            if shift_check(obj, (x_, y_), board):
                return True

    x_ = x + 1
    y_ = y + obj.pawn_dir
    if x_ >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
        if isrival(obj, (x_, y_), board):
            if shift_check(obj, (x_, y_), board):
                return True

    #en passant check
    if obj.pawn_dir == -1:
        if y == 3:
            x_ = x - 1
            if x_ >= 0 and x_ < 8:
                if check_en_passant(obj, x_, y, board):
                    return True

            x_ = x + 1
            if x_ >= 0 and x_ < 8:
                if check_en_passant(obj, x_, y, board):
                    return True
    else:
        if y == 4:
            x_ = x - 1
            if x_ >= 0 and x_ < 8:
                if check_en_passant(obj, x_, y, board):
                    return True

            x_ = x + 1
            if x_ >= 0 and x_ < 8:
                if check_en_passant(obj, x_, y, board):
                    return True

    return False





def check_en_passant(obj, x_, y, board):
    if not isfree(obj, (x_, y), board):
        obj_ = board.cells[x_][y].piece
        if obj_.type == 'pawn' and board.last_move['obj'] == obj_ and obj_.move_no == 1:
            board.cells[x_][y].piece = ''
            obj_.alive = False
            dead.append(obj_)

            ret_val = False
            if shift_check(obj, (x_, y), board):
                ret_val = True

            board.cells[x_][y_].piece = obj_
            obj_.alive = True
            dead.pop()

            return ret_val

    return False
                
    



def check_bishop(obj, color, board):
    if traverse(obj, board, 1, -1):
        return True
    if traverse(obj, board, -1, 1):
        return True
    if traverse(obj, board, 1, 1):
        return True
    if traverse(obj, board, -1, -1):
        return True
    return False

def check_knight(obj, color, board):
    if traverse_kn_kg(obj, board, 1, 2):
        return True
    if traverse_kn_kg(obj, board, 1, -2):
        return True
    if traverse_kn_kg(obj, board, -1, 2):
        return True
    if traverse_kn_kg(obj, board, -1, -2):
        return True
    if traverse_kn_kg(obj, board, 2, 1):
        return True
    if traverse_kn_kg(obj, board, 2, -1):
        return True
    if traverse_kn_kg(obj, board, -2, 1):
        return True
    if traverse_kn_kg(obj, board, -2, -1):
        return True

    
def check_rook(obj, color, board):
    if traverse(obj, board, 1, 0):
        return True
    if traverse(obj, board, 0, 1):
        return True
    if traverse(obj, board, -1, 0):
        return True
    if traverse(obj, board, 0, -1):
        return True
    return False

    
def check_queen(obj, color, board):
    if traverse(obj, board, 1, 0):
        return True
    if traverse(obj, board, 0, 1):
        return True
    if traverse(obj, board, -1, 0):
        return True
    if traverse(obj, board, 0, -1):
        return True
    if traverse(obj, board, 1, -1):
        return True
    if traverse(obj, board, -1, 1):
        return True
    if traverse(obj, board, 1, 1):
        return True
    if traverse(obj, board, -1, -1):
        return True
    return False

def check_king(obj, color, board):
    if traverse_kn_kg(obj, board, 1, 0):
        return True
    if traverse_kn_kg(obj, board, 0, 1):
        return True
    if traverse_kn_kg(obj, board, -1, 0):
        return True
    if traverse_kn_kg(obj, board, 0, -1):
        return True
    if traverse_kn_kg(obj, board, 1, 1):
        return True
    if traverse_kn_kg(obj, board, 1, -1):
        return True
    if traverse_kn_kg(obj, board, -1, 1):
        return True
    if traverse_kn_kg(obj, board, -1, -1):
        return True

def traverse_pawn(obj, board, x, y):
    pass    

#for rook, bishop, queen
def traverse(obj, board, add_x, add_y):
    x, y = obj.pos[0], obj.pos[1]
    for i in range(1, 8):
        x_ = x + add_x * i
        y_ = y + add_y * i
        if x_ >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
            obj_ = board.cells[x_][y_].piece
            if obj_ == '':
                if shift_check(obj, (x_, y_), board):
                    return True
            elif isrival(obj, (x_, y_), board): 
                if shift_check(obj, (x_, y_), board):
                    return True
                else:
                    return False
            else:
                return False

    return False

#traversal for knight and king
def traverse_kn_kg(obj, board, add_x, add_y):
    x, y = obj.pos[0], obj.pos[1]
    x_ = x + add_x
    y_ = y + add_y
    if x_ >= 0 and x_ < 8 and y_ >= 0 and y_ < 8:
        obj_ = board.cells[x_][y_].piece
        if obj_ == '':
            if shift_check(obj, (x_, y_), board):
                return True
        elif isrival(obj, (x_, y_), board): 
            if shift_check(obj, (x_, y_), board):
                return True
            else:
                return False
        else:
            return False

    return False


def shift_check(obj, to, board):
   
    #shifting the piece to new_position
    pos_now = obj.pos
    board.cells[pos_now[0]][pos_now[1]].piece = ''
    obj_to = ''
    iscutting = False

    if isrival(obj, to, board):
        iscutting = True
        obj_to = board.cells[to[0]][to[1]].piece
        dead.append(obj_to)
        obj_to.alive = False
        board.cells[to[0]][to[1]].piece = ''

    board.cells[to[0]][to[1]].piece = obj
    obj.pos = to

    #checking whether the king is now in check and validating
    return_value = True
    if pieces['king_' + obj.color[0]][0].in_check(board):
        return_value = False 

    #replacing back the piece 
    if iscutting:
        board.cells[to[0]][to[1]].piece = obj_to
        dead.pop()
        obj_to.alive = True
    else:
        board.cells[to[0]][to[1]].piece = ''
    board.cells[pos_now[0]][pos_now[1]].piece = obj
    obj.pos = pos_now

    return return_value


