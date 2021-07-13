
from DnaData import parser_seq, valid_name, create


class Dup:
    def execute(self, command_arg):
        try:
            nda_data=parser_seq(command_arg[0])
            name = valid_name(nda_data[0],"_")
            create(name,nda_data[1])
        except:
            print("input not valid")




