from DnaData import parser_seq, updete_change

class Slice:
    def execute(self,command_arg):
        try:
            dna_data = parser_seq(command_arg[0])
            name = dna_data[0]
            sequence = dna_data[1]
            sequence=sequence[int(command_arg[1]):int(command_arg[2])]
            updete_change(command_arg, name, "_s", sequence, 3)
        except:
            print("input not valid")


