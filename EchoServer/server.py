"""
Branigan McPeters
bmcpeter@my.athens.edu
00083473
CS 415 ASG 5 Question 2

Multithreaded Echo Client/Server Fortune Teller
Server Side
"""

import socket
import random
from threading import Thread


# List of fortunes
fortunes = ["Beware the ides of march", "Throw caution to the wind. Today is the day to make life changes.",
            "Someone very close to you is thinking of you today.", "The odds are in your favor today.", "Don't go outside tonight."]


class Server:
    def __init__(self):
        # Set up server side
        self.server = socket.socket()
        port = 9876
        # Bind port to IP addr
        self.server.bind(('127.0.0.1', port))
        # Listen for client request
        print("Waiting for connection")
        self.server.listen(2)

        self.loop()

    def loop(self):
        # Accept connections and spawn threads to handle client requests
        while True:
            conn, addr = self.server.accept()
            x = Thread(target=Server.client_thread, args=(conn, addr,))
            x.start()

    def client_thread(conn, addr):
        # Receive the clients' messages and print
        print(addr, ' has connected')
        while True:
            data = conn.recv(1024).decode()
            if data == None:
                break
            elif data == "Thank you":
                conn.sendall(b'*whimsical noises')
                break
            else:
                print("Client Message:", data)
                index = random.randint(0, len(fortunes)-1)
                response = fortunes[index]
                conn.sendall(response.encode())
        conn.close()


s = Server()
s.close()
