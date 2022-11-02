import socket
from threading import *
import psycopg2

def message_sender(ClientMultiSocket):
    prompt = 'Enter the recipient number(enter NONE if you want to stop messaging):'
    while True:
        reciever = input(prompt)
        if(reciever == "NONE"):
            break
        message = input("Message: ")
        ClientMultiSocket.sendall(str.encode(wrap_message(reciever, message)))
        # res = ClientMultiSocket.recv(1024)
        # print(res.decode('utf-8'))

def message_reciever(ClientMultiSocket):
    prompt = 'Enter the recipient number(enter NONE if you want to stop messaging):'
    while True:
        res = ClientMultiSocket.recv(1024)
        if not res:
            break
        print("\nReceived: ", res.decode('utf-8'))
        print(prompt, end = "", flush=True)

def wrap_message(reciever, message):
    return reciever+"\n"+message

def verify_with_server(uname, upwd):
    pass

def add_to_server(uname, upwd):
    pass

def make_user_sql(uname, upwd):
    pass

def connect_to_sql(params):
    conn = psycopg2.connect(**params)
    pass

choice = input("Press 0 for login and 1 for signup")
if choice == "1":
    uname = input("Enter username")
    upwd = input("Enter password")
    add_to_server(uname, upwd)
    make_user_sql(uname, upwd)
    pass
else:
    uname = input("Enter your username")
    upwd = input("Enter your password")
    verify_with_server(uname, upwd)
    pass

connect_to_sql()


ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 9000
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)

print('Enter your username: ')


receiving_thread = Thread(target=message_reciever, args=(ClientMultiSocket, ))
sending_thread = Thread(target=message_sender, args=(ClientMultiSocket, ))
receiving_thread.start()
sending_thread.start()
# ClientMultiSocket.close()

