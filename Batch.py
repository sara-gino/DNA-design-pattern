from DnaData import get_db, write_db
from Parser import Parser
from batch_commands.batch_commands import run_command

class Batch:
    def __init__(self,name_batch):
        self.__name_batch=name_batch
        self.__commands=[]

    def execute(self):
        input_command = input(str("> cmd >>>"))
        parser = Parser(input_command)
        command = parser.get_command()
        arg_command = parser.get_command_arg()
        while (command != "end"):
            run_command(command, arg_command)
            self.__commands.append(input_command)
            input_command = input(str("> cmd >>>"))
            parser = Parser(input_command)
            command = parser.get_command()
            arg_command = parser.get_command_arg()
        data=get_db()
        try:
            data["batch"][self.__name_batch]+=self.__commands
        except:
            data["batch"][self.__name_batch]=self.__commands
        write_db(data)