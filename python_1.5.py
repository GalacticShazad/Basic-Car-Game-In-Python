command=""
started = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            print("Car is starting...")
            started = True
    elif command == "stop":
        if started:
            print("Car stopped")
            started = False
        else:
            print("Car is already stopped!")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("help - to display this help message")
        print("quit - to exit the game")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")