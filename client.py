import socket
import threading
from params import *

def main():

    # Connection au serveur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((PARAM_SERVER_IP, PARAM_SERVER_PORT))

    # Saisie du pseudo
    pseudo = input("Votre pseudo : ")

    # Creation de la socket client
    # TODO

    # Notification des infos clients au serveur (pseudo, socket de reception)
    # TODO

    while True:

        # Saisie d'un message
        message = input(f"{pseudo}> ")

        # Envoi du message
        client_socket.sendall((pseudo+"> "+message).encode('utf-8'))

        # Reception de la réponse
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"{response}")

if __name__ == "__main__":
    main()