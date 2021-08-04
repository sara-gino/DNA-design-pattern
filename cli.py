from DnaData import get_db, write_db
from Parser import Parser
from run_command import run_command

if(__name__=="__main__"):
    data = get_db()
    write_db(data)
    while True:
        input_command = input(str("> cmd >>>"))
        parser = Parser(input_command)
        command = parser.get_command()
        arg_command=parser.get_command_arg()
        run_command(command,arg_command)
