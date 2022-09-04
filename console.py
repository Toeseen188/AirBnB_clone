#!/usr/bin/python3
""" This module contains the commandline for AirBnB clone """
import cmd
from models import storage
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class cmd """
    prompt = '(hbnb) '
    class_list = {"BaseModel"}

    def do_quit(self, args):
        """  type <quit> to exit the program """
        return True

    def do_EOF(self, args):
        """ type <EOF>  to exit the program """
        return True

    def emptyline(self):
        """ Ignore empty line, spaces and ENTER """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel.
        Exceptions:
            =>If the class name is missing, print ** class name missing **
                (ex: $ create)
            =>If the class name doesn’t exist, print ** class doesn't exist **
                (ex: $ create MyModel)
        """

        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if arg[0] not in self.class_list:
                raise NameError

            new_inst = eval(arg[0])()
            new_inst.save()
            print(new_inst.id)

        except NameError:
            print("** class doesn't exist **")

        except SyntaxError:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
