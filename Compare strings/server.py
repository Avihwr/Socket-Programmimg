import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data1 = conn.recv(1024).decode()
        data2 = conn.recv(1024).decode()
        if not data1:
            # if data is not received break
            break
        s1 = str(data1)
        s2 = str(data2)

        if s1 == s2:
            msg = 'Same strings'
            data = msg
            conn.send(data.encode())
        if s1 < s2:
            msg = f'{s1} is smaller than {s2}'
            data = msg
            conn.send(data.encode())
        if s1 > s2:
            msg = f'{s1} is bigger than {s2}'
            data = msg
            conn.send(data.encode())

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
