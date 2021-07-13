from DnaData import parser_seq, updete_change

class Replace:
    def execute(self,command_arg):
        try:
            dna_data = parser_seq(command_arg[0])
            name = dna_data[0]
            sequence = dna_data[1]
            i=1
            while i<len(command_arg) and command_arg[i]!=":":
                sequence=sequence[:int(command_arg[i])]+command_arg[i+1]+sequence[int(command_arg[i])+1:]
                i+=2
            updete_change(command_arg, name, "_r", sequence,i)
        except:
            print("input not valid")


