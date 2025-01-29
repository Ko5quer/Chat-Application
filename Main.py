
from message import write_message,check
import time 


#Main

#Gets user input
name=str(input("Enter your username: "))
while True:
    try:
        with open("chat.txt","r") as file:
            print("file opened succesfully")
            choice=int(input("Would you like to write a message: 1.Yes   2.No 3.Exit"))

            if (choice==1):
                while True:     
                    if (check()):
                        write_message(name)
                        #to delay it and stop spam messages
                        time.sleep(10)
                    else:
                        print("1")
                        time.sleep(10)
            elif (choice==2):
                print("Exiting the system")
            elif (choice==3):
                print("Exiting the system. Goodbye!")
            else:
                print("Please choose between 1,2 and 3")      

    except FileNotFoundError:
        #To create a file when a file doesnt exist
        with open("chat.txt","w") as chat:
            message=str(input("Enter the first message: "))
            chat.write(name+": "+message+"\n")



