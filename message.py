line=" "
copy=" "



def display_message():
    try:
        with open("chat.txt", "r") as chat:
            print(chat.read())
    except FileNotFoundError:
        print ("The file failed to open")


def write_message(name):
    display_message()
    try:
        with open("chat.txt","a") as chat:
                    message=input(name +":")
                    chat.write(name+ ": "+message+'\n')
                    change()

    except FileNotFoundError:
        print ("file faied to open")


def check():
    global copy, line
    try:
        with open("chat.txt","r") as chat:
            line=chat.read()
            if(line!=copy):
                change()
                return True
            else:
                return False


    except FileNotFoundError:
        print("File not found")

def change():
    global copy, line
    copy=line


