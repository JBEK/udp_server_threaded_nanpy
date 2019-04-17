import socket
import sys
from nanpy import (ArduinoApi, SerialManager)
from threading import Thread

localIP     = "192.168.1.25"
bufferSize  = 3

connection = SerialManager ()
a = ArduinoApi (connection = connection)
a.pinMode(3, a.OUTPUT)
a.pinMode(5, a.OUTPUT)

class Server1 (Thread) :
    
    def __init__(self, Server1):
        Thread.__init__(self)
        self.Server1 = Server1


    def run(self):
        
        Port1   = 8080
        
# Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
        UDPServerSocket.bind((localIP, Port1))

        print("UDP server1 up and listening")
        
        while (True):
    
# Definition des data
            data, addr = UDPServerSocket.recvfrom(bufferSize)
    
            int_val = int (data)
    
            print(int_val)
            a.analogWrite (3, int_val)
    
              

class Server2 (Thread) :
    
    def __init__(self, Server2):
        Thread.__init__(self)
        self.Server2 = Server2
    
    def run(self):

        Port2   = 1803

# Create a datagram socket

        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        UDPServerSocket.bind((localIP, Port2))
    
        print("UDP server2 up and listening")
        
# Definition des data
        while (True):
            data2, addr = UDPServerSocket.recvfrom(bufferSize)
    
            int_val2 = int (data2)
    
        
            print(int_val2)
            a.analogWrite (5, int_val2)
    
        
thread_1 = Server1 (Server1)
thread_2 = Server2 (Server2)

thread_1.start ()
thread_2.start ()

#thread_1.join ()
#thread_2.join ()
