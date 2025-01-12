try:
    with open("chat.txt", "r") as chat:
        chat.write("This is a test message\n")
    print("File created and written successfully.")
except Exception as e:
    print(f"Error: {e}")