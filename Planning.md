
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
		display_message()
		open chat (chat.txt, append)
		display name ":"
		enter message
		if (chat is_open){
			chat <<message <<"/n"
		}
		else {
			display "file failed to open"
		}
		close chat
	}

```


```
	check_message(){
		open chat(chat.txt, read)
		open copy(cpchat.txt, read)
		if (copy is_open and chat is_open){
			//compares two files
			while (getline(copy,line) and getline(chat,line1){
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


```
	Main(){
		int choice
		string name, message
		display "Enter your username"
		enter name
		while (true)
			//checks to see if file exists
			open chat(chat.txt,read)
			
			if (not chat is_open){
				//breaks if things dont work
				display "would you like to write a message 1.Yes  2.No"
				enter choice
				open chat(chat,write)
				if (choice==2){
					break
				}
				//creates file then writes to it 
				display name ": "
				enter message 
				chat<<name<<":"<<message
				close chat
			}
			else {
				write_message(name)
			}
			allows the loop to break 
			display "Would you like to continue 1.Yes  2.No"
			enter choice
			if (choice==2){
				break
			}
			delay 30sec
	}

```