
def display_message():
    try:
        with open("chat.txt", "r") as chat:
            line=chat.read()
            print(line)
    except FileNotFoundError:
        print ("The file failed to open")


def write_message(name):
    display_message()
    try:
        with open("chat.txt","a") as chat:
                
                message=input(name +":")
                chat.write(name+ ": "+message+'\n')

    except FileNotFoundError:
        print ("file faied to open")

def check_message():
    try:
        with open ("chat.txt","r") as chat, open("copy.txt","r+") as copy:
            content=chat.read()
            content_cpy=copy.read()

            #update the copy if the lines are different   
            if (content!=content_cpy):
                copy.write(content)
                return True
    except FileNotFoundError:
        with open("copy.txt","w") as copy:
            copy.write("file created")
    return False






