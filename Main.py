
import time
import os
from message import write_message,check_message,display_message


#Main
name=str(input("Enter your username: "))
print("Current Working Directory:", os.getcwd())
try:
    with open("message.txt","r") as file:
        content=file.read()
        print("file opened succesfully")
        print(content)
except FileNotFoundError:
    with open("message.txt","w") as chat, open("copy.txt","w") as copy:
        message=str(input("Enter the first message: "))
        chat.write(name+": "+message+"\n")
        copy.write(name+": "+message+"\n")
        print("Q2")


