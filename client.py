import socket
import sys
import pdb
from progressbar import ProgressBar, Percentage, Bar, ETA
from time import sleep
import os

HOST = sys.argv[2]
PORT = int(sys.argv[3])
file_name = sys.argv[1]
progress, progress_maxval = 0, 100


def send(file_name):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send("put " + file_name)
    # pdb.set_trace()
    # string = file_name.split(' ', 1)
    inputFile = file_name
    pbar = ProgressBar(widgets=['Progress ', Percentage(), Bar(), ' ', ETA(), ], maxval=progress_maxval).start()
    sleep(1)

    with open(inputFile, 'rb') as file_to_send:
        size = os.stat(inputFile).st_size
        total_read = 0
        for data in file_to_send:
            progress = (total_read*100/size)
            pbar.update(progress)
            socket1.sendall(data)
            sleep(0.5)
            total_read += len(data)

    pbar.finish()
    print('File sent successfully!')

    socket1.send('quit')
    socket1.close()
    
    sys.exit(0)


while(True):
    send(file_name)
        
