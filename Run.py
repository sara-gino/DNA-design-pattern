
from DnaData import get_db
from Parser import Parser
from batch_commands.batch_commands import run_command


class Run:
    def __init__(self,name_batch):
        self.__name_batch=name_batch[1:]
    def execute(self):
        data = get_db()
        try:
            for command in data["batch"][self.__name_batch]:
                parser = Parser(command)
                command = parser.get_command()
                arg_command = parser.get_command_arg()
                run_command(command,arg_command)
        except:
            print("batch {} not exist".format(self.__name_batch))


