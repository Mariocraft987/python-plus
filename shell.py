print("python plus (c)")
print("Tip: type '/help' for more commands")

while True:
    command = input("Type a command: ")

    if command == "/help":
        print("Available commands:")
        print("1. /help - Show available commands")
        print("2. /greet - Greet the user")
        print("3. /date - Print the current date")
        print("4. /time - Print the current time")
        print("5. /math - Perform basic arithmetic operations")
        print("6. /exit - Exit the program")
    
    elif command == "/greet":
        name = input("Enter your name: ")
        print("Hello,", name, "!")
    
    elif command == "/date":
        from datetime import date
        today = date.today()
        print("Today's date is:", today)
    
    elif command == "/time":
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current time is:", current_time)
    
    elif command == "/math":
        expression = input("Enter a mathematical expression: ")
        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
    
    elif command == "/exit":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid command. Type '/help' for available commands.")
