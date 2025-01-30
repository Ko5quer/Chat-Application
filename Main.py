
from message import write_message,check
import time 


#Main

#Gets user input
name=str(input("Enter your username: "))
while True:
    try:
        with open("chat.txt","r") as file:
            choice=int(input("1.Write message \n2.Refresh \n3.Exit \nPlease choose what you want to do: "))

            if (choice==1): 
                        write_message(name)
                        #to delay it and stop spam messages
                        time.sleep(10)
                        time.sleep(10)
            elif (choice==2):
                if (check()):
                    write_message(name)
                else:
                     print("No new messages found, try again")
            elif (choice==3):
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Please choose between 1,2 and 3")      

    except FileNotFoundError:
        #To create a file when a file doesnt exist
        with open("chat.txt","w") as chat:
            message=str(input("Enter the first message: "))
            chat.write(name+": "+message+"\n")



