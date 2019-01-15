import socket
import sys
 
HOST = '' 
PORT = 5555 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
    
except socket.error as msg:
    print('build failed',str(msg))
    sys.exit()
	
s.listen(5)
conn ,addr=s.accept()
print('connected to: ',addr[0]+':'+str(addr[1]))
print('Socket bind complete')