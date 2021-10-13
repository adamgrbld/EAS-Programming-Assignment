from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
import datetime
import timeit
import socket


class AesEncrypt:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    # def encrypt(self, message, key, key_size=256):
    #     message = self.pad(message)
    #     iv = Random.new().read(AES.block_size)
    #     cipher = AES.new(key, AES.MODE_CBC, iv)
    #     return iv + cipher.encrypt(message)

    # def encrypt_file(self, file_name):
    #     begin_time = datetime.datetime.now()
    #     with open(file_name, 'rb') as fo:
    #         plaintext = fo.read()
    #     enc = self.encrypt(plaintext, self.key)
    #     with open(file_name + ".enc", 'wb') as fo:
    #         fo.write(enc)
    #     os.remove(file_name)
    #     print(datetime.datetime.now() - begin_time)
        

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        begin_time = datetime.datetime.now()
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)
        print(datetime.datetime.now() - begin_time)

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = AesEncrypt(key)
clear = lambda: os.system('cls')

# while True:
    # clear()
    # choice = int(input(
    #     "1. Ketik '1' untuk encrypt file.\n2. Ketik '2' untuk decrypt file.\n"))
    # if choice == 1:
# enc.encrypt_file(str(input("Masukkan nama file untuk di encrypt: ")))
    # Create a TCP/IP socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    f = open("./randoma.txt.enc", "wb")
    while True:
        data = connection.recv(32)
        f.write(data)
    #   print(f"received {data}")
        if not data:
            break
    # Clean up the connection
    f.close()
    connection.close()
    break;

enc.decrypt_file("./randoma.txt.enc")    
    # elif choice == 2:
        # enc.decrypt_file(str(input("Masukkan nama file untuk di decrypt: ")))
    # elif choice == "exit":
    #     exit()
    # else:
    #     print("Please select a valid option!")

