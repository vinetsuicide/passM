import random
import string
import pyfiglet  
from termcolor import colored  

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password(filename, password):
    with open(filename, 'a') as file:
        file.write(f"{password}\n")

def list_passwords(filename):
    with open(filename, 'r') as file:
        passwords = file.readlines()
        for password in passwords:
            print(password.strip())

def main():
    
    passm_art = pyfiglet.figlet_format("passM", font="slant")

    print(colored(passm_art, color="blue"))
    print(colored("Password Generator\n", color="green"))

    while True:
        action = input(colored("Choose an action (gen/list/quit): ", color="yellow")).strip().lower()

        if action == "gen":
            length = int(input(colored("Enter the password length: ", color="yellow")))
            generated_password = generate_password(length)
            print(colored(f"Generated Password: {generated_password}\n", color="cyan"))
            save_password('passwords.txt', generated_password)
        elif action == "list":
            print(colored("\nList of Passwords:", color="cyan"))
            list_passwords('passwords.txt')
            print()
        elif action == "quit":
            print(colored("Goodbye!", color="green"))
            break
        else:
            print(colored("Invalid choice. Please enter 'gen', 'list', or 'quit'.", color="red"))

if __name__ == "__main__":
    main()

