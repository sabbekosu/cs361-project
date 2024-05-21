# Random Name Generator Microservice

## Overview

This microservice generates random names based on specified categories or provides a random name when no category is specified. The interaction with the microservice occurs through a single text file named `request_response.txt`.

## How to Request Data

To request data from the microservice, write the desired category to `request_response.txt`. If no category is specified, a random name will be generated.

### Example Code to Request Data

```python
def write_request_file(category=None):
    with open('request_response.txt', 'w') as file:
        if category:
            file.write(f'Category: {category}')
        else:
            file.write('Category: Any')

# Example usage:
write_request_file(category='Fantasy')
```

## How to Receive Data

To receive the generated name, read the `request_response.txt` file after making the request. The file will contain the generated name.

### Example Code to Receive Data

```python
def read_response_file():
    with open('request_response.txt', 'r') as file:
        response = file.read()
    return response.strip()

# Example usage:
name = read_response_file()
print(name)  # Output should be something like "Generated Name: Aragorn"
```

## How to Stop the Microservice

To stop the microservice, write the word "stop" to the `request_response.txt` file. The microservice will then terminate.

### Example Code to Stop the Microservice

```python
def stop_microservice():
    with open('request_response.txt', 'w') as file:
        file.write('stop')

# Example usage:
stop_microservice()
```

## UML Sequence Diagram

The following UML sequence diagram illustrates the interaction between the test script, the file system, and the microservice:

![UML Sequence Diagram](.\uml_seq.png)

## Mitigation Plan

1. **For which teammate did you implement “Microservice A”?**
   - Teammate: [Teammate Name or Identifier]

2. **What is the current status of the microservice?**
   - The microservice is complete and ready for integration.

3. **If the microservice isn’t done, which parts aren’t done and when will they be done?**
   - N/A

4. **How is your teammate going to access your microservice?**
   - The code is available on GitHub. They should clone the repository and run the code locally.

5. **If your teammate cannot access/call YOUR microservice, what should they do?**
   - Contact me via email or messaging app. I am available from 9 AM to 5 PM on weekdays.

6. **If your teammate cannot access/call your microservice, by when do they need to tell you?**
   - Please inform me at least 48 hours before the deadline.

7. **Is there anything else your teammate needs to know?**
   - Ensure Python 3.6+ is installed. No additional libraries are required.
