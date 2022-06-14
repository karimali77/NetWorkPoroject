from socket import *
import hashlib
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "127.0.0.1"
PORT = 4321
client_socket.connect((IP,PORT))
file_content = client_socket.recv(2048).decode()                    # file content from server
hash_file_content_from_server = client_socket.recv(1024).decode()   # hash from server
hash_file_content = hashlib.md5(file_content.encode('utf-8')).hexdigest()  # hash to my file content
print("hash_file_content_from_server: " +hash_file_content_from_server)
print("hash_file_content: " + hash_file_content)
if(hash_file_content == hash_file_content_from_server):
 print("The connection is secure")
 try:
  file = open("downloads/download" + ".txt", "w")
  file.write(file_content)
  file.close()
 except error as e:
  print(e)
else:
 print("The connection is not secure")

client_socket.close()

