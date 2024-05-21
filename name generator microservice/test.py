import subprocess
import time

def write_request_file(content):
    with open('request_response.txt', 'w') as file:
        file.write(content)

def read_response_file():
    with open('request_response.txt', 'r') as file:
        response = file.read()
    return response.strip()

def clear_file_contents(filename):
    with open(filename, 'w') as file:
        file.write('')

def main():
    # Clear any existing files
    clear_file_contents('request_response.txt')

    # Start the microservice
    microservice_process = subprocess.Popen(['python', 'name_generator.py'])

    # Give the microservice a moment to start
    time.sleep(2)

    # Make a request to the microservice
    write_request_file('Category: Hobbit')
    
    # Give the microservice a moment to process the request
    time.sleep(2)

    # Read the response
    response = read_response_file()
    print(response)  # Output should be something like "Generated Name: Aragorn"

    # Send stop signal to the microservice
    write_request_file('stop')

    # Give the microservice a moment to process the stop request
    time.sleep(2)

    # Wait for the microservice to terminate
    microservice_process.wait()

    # Clean up
    clear_file_contents('request_response.txt')

if __name__ == "__main__":
    main()
