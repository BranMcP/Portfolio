"""
Branigan McPeters
bmcpeter@my.athens.edu
00083473
CS 415 ASG 5 Question 2

Multithreaded Echo Client/Server Fortune Teller
Client Side
"""
import socket


class Client:
    def __init__(self):
        # Create a socket objects
        self.client = socket.socket()

        # Define the port on which you want to connect
        port = 9876
        self.connect(port)

    def connect(self, port):
        # connect to the server on local computer
        try:
            self.client.connect(('127.0.0.1', port))
        except:
            print("Something went wrong...")

    def send(self, message):
        self.client.sendall(message)
        return self.client.recv(1024)


# Create instance of client class
c = Client()
print(c.send(b'Please tell me my fortune'))
print(c.send(b'Thank you'))
c.client.close()  # added
