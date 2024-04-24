import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
MAX_CONNECTIONS = 5

clients = []
lock = threading.Lock()

def handle_client(client_socket, username):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Broadcast the message to all other connected clients with the sender's username
            broadcast_message(f"{username}: {data}", client_socket)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        with lock:
            clients.remove(client_socket)
            client_socket.close()

def broadcast_message(message, sender_socket):
    with lock:
        for client_socket in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message: {e}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CONNECTIONS)
    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address[0]}:{client_address[1]}")

            # Receive the username from the client
            username = client_socket.recv(1024).decode('utf-8')

            with lock:
                clients.append(client_socket)

            # Start a new thread to handle communication with this client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()


# run this code in cmd using the current file directory and type python server.py in cmd