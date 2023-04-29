from cli import CLI
from container_controller import ContainerController

COMMANDS_INFO = """
    add <key> [key, …] – add one or more elements to the container (if the element is already in there then don’t add)
    remove <key> – delete key from container
    find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is
    list – print all elements of container
    grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is
    save/load – save container to file/load container from file
    switch – switches to another user
"""

def print_possible_commands():
    print("Possible Commands:", COMMANDS_INFO)

def start_application():
    print(f"""
    Container of Unique Elements CLI Program.
    
        Possible Commands: {COMMANDS_INFO} 
    """)

    controller = ContainerController()
    cli = CLI()

    possible_commands = ["add", "remove", "find", "list", "grep", "save", "load", "switch"]
    for command in possible_commands:
        cli.add_command(command, getattr(controller, command))
    cli.add_command("help", print_possible_commands)


    try:
        while True:
            cli.parse_command()
    except KeyboardInterrupt:
        print("")
        controller._ask_for_save()
        print("\nSee You Later!")


def main():
    #try:
    start_application()
    #except KeyboardInterrupt:
    #    print("\nSee You Later!")

if __name__ == "__main__":
    main()
