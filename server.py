import socket
import threading

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
    fonction qui traite les messages du client
    :param client_socket:
    '''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message_complet = data.decode('utf-8')
        pseudo, message = process_message(message_complet)

        if pseudo not in list_clients:
            list_clients.append(pseudo)

        print(f"liste des utilisateurs : {list_clients}")
        print(f"Received message: {message} from {pseudo}")
        response = message
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.29'
    port = 12346
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

