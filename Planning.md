
Goal 

Simple chat application
	Features
		1. Messages must change in real time
		2. Users must be able to see and respond to messages
		3. Users take turns responding on one system
		4. Offline 

Implementation
- Using loops to check messages (delay loop)
- Saving info to one text file
- Updating text file 


Pseudocode 

```
	Start
	function display_message(){
		open chat(chat.txt, read)
		
		if (chat is_open) {
			while getline(chat, line)
				display line
		}
		else {
			display "file failed to open"
		}
		close chat 
	}
```

```
	function write_message(name){
		string message
		call display_message()
		open chat (chat.txt, append)
		display name ":"
		enter message
		if (chat is_open){
			chat <<message <<"/n"
			call change()
		}
		else {
			display "file failed to open"
		}
		close chat
	}

```

~This did not work and  a better method was used which used global variables
```
	function check_message(){
		open chat(chat.txt, read)
		open copy(cpchat.txt, read
		if (copy is_open and chat is_open){
			//compares two files
			while (getline(copy,line) and getline(chat,line1)){
				if (not line==line1)
				{
					return true 
				}
			}
		}
		else{
			display"file failed to open" 
		}
		return false
	}

```

``

```
	function check(){
		global string copy, line
		open chat(chat.txt,read)
		if (chat is_open){
			call change()
			return true
		}
		else{
			return false
		}
	}
```

```
	function change(){
		global string logs, cp_logs
		cp_logs=logs
	}
```

```
	Main(){
		string name
		display "Enter your username: "
			enter name
		while (true){
			open chat(chat.txt,read)
			if (chat is_open){
				display "file opened succesfully"
				display "Would you like to write a message 1.Yes 2.No"
				enter choice
				if (choice==1){
					while true:
						//To check if the  is an update to the file and allow the
						//user to write if the is a new message
						if (call check()){
							call write_message(name)
							delay 10sec
						}
						else
							delay 10sec
						}
				}
				else{
					display("exiting the system")
				}
			}
			//creates a file if the file is not there
			else{
				open chat(chat.txt,write)
				display "No message found, Enter the first message:"
				enter message
				chat<<name<<": "<<message<<"\n"
				chat.close
			}
		}
	}
```

```

Variables used
	files
		chat.txt //Name of the file where the chat logs are used
		chat //Used to interact with chat.txt'
	normal variables
		string name 
		string message //Stores the message user writes
		int choice //Gives user option to write message or not
	global variables
		logs //Keeps track of chat.txt content
		cp_logs //compares with logs to see if the is a change in the file
		
	
```