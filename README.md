# AirBnB Clone - The Console

## Description

This project is the first step towards building a full web application like AirBnB. The console is a command interpreter to manage objects for the AirBnB(HBnB) project. It can be used to handle and manipulate all the classes used by the application (e.g., User, State, City, Place, etc.).

# Airbnb Clone

The Airbnb Clone project is a comprehensive approach to mirroring the functionality of the Airbnb platform. It includes a custom command-line interpreter for data management, and the ability to manage objects like users, places, states, cities, amenities, and reviews. This project is part of our training program to understand higher-level programming and full-stack development.

## Command Interpreter Description

The command interpreter is designed to manage the whole application's functionality from the command line, such as:

- Create a new object (ex: a new User or a new Place).
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.).
- Update attributes of an object.
- Destroy an object.

## How to Start It

To start the console, navigate to the project directory and run the `console.py` file with python3:

```bash
cd AirBnB_clone
./console.py
How to Use It
The console works both in interactive mode and non-interactive mode, similar to a Unix shell.

Interactive Mode:
Run the console (./console.py or python3 console.py) and type commands directly into the prompt.

Example:

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
Non-Interactive Mode:
Echo the command and pipe it into the console.py file:

Example:

bash
Copy code
$ echo "help" | ./console.py
Examples
Here are some example commands you can run in the console:

create User: Creates a new instance of User.
show User 1234-1234-1234: Shows the details of the user with id 1234-1234-1234.
destroy User 1234-1234-1234: Deletes the user with id 1234-1234-1234.
all: Displays all objects.
update User 1234-1234-1234 email "a@example.com": Updates the User's email attribute.
                     