import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(1)
print ('Socket Listen Start')
connector, addr = s.accept()
key_enc = "1231241231"
import math

def xor(data, key):
    repeat = math.ceil(len(data)/len(key))
    repeatKey = key * repeat
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(data, repeatKey))

while 1:
	data = connector.recv(1024)
	if not data: break
	decrypt = xor(data.decode("utf-8"), key_enc)
	print ("Received Message :", decrypt)
	data = input("Message : ")
	encrypt = xor(data, key_enc)
	connector.send(encrypt.encode('utf-8'))

s.close()
    
