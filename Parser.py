
class Parser:

    def __init__(self,command):
        pars_command= lambda command:[i for i in  command.split(' ')]
        command=pars_command(command)
        self.__command=command[0]
        self.__command_arg=command[1:]

    def get_command(self):
        return  self.__command

    def get_command_arg(self):
        return self.__command_arg