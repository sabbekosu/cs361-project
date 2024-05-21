import random
import os
import time

# List of sample names
names = ["Aragorn", "Legolas", "Gimli", "Frodo", "Sam", "Gandalf", "Boromir", "Arwen", "Galadriel", "Elrond"]

# Categories and their corresponding names
categories = {
    "Fantasy": ["Aragorn", "Legolas", "Gimli", "Gandalf", "Galadriel"],
    "Hobbit": ["Frodo", "Sam", "Bilbo", "Merry", "Pippin"],
    "Elf": ["Legolas", "Arwen", "Galadriel", "Elrond", "Thranduil"]
}

last_content = ''

def generate_random_name(category=None):
    if category and category in categories:
        return random.choice(categories[category]).strip()
    else:
        return random.choice(names).strip()

def main():
    while True:
        if os.path.exists('request_response.txt'):
            with open('request_response.txt', 'r') as file:
                content = file.read().strip()
                if content != last_content:
                    time.sleep(1)
                    #print(f"Received content: {content}")  # Debugging statement

            if content.lower() == "stop":
                # Clear the file and stop the service
                with open('request_response.txt', 'w') as file:
                    file.write('')
                #print("Stopping microservice.")
                break

            if content.startswith('Category:'):
                #print(f"Received request: {content}")  # Debugging statement
                category = content.split(': ')[1] if ': ' in content else None
                name = generate_random_name(category)
                with open('request_response.txt', 'w') as response_file:
                    response_file.write(f'Generated Name: {name}')
                    #print(f"Wrote response: {name}")  # Debugging statement

        # Sleep to prevent the loop from running too fast
        time.sleep(1)

if __name__ == "__main__":
    main()
