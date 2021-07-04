#client side script
import socket
import threading
import pickle
import main


IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)
FORMAT = 'utf-8'
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def snd_msg(msg):
    pickled_msg = pickle.dumps(msg)
    msg_len = str(len(pickled_msg))
    header = msg_len + ' ' * (HEADER - len(msg_len))
    client.send(header.encode(FORMAT))
    client.send(pickled_msg)


def recv_msg():
    header = client.recv(HEADER).decode(FORMAT)
    if header:
        msg_len = int(header)
        msg = pickle.loads(client.recv(HEADER))
        print(msg)
        return msg
    return False



def get_send_info():
    while main.play == '':
        continue
    while main.play.isturn:
        continue
    send_info = {'from' : main.board.last_move['from'], 'to' : main.board.last_move['to']}
    return send_info
    
    
def update_move(move_info):
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



def setup():
    name = input('username: ').strip()
    snd_msg(name)

    turn = recv_msg()
    game_thread = threading.Thread(target = main.main, args = (int(turn),))
    game_thread.start()

    if int(turn) == 0:
        while True:
            msg_recieved = recv_msg()
            update_move(msg_recieved)
            print(msg_recieved)

            msg_tosend = get_send_info()
            snd_msg(msg_tosend)
    
    else:
        while True:
            msg_tosend = get_send_info()
            snd_msg(msg_tosend)

            msg_recieved = recv_msg()
            update_move(msg_recieved)
            print(msg_recieved)

if __name__ == "__main__":
    setup()
