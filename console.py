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

    def do_show(self, args):
        """  Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
        Exceptions:
        => If the class name is missing, print ** class name missing **
            (ex: $ show)
        => If the class name doesn’t exist, print ** class doesn't exist**
            (ex: $ show MyModel)
        => If the id is missing, print ** instance id missing **
            (ex: $ show BaseModel)
        => If the instance of the class name doesn’t exist for the id,
            print ** no instance found **
            (ex: $ show BaseModel 121212)
        """
        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if len(arg) < 2:
                raise IndexError()
            if arg[0] not in self.class_list:
                raise NameError()
            
            obj = storage.all()

            obj_key = arg[0] + "." + arg[1]

            if obj_key in obj:
                print(obj[obj_key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and 
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        Note:
            => If the class name is missing, print ** class name missing **
                (ex: $ destroy)
            => If the class name doesn’t exist, print ** class doesn't exist **
                (ex:$ destroy MyModel)
            => If the id is missing, print ** instance id missing **
                (ex: $ destroy BaseModel)
            => If the instance of the class name doesn’t exist for the
                id, print ** no instance found **
                (ex: $ destroy BaseModel 121212)
        """

        try:
            if not args:
                raise SyntaxError()
            arg = args.split(" ")
            if len(arg) < 2:
                raise IndexError()
            if arg[0] not in self.class_list:
                raise NameError()
            
            obj = storage.all()

            obj_key = arg[0] + "." + arg[1]

            if obj_key in obj:
                del obj[obj_key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")


    def do_all(self, agrs):
        """ Prints all string representation of all instances based
        or not on the class name. 
        Ex: $ all BaseModel or $ all.
        Note:
            => The printed result must be a list of strings
            => If the class name doesn’t exist, print ** class doesn't exist **
            (ex: $ all MyModel)
        """
        obj = storage.all()
        list_= []
        try:
            if args: 
                arg = args.split(" ")
                if arg[0] not in self.class_list:
                    raise NameError()
                for obj_key in obj:
                    cls_name = obj_key.split(".")
                    if cls_name[0] == arg[0]:
                        print("{}".format(list_.append(obj[obj_key])))
            
            for obj_key in obj:
                print("{}".format(list_.append(obj[obj_key])))
        
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
