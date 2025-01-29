#Declaring global variables
logs=" "
cp_logs=" "



def display_message():
    try:
        with open("chat.txt", "r") as chat:
            print(chat.read())
    except FileNotFoundError:
        print ("The file failed to open")

#Allows user to write messages and updates the global variables
def write_message(name):
    display_message()
    try:
        with open("chat.txt","a") as chat:
                    message=input(name +":")
                    chat.write(name+ ": "+message+'\n')
                    change()

    except FileNotFoundError:
        print ("file faied to open")

#Function that checks if a new message has arrived and allows user to respond back
def check():
    global cp_logs, logs
    try:
        with open("chat.txt","r") as chat:
            logs=chat.read()
            if(not logs==cp_logs):
                change()
                return True
            else:
                return False
    except FileNotFoundError:
        print("File not found, Please try again later")

#updates the copy
def change():
    global cp_logs,logs
    cp_logs=logs


