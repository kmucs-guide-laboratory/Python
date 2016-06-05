import socket, sys
HOST = '127.0.0.1'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
key_enc = "1231241231"
import math

def xor(data, key):
    repeat = math.ceil(len(data)/len(key))
    repeatKey = key * repeat
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(data, repeatKey))

while True:
    data = input("Message : ")
    encrypt = xor(data, key_enc)
    print("encrypt : ")
    print(encrypt)
    s.send(encrypt.encode("utf-8"))
    data = s.recv(1024)
    if not data: break
    decrypt = xor(data.decode"utf-8"), key_enc)
    print ("Received Message :", decrypt)

s.close()
