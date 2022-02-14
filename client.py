import socket
import threading


PORT = 9090
ADDRESS = '192.168.137.1'

client = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
client.connect((ADDRESS , PORT))


def send_message():
    """
    Thread to send message to server
    :return: None
    """
    try:
        client.send(name.encode('utf-8'))
        while True:
            msg = input()
            # print(f"{name} : {msg}")
            client.send(msg.encode('utf-8'))
            if msg == 'exit':
                client.close()
                break

    except Exception as e:
        # print("[EXCEPTION OCCURS]", e)
        client.close()


def receive_message():
    """
    Receive message from server
    :return: None
    """
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("[EXCEPTION WHILE RECEVING]")
            client.close()  
            break

name = input("Please Enter you'r name: ")

thread1 = threading.Thread(target=send_message)
thread1.start()

thread2 = threading.Thread(target=receive_message)
thread2.start()