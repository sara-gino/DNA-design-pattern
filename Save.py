from DnaData import parser_seq, save_seq_or_batch_in_file

class Save():
    def execute(self,command_arg):
        try:
            dna_data = parser_seq(command_arg[0])
            name = dna_data[0]
            sequence = dna_data[1]
            if(len(command_arg)==1):
                name_file=name+".rawdna"+".txt"
            else:
                name_file=command_arg[1]
            save_seq_or_batch_in_file(name_file,sequence)
        except:
            print("input not valid")
