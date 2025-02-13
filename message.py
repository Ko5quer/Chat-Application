
class Texts:
    def __init__(self,name):
        self.name=name
        self.logs=" "
        self.cplogs=" "
    
    def def_file(self):
        try:
          with open ("chat.txt","r") as chat:
            self.logs=chat.read()
        except FileNotFoundError:
            with open("chat.txt","w") as chat:
                message=str(input("Enter the first message: "))
                chat.write(self.name+": "+message+"\n")
    
    
    def disp_text(self):
        try:
            with open("chat.txt", "r") as chat:
                print(chat.read())
        except FileNotFoundError:
            print ("The file failed to open")

    def write_message(self):
        self.disp_text()
        try:
            with open("chat.txt","a+") as chat:
                        message=input(self.name +":")
                        chat.write(self.name+ ": "+message+'\n')
                        self.logs=chat.read()
                        self.change()
        except FileNotFoundError:
            print("File failed to open")
    
    def check(self):
        self.update()
        if(self.logs != self.cplogs):
            return True
        else:
            return False
        
    def update(self):
        try:
            with open("chat.txt","r") as chat:
                self.logs=chat.read()
        except FileNotFoundError:
            print("Error finding chat logs")

    def change(self):
        self.cplogs=self.logs



