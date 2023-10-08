commands:dict = {
    "help": "shows available commands",
    "hello": "prints 'How can I help you?'",
    "add [user] [phone]": "adds new contact",
    "change [user] [phone]": "changes exist contact phone number",
    "phone [user]": "prints exist contact phone number",
    "all": "prints all exist contacts",
    "exit": "enter 'close' or 'exit' to close the assistant",
}

def help():
    formatted_commands = ""
    for key, value in commands.items():
        formatted_commands += f"==> {key}: {value}\n"
    return formatted_commands

def parse_input(user_input:str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args:list[str, str], contacts:dict):
    if len(args) != 2:
        return "Please specify user name and phone number in format: add [user] [phone]"
    name, phone = args
    if (contacts.get(name.lower())):
        print(
            f"Contact '{name}' with '{contacts.get(name)}' phone number is already exist.")
        command = input(
            "Do you want to update it? Enter 'Yes' for update ").strip().lower()
        if command == 'yes':
            return change_contact(args, contacts)
        else:
            return f"Contact '{name}' wasn't updated."
    contacts[name] = phone
    return "Contact added."


def change_contact(args:list[str, str], contacts:dict):
    if len(args) != 2:
        return "Please specify user name and phone number in format: change [user] [phone]"
    name, phone = args
    if (contacts.get(name)):
        contacts[name] = phone
        return f"Contact '{name}' updated with '{phone}' phone number."
    else:
        return f"Contact '{name}' wasn't found."


def show_phone(args:list[str, str], contacts:dict):
    if len(args) != 1:
        return "Please specify user name."
    name:str = args[0]
    phone:str = contacts.get(name)
    if phone:
        return phone
    else:
        return f"Contact '{name}' wasn't found."


def show_all(contacts:dict):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot! Enter a commmand or 'help' to see available commands.")
    while True:
        user_input:str = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "help":
            print(help())
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()