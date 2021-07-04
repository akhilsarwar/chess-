import socket
import select
import pickle 

IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)
FORMAT = 'utf-8'
HEADER = 64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(ADDR)
server.listen()

sockets = [server]
clients = {}

print('SERVER LISTENING ON ([{0}]:[{1}]) '.format(ADDR[0], ADDR[1]))

class Client_Details:
    def __init__(self, username, addr):
        self.username = username
        self.addr = addr


def snd_msg(client, msg_info):
    client.send(msg_info['header'].encode(FORMAT))
    client.send(pickle.dumps(msg_info['msg']))



def recv_msg(client):
    header = (client.recv(HEADER)).decode(FORMAT)
    if header:
        msg_len = int(header)
        msg = pickle.loads(client.recv(msg_len))
        print(msg)
        return {'msg' : msg, 'header' : header}
    return False



def prep_msg(msg):
    msg_len = str(len(msg))
    header = msg_len + ' ' * (HEADER - len(msg_len))
    return {'msg' : msg, 'header' : header}



def get_turn_info():
    if len(sockets) == 2:
        return prep_msg('1')
    elif len(sockets) == 3:
        return prep_msg('0')
    else:
        return False



def remove_client(client):
    sockets.remove(client)
    client_info = clients.pop(client)
    print('CLIENT [{0} : {1}] DISCONNECTED!!'.format(client_info.username, client_info.addr))


def add_client(client, username_info, addr):
    sockets.append(client)
    clients[client] = Client_Details(username_info['msg'], addr)
    print('CONNECTION ESTABLISHED SUCCESSFULLY, "{0}" IS NOW CONNECTED'.format(clients[client].username))






def main():
    while True:

        read_sockets, _, exception_sockets = select.select(sockets, [], sockets)
        
        for current_socket in read_sockets:
            if current_socket == server:
                if len(sockets) < 3:
                    client, addr = server.accept()

                    #now server accepts the client username 
                    username_info = recv_msg(client)
                    if username_info:
                        add_client(client, username_info, addr)

                        turn_info = get_turn_info()
                        if turn_info:
                            snd_msg(client, turn_info)


            else:
                try:
                    msg_info = recv_msg(current_socket)
                    
                    #now sending the recieved message to all clients, (essentially the only client remaining)
                    for socket_ in sockets:
                        if socket_ != server and socket_ != current_socket:
                            snd_msg(socket_, msg_info)
                except:
                    remove_client(current_socket)                    

        for socket_ in exception_sockets:
            remove_client(socket_)



    
if __name__ == "__main__":
    main()
