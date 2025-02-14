
class Texts:
    def __init__(self,name):
        self.name=name
        self.logs=" "
    
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
        except FileNotFoundError:
            print("File failed to open")
    
    def check(self):
        try:
            with open("chat.txt","r") as chat:
                content=chat.read()
                print(f"Content of file:\n{content}")
                print(f"Content of ccopy:\n{self.logs}")
                if(content==self.logs):
                    return 3
                else:
                    self.logs=content
                    return 4
                print(content)
        except FileNotFoundError:
            print("Chat logs not found")



