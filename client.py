#client side script
import socket
import threading
import pickle
import main
from multiplayer_funcs import get_send_info
from multiplayer_funcs import update_rival_lastmove


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


def setup():
    name = input('username: ').strip()
    snd_msg(name)

    turn = recv_msg()
    game_thread = threading.Thread(target = main.main, args = (int(turn),))
    game_thread.start()

    if int(turn) == 0:
        while True:
            msg_recieved = recv_msg()
            update_rival_lastmove(msg_recieved)
            print(msg_recieved)

            msg_tosend = get_send_info()
            snd_msg(msg_tosend)
    
    else:
        while True:
            msg_tosend = get_send_info()
            snd_msg(msg_tosend)

            msg_recieved = recv_msg()
            update_rival_lastmove(msg_recieved)
            print(msg_recieved)

if __name__ == "__main__":
    setup()
