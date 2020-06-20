from _thread import *
import socket
import sys
# freenet
sever = '192.168.1.185'
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((sever, port))
except socket.error as e:
    print(str(e))
    raise e

s.listen(2)
print('Waiting for connection, Server started')


def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])


pos = [(0,0), (100,100)]


def thread_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            # if there is not data
            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print('Received: ', data)
                print('Sending: ', reply)
                conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print('Lost connection')
    conn.close()

current_player = 0
while True:
    conn, addr = s.accept()
    print('Connected to:', addr)
    start_new_thread(thread_client, (conn,  current_player))
    current_player += 1