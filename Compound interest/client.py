import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    P = input(" Enter initial principal balance -> ")  # take input
    r = input(" Enter	interest rate -> ")  # take input
    n = input(" Enter number of times interest applied per time period -> ")  # take input
    t = input(" Enter number of time periods elapsed -> ")  # take input

    client_socket.send(P.encode())  # send message
    client_socket.send(r.encode())  # send message
    client_socket.send(n.encode())  # send message
    client_socket.send(t.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Final Amount ' + data)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

