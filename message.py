#Declaring global variables
logs=" "
cp_logs=" "


"""
Function runs once to define the global variables for checking messages
and creates the file if it doesnt exist
"""
def define_variable(name):
     global logs, cp_logs
     try:
          with open ("chat.txt","r") as chat:
            logs=chat.read()
            change()
     except FileNotFoundError:
        with open("chat.txt","w") as chat:
            message=str(input("Enter the first message: "))
            chat.write(name+": "+message+"\n")



def display_message():
    try:
        with open("chat.txt", "r") as chat:
            print(chat.read())
    except FileNotFoundError:
        print ("The file failed to open")


"""
Allows user to write messages and updates the global variables to 
check if the is a new message
"""
def write_message(name):
    global logs
    display_message()
    try:
        with open("chat.txt","a") as chat:
                    message=input(name +":")
                    chat.write(name+ ": "+message+'\n')
                    define_variable(name)

    except FileNotFoundError:
        print ("file faied to open")


"""
Function that checks if a new message has arrived and alerts the user about the new message
"""
def check():
    global cp_logs, logs
    try:
        with open("chat.txt","r") as chat:
            logs=chat.read()
            if(not logs==cp_logs):
                return True
            else:
                return False
    except FileNotFoundError:
        print("File not found, Please try again later")


"""
Updates the copy with the current message
"""
def change():
    global cp_logs,logs
    cp_logs=logs


