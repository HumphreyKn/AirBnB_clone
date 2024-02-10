#!/usr/bin/python3
"""The command line Interpreter Modue"""

import cmd


class HBNBCommand(cmd.Cmd):
    """A command interpreter for HBNB"""

    prompt = '(hbnb) '

    # define the method to exit the program
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # define the method to handle EOF (end-of-file) inpu
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    # define the method to handle empty line input
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
