import socket
import threading
from params import *

list_clients = []

def process_message(param_message) :
    '''
    fonction permettant de déduire le pseudo et le message
    :param param_message:
    :return: retourne le pseudo et le message
    '''
    longueur_pseudo = param_message.find(">")
    p = param_message[:longueur_pseudo]
    m = param_message[longueur_pseudo + 2:]
    return p, m

def handle_client(client_socket):
    '''
    fonction qui traite les messages du reçu d'un client
    :param client_socket:
    '''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message_avec_pseudo = data.decode('utf-8')
        pseudo, message = process_message(message_avec_pseudo)

        # Si le client n'est pas listé, on l'ajoute à la liste
        if pseudo not in list_clients:
            list_clients.append(pseudo)

        print(f"liste des utilisateurs : {list_clients}")
        print(f"Received message: {message} from {pseudo}")

        # Envoi de ma réponse au client
        response = message
        client_socket.sendall(response.encode('utf-8'))

    # Fermeture de la socket à la fin du traitement du message
    client_socket.close()


def main():
    '''
    Méthode principale
    :return:
    '''

    # Ouverture de la socket et ecoute dessus
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((PARAM_SERVER_IP, PARAM_SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {PARAM_SERVER_IP}:{PARAM_SERVER_PORT}")

    while True:

        # Reception d'un message d'un client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # On traite le message dans un thread dédié => méthode handle_client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

