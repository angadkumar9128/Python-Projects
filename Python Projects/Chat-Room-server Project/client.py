import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
    except Exception as e:
        print(f"Error: {e}")

def main():
    HOST = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass

    client_socket.close()

if __name__ == "__main__":
    main()


# run this code in cmd using the current file directory and type python client.py in cmd