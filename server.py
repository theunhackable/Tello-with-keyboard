import socket
import datetime
from time import sleep

# CONSTANTS
TELLO = ('192.168.10.1', 8889)
LOCAL_HOST = ('', 9000)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(LOCAL_HOST)

def write_log(data):
    file = open('tellolog.txt','a+')
    message = '[{}] {} : [{}] FROM [{}]\n'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                           data[0],
                                           data[1].upper(),
                                           data[2])
    file.write(message)
    file.close()
    return message
def joystick_command(command):
    server.sendto(command.encode(encoding='utf-8'), TELLO)
    data = [command, 'response', TELLO]
    message = write_log(data)
    return message

def send_command(command):
    try:
        if 'rc' in command:
            message = joystick_command(command)
            return message
        else:
            server.sendto(command.encode(encoding='utf-8'), TELLO)
            print('sending...')
            response, address = server.recvfrom(1518)
            print('recieved...')
            data = [command, response.decode(encoding='utf-8'), address]
            message = write_log(data)
            return message
    except OSError:
        print('OSError:Make sure that the TELLO is connected')
        data = [command, 'OSError', address]
        message = write_log(data)
        return(message)


    