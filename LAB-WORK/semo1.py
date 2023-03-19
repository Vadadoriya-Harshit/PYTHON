import socket
import threading

def receive_message(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(f"{client_address}: {message}")
            client_socket.send("Message received".encode())
        else:
            break

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen(1)
    print("Server is running on localhost:8000")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        client_socket.send("Welcome to the chat server!".encode())
        threading.Thread(target=receive_message, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    main()
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8000))

    while True:
        message = input("Enter a message: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")

if __name__ == "__main__":
    main()
