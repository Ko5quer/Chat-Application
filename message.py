
def display_message():
    try:
        with open("chat.txt", "r") as chat:
            line=chat.read()
            print(line)
    except FileNotFoundError:
        print ("file failed to open")


def write_message(name):
    display_message()
    try:
        with open("chat.txt","a") as chat:
            message=input(name +":")
            chat.write(message)
    except FileNotFoundError:
        print ("file faied to open")

def check_message():
    try:
        with open ("chat.txt","r") as chat, open("cpychat.txt","r+") as copy:
            line=chat.read()
            line1=copy.read()
            if (not line==line1):
                copy.write(line)
                return True
    except FileNotFoundError:
        print("file failed to open")
    return False



