import sys, os, socket, time, pickle

from helper import getSocketName

def executeAdd(args):
    try:
        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        socketPath = getSocketName()
        client.connect(socketPath)
    except:
        print("Error connecting to socket. Make sure the daemon is running")
        sys.exit(1)

    if args.command:
        addCommand = {'mode': 'add', 'command': args.command, 'path': os.getcwd()}
        data_string = pickle.dumps(addCommand, -1)
        client.send(data_string)
        answer = client.recv(1024)
        print(pickle.loads(answer))
        client.close()
