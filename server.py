import socket
import sys
HOST = '0.0.0.0'
PORT = 80

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

while (True):

    conn, addr = socket.accept()
    print('New client connected ..')
    reqCommand = conn.recv(1024)
    print('Client> %s' %(reqCommand))
    if (reqCommand == 'quit'):
        break
    else:
        string = reqCommand.split(' ', 1)
        reqFile = string[1]

        if (string[0] == 'put'):
            with open(reqFile, 'wb') as file_to_write:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file_to_write.write(data)
                    file_to_write.close()
                    break
            print('Receive Successful')

        elif (string[0] == 'get'):
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
            print('Send Successful')
            
    conn.close()

socket.close()