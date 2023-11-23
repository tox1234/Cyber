import socket

MAX_PACKET = 1024

commands = ["Name", "Exit", "Time", "Rand"]

def command(message):
    """
    checks to see if message is a valid command
    :param message: the command the user has entered
    :type: string
    :return: if the message is a command then it will return the message and if it isn't it will return "'ot valid'
    """
    if message not in commands:
        message = 'not valid'
    return message



def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect(('127.0.0.1', 1729))
        while True:
            message = input("Enter command")
            message = command(message)
            if message != 'not valid':
                my_socket.send(message.encode())
                response = my_socket.recv(MAX_PACKET).decode()
                print(response)
                if response == 'You were disconnected from the sevrer':
                    break
            else:
                print('not a valid command')
    except socket.error as err:
        print("Received socket error " + str(err))
    finally:
        my_socket.close()


if __name__ == '__main__':
    main()