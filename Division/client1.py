import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    Num1 = input(" Enter Num2 -> ")  # take input
    Num2 = input(" Enter Num1 -> ")  # take input

    client_socket.send(Num1.encode())  # send message
    client_socket.send(Num2.encode())  # send message

    data = client_socket.recv(1024).decode()  # receive response

    print('Final Result ' + data)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
