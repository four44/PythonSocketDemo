import threading
import socket
user = input('user? =')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def split(word):
    return [char for char in word]

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            word = message
            list1 =split(word)
            l = []
            l.append(list1[len(list1) - 2])
            l.append(list1[len(list1) - 1])
            if message == "alias?":
                client.send(user.encode('utf-8'))
            # elif l[0] == list1[len(alias)+1] and l[1] == list1[len(alias)+2]:
            #     print(message)
            else:
                print(message)
                #print(l)

            # else:
            #     print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{user}:{input("")}'

        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
