#!/usr/bin/python3
""" This module contains the commandline for AirBnB clone """
import cmd


class HBNBCommand(cmd.Cmd):
    """ class cmd """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """  type <quit> to exit the program """
        return True

    def do_EOF(self, args):
        """ type <EOF>  to exit the program """
        return True

    def emptyline(self):
        """ Ignore empty line, spaces and ENTER """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
