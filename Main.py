
from message import write_message,check_message
import time 


#Main
name=str(input("Enter your username: "))

try:
    with open("message.txt","r") as file:
        print("file opened succesfully")
        while True:
            if (check_message()):
                write_message()
            else:
                continue
            time.sleep(30)
except FileNotFoundError:
    with open("message.txt","w") as chat, open("copy.txt","w") as copy:
        message=str(input("Enter the first message: "))
        chat.write(name+": "+message+"\n")
        copy.write(name+": "+message+"\n")



