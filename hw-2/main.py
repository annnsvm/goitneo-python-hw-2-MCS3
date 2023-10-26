import task1


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = task1.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(task1.add_contact(args, contacts))
        elif command == "change":
            print(task1.change_contact(args, contacts))
        elif command == 'phone':
            print(task1.show_contact(args, contacts))
        elif command == "all":
            print(task1.show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
