"""
This is tcp-ip client program to send game attribute data to 
game server and receive target variable.This will help to
test tcp-ip communication part of game server.
input   : attributes
outpust : target variable
"""

import socket

def client_program():
    host = socket.gethostname()
    host ="localhost"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    #message = "6,9,13,23,0,5,8,6,10"
    message="12,9,0"

    while message.lower().strip() != 'bye':
        print("Sending Data to server : \n",message)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = 'bye'
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
