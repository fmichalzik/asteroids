# asteroids
I'am going to build a simple video game, based on the classic Asteroids.

The learning goals of this project are:
- Working on multi-file Python projects
- Show you a real-world use case for object-oriented programming
- To have a fun building a project!

Setup:
We are going to be using pygame and a virtual environment to develop our game.
Pygame is a module for developing games using Python. It provides simple functions and methods for us to easily draw images within a GUI window and handle user input.

Virtual Environment (venv):
Virtual environments are Python's way to keep dependencies (e.g. the pygame module) separate from other projects on our machine.

Installation protocol:

Create a virtual environment at the top level of the project directory:
- $ apt install python3.12-venv
- $ python3 -m venv venv

Activate the virtual environment:
- $ source venv/bin/activate

Create a file called requirements.txt in the top level of the project directory with the following contents:
- pygame==2.6.1
This tells Python that this project requires pygame version 2.6.1.

Install the requirements:
- $ pip install -r requirements.txt