from transfer_data import Transfer_data
import json
import main

def get_send_info():
    i = 0
    while main.play == '':
        i += 1
        print(i)
    while main.play.isturn:
        continue
    send_info = {}
    send_info['object'] = Transfer_data(main.board.last_move, (-1, -1), main.board.last_move.pos)
    send_info_json = json.dumps(send_info)
    return send_info_json
    
    
def update_rival_lastmove(msg):
    move_info = json.loads(msg)
    obj = move_info['object'].obj
    from_ = move_info['object'].from_
    to_ = move_info['object'].to_
    obj.move(main.board, to_)


    
