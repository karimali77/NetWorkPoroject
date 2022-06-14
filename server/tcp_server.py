from socket import *
import socket
import threading
import hashlib

IP = "127.0.0.1"
PORT = 4321
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP,PORT))
server_socket.listen(5)
print("Server Running....")

def myThread(client_socket,client_address):
    while True:
        words = ""
        try:
            file = open("files/file.txt", "r")
            for row in file:
                words_of_row = row.split()
                for word in words_of_row:
                    words += word + " "
                words += "\n"
            md5_words = hashlib.md5(words.encode('utf-8')).hexdigest()
            client_socket.send(words.encode())
            client_socket.send(md5_words.encode())
        except socket.error as e:
            print(e)
            client_socket.send(str(e).encode())
        except KeyError as e:
            client_socket.send("This file is not exist.".encode())
        except :
            client_socket.send("Something went wrong")


(client_socket ,client_address) = server_socket.accept()
th = threading.Thread(target=myThread,args=(client_socket,client_address))
th.start()

