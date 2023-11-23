#written by Ido
import socket
import random
from datetime import datetime

MAX_PACKET = 4
QUEUE_LEN = 1
NAME = "ido's server"


def time():
    """
    Returns the current time
    :return: current_time - the time separated into hours, minutes and seconds
    """
    time_and_date = datetime.now()
    current_time = time_and_date.strftime('%H:%M:%S')
    return current_time


def rand():
    """
    Generates a random number between 1 and 10
    :return: random_num - the random num
    """
    random_num = random.randint(1, 10)
    return str(random_num)



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('0.0.0.0', 1729))
        server_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = server_socket.accept()
            try:
                while True:
                    request = client_socket.recv(MAX_PACKET).decode()
                    if request == 'Rand':
                        sent_message = rand()
                    elif request == 'Time':
                        sent_message = time()
                    elif request == 'Name':
                        sent_message = NAME
                    elif request == 'Exit':
                        client_socket.send('You were disconnected'.encode())
                        break
                    else:
                        sent_message = 'not a valid command'
                    client_socket.send(sent_message.encode())
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
    except socket.error as err:
        print('received socket error on server socket' + str(err))
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
