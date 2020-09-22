import socket


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))  # connect to the server
    str1 = input(" Enter string 1 -> ")
    str2 = input(" Enter string 2 -> ")

    client_socket.send(str1.encode())
    client_socket.send(str2.encode())
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
