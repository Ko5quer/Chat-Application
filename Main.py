
from message import write_message,check_message
import time 


#Main
name=str(input("Enter your username: "))
while True:
    try:
        with open("message.txt","r") as file:
            print("file opened succesfully")
            enter=int(input("Would you like to write a message: 1.Yes   2.No: "))

            if (enter==1):
                write_message(name)
            while True:     
                if (check_message()):
                    write_message(name)
                else:
                    print("1")
                    time.sleep(30)
                    continue         
    except FileNotFoundError:
        with open("message.txt","w") as chat, open("copy.txt","w") as copy:
            message=str(input("Enter the first message: "))
            chat.write(name+": "+message+"\n")
            copy.write(name+": "+message+"\n")



