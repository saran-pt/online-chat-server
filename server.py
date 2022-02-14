import socket
import threading

PORT = 9090
HOST = socket.gethostbyname(socket.gethostname()) #local host

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

clients = []


def start():
    """
    Thread to accept clients
    :return: None
    """
    server.listen()
    print("[SERVER] Server is listening now...")
    
    while True:
        try:
            client_socket, address = server.accept()
            clients.append(client_socket)
            print(f"{address} is connected")

            thread = threading.Thread(target=client_handle , args=(client_socket,))
            thread.start()
        except Exception as e:
            print("[EXCEPTIO]", e)


def client_handle(client_socket):
    """
    Handle messages from the client
    :param client_socket: socket
    :return: None
    """
    try:
        name = client_socket.recv(1024).decode('utf-8')
        broadcast(f"{name} is connected now! :", "")

        while True:
            
            msg = client_socket.recv(1024).decode('utf-8')
            if msg == 'exit':
                clients.remove(client_socket)
                broadcast(f"{name} has left the room! :", "")
                break
            else:
                broadcast(msg, name)
    
    except Exception as e:
        print('[EXCEPTION]', e)

    client_socket.close()


def broadcast(message, name):
    """
    send messages to all clients
    :param message: str
    :param name: str
    :return: None
    """
    for client in clients:
        try:
            client.send(f'{name} : {message}'.encode('utf-8'))
        except:
            print('[EXCEPTION ON BROADCAST]')


if __name__ == '__main__':
    start()