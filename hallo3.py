from datetime import datetime

def time_stamp():
    """Returns the time in HH:MM:SS format"""
    return datetime.now().strftime("%H:%M:%S")

def print_message(message):
    """Prints the message with the current time"""
    print(f"{time_stamp()} {message}")

def main():
    # Greeting
    print_message("Hello!")
    # Opening question
    print_message("How can I help you?")

    while True:
        user_input = input()
        print(f"{time_stamp()} {user_input}")  # print user input with timestamp

        # If the user types bye → exit
        if user_input.lower() == "bye":
            print_message("Goodbye!")
            break
        
        # Repeat the user's input
        print_message(user_input)

if __name__ == "__main__":
    main()
