An airbnb clone

Description
===============
AirBnB is a complete web application, integrating database storage, backend API, and front-end interface in a clone of AirBnB.

This team project is a part of the ALX program.
It represents the first step towards building a full web application.

The first step consists of:
    1. a custom command_line interface for data management,
    2. and the base classes for the storage of this data.


Usage
=======
The console works both in interactive mode and non-interactive mode, much like a unix shell. It prints a prompt (hbnb) and waits for the user for input.

interactive mode
---------------------
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

non-interactive mode
------------------------
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


Testing
==========
Unittests for the AirBnB project are defined in the test folder. To run the entire test suite simultaneously execute the following command:

$ python3 unittest -m discover tests

Alternatively, you can specify a single test file to run at a time:

$ python3 unittest -m tests/test_console.py