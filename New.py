from DnaData import create


class New:
    def execute(self,command_arg):
        sequence = command_arg[0]
        try:
            name = command_arg[1][1:]
        except:
            name="seq"
        create( name,sequence)