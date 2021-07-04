import pickle
import main

def get_send_info():
    i = 0
    while main.play == '':
        print(i)
        i += 1
        continue
    while main.play.isturn:
        continue
    send_info = {'from' : main.board.last_move['from'], 'to' : main.board.last_move['to']}
    return send_info
    
    
def update_rival_lastmove(move_info):
    from_ = move_info['from']
    to_ = move_info['to']
    obj = main.board.cells[from_[0]][from_[1]].piece
    player_lastmove = main.board.last_move
    obj.move(main.board, to_)
    print('last self move:  {0}'.format(player_lastmove))
    main.select.alter_lastmove_highlight(player_lastmove, main.board)
    print('last rival  move:  {0}'.format(main.board.last_move))
    main.select.alter_lastmove_highlight(main.board.last_move, main.board)
    main.play.change_turn()


    
