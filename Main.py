from message import Texts
import time 


#Main

#Gets user input
print("--------------User Info--------------")
name=str(input("Enter your username: "))
print("\n")
text=Texts(name)
while True:
    try:
        with open("chat.txt","r") as file:
            print("\n*****Chat-Application-System*****")
            try:
                choice=int(input("1.Write message \n2.Refresh \n3.Exit \nPlease choose what you want to do: "))

                if (choice==1): 
                            text.write_message()
                            #to delay it and stop spam messages
                            time.sleep(10)
                elif (choice==2):
                    if (text.check()==4):
                        print("-"*50)
                        print ("New message detected")
                        print("-"*50, end="\n")
                    elif(text.check()==3):
                        print("-"*50)
                        print("No new messages found, try again")
                        print("-"*50 ,end="\n")
                    else:
                         print ("this is just broken")
                elif (choice==3):
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Please choose between 1,2 and 3")
            except ValueError:
                 print("Please choose between 1,2 and 3")      

    except FileNotFoundError:
        print("File not found")




