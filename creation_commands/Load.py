from DnaData import create


class Load:
    def execute(self, command_arg):
        try:
            with open(command_arg[0], 'r') as f:
                sequence = f.read()
        except:
            print("file not exist")
            return
        try:
            name = command_arg[1][1:]
        except:
            name = "seq"
        create(name,sequence)
