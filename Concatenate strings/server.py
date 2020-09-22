import socket


def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:

        data1 = conn.recv(1024).decode()
        data2 = conn.recv(1024).decode()
        if not data1:
            # if data is not received break
            break
        string = str(data1) + str(data2)

        data = string
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
