from commands import RedisCommands
from Persistence import Persistence
from config import PERSISTENCE_FILE

def main():
    db_commands = RedisCommands()
    persistence = Persistence(db_commands.db, PERSISTENCE_FILE)

    # Load data from persistence file
    persistence.load_data()

    ascii_art = r"""
     
  _____          _ _             
 |  __ \        | (_)            
 | |__) |___  __| |_ _ __  _   _ 
 |  _  // _ \/ _` | | '_ \| | | |
 | | \ \  __/ (_| | | |_) | |_| |
 |_|  \_\___|\__,_|_| .__/ \__, |
                    | |     __/ |
                    |_|    |___/ 
"""
    print(ascii_art)
    print("Welcome to redipy - a lightweight, Redis-like key-value store implemented in Python")
    print("Type 'EXIT' to quit the session.")

    while True:
        command_input = input(">> ").strip().split()
        if not command_input:
            continue

        command = command_input[0].upper()

        if command == "EXIT":
            # Save data before exiting
            persistence.save_data()
            print("Goodbye!")
            break

        response = db_commands.handle_command(command, *command_input[1:])
        print(response)

if __name__ == "__main__":
    main()
