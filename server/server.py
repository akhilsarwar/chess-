import socket
import select

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
    client.send(msg_info['msg'].encode(FORMAT))

def recv_msg(client):
    header = (client.recv(HEADER)).decode(FORMAT)
    if header:
        msg_len = int(header)
        msg = (client.recv(msg_len)).decode(FORMAT)
        return {'msg' : msg, 'header' : header}
    return False


def main():

    read_sockets, _, exception_sockets = select.select(sockets, [], sockets)
    
    for current_socket in read_sockets:
        if current_socket == server:
            
            client, addr = server.accept()

            #now server accepts the client username 
            username_info = recv_msg(client)
            if username_info:
                client[client] = Client_Details(username_info['msg'], addr)
                sockets.append(client)
                print('CONNECTION ESTABLISHED SUCCESSFULLY, "{0}" IS NOW CONNECTED'.format(client[client].username))
            else:
                continue

        else:
            msg_info = recv_msg(client)
            
            #now sending the recieved message to all clients, (essentially the only client remaining)
            for socket_ in sockets:
                if socket_ != server and socket_ != current_socket:
                    snd_msg(socket_, msg_info)
    for socket_ in exception_sockets:
        sockets.remove(socket_)
        clients.pop(socket_)



    
if __name__ == "__main__":
    main()
