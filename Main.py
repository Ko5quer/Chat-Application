
from message import write_message,check
import time 


#Main
name=str(input("Enter your username: "))
while True:
    try:
        with open("chat.txt","r") as file:
            print("file opened succesfully")
            enter=int(input("Would you like to write a message: 1.Yes   2.No: "))

            if (enter==1):
                while True:     
                    if (check()):
                        write_message(name)
                        time.sleep(30)
                    else:
                        print("1")
                        time.sleep(30)
                        continue   
            else:
                print("Exiting the system")
                  
    except FileNotFoundError:
        with open("chat.txt","w") as chat:
            message=str(input("Enter the first message: "))
            chat.write(name+": "+message+"\n")



