from json import loads, dumps


# ------------------------- Global Methods For Server And Client ------------------------- #
# Send Message To Socket
def send_message(socket, msg_type, message):
    # Message Type And Content Dictionary
    message_dict = {
        'type': msg_type,
        'message': message
    }
    message_dict = dumps(message_dict).encode('utf-8')

    # 10 Byte For Size Of Message
    size = str(len(message_dict)).zfill(10).encode('utf-8')

    # Send To Socket
    socket.send(size)
    socket.send(message_dict)


# Receive Message From Socket
def receive_message(socket):
    size = socket.recv(10)

    # Check Connection Close
    if not size:
        return None

    else:
        size = int(size.decode('utf-8'))

        message = socket.recv(size).decode('utf-8')
        message = loads(message)

        return message


# ------------------------- User CLI Methods ------------------------- #
# For Print Line
def print_line():
    print('------------------------------')


# Get Int Choice From User
def get_int(message):
    print(message)

    while True:
        inp = input('Your Input: ')

        try:
            inp = int(inp)
            break

        except Exception:
            print("Wrong Input!!! Please Enter Valid Number.")

    return inp
