import socket
import threading

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.29'
    port = 12346
    client_socket.connect((host, port))

    pseudo = input("Votre pseudo : ")

    while True:
        message = input(f"{pseudo}> ")
        client_socket.sendall((pseudo+"> "+message).encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"{response}")


if __name__ == "__main__":
    main()