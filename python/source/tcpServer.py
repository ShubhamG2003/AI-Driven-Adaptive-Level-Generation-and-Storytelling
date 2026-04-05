"""
This file contains program to test predictions using all ensemble methods.

modelList = ["BAG-0", "BAG-1", "BOOST-0", "BOOST-1", "STACK-0", "STACK-1", "LDA"]
"""

from Ensemble import BuildModel, GetPrediction
import socket


def GameServer():
    BuildModel("LDA")
    host = "localhost"
    port = 5000
    print(f"Host: {host} Port: {port}")
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        rdata = conn.recv(1024).decode()
        if not rdata:
            # if data is not received break
            break
        print("from connected user: " + str(rdata))
        data = GetPrediction(rdata)
        print(f"{data} type of data is {type(data)}")
        conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection


# -----------------------------------------------------------------------------------
GameServer()
