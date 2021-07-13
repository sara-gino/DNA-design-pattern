from DnaData import get_sequence_by_id


class Len:
    def execute(self,command_arg):
        seq=get_sequence_by_id(command_arg[0][1:])
        try:
            print(len(seq))
        except:
            print("id seq {} not exist ".format(command_arg[0][1:]))
