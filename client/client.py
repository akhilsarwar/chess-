#client side script
import socket
import threading


IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)
FORMAT = 'utf-8'
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def snd_msg(msg):
    msg_len = str(len(msg))
    header = msg_len + ' ' * (HEADER - len(msg_len))
    client.send(header.encode(FORMAT))
    client.send(msg.encode(FORMAT))


def recv_msg():
    header = client.recv(HEADER).decode(FORMAT)
    if header:
        msg_len = int(header)
        msg = client.recv(HEADER).decode(FORMAT)
        print(msg)
        return msg
    return False


def main():
    name = input('username: ').strip()
    snd_msg(name)

    turn = recv_msg()

    if int(turn) == 0:
        while True:
            msg_recieved = recv_msg()
            
            #process info
            print(msg_recieved)

            msg_tosend = input('write: ')
            snd_msg(msg_tosend)
    
    else:
        while True:
            msg_tosend = input('write: ')
            snd_msg(msg_tosend)

            msg_recieved = recv_msg()
            #process info
            print(msg_recieved)

if __name__ == "__main__":
    main()
