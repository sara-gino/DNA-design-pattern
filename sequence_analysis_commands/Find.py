from DnaData import parser_seq, seq_to_find_or_count, get_index_sub_seq

class Find:
    def execute(self,command_arg):
        dna_data=parser_seq(command_arg[0])
        seq=dna_data[1]
        seq_find=seq_to_find_or_count(command_arg[1])
        ind=get_index_sub_seq(seq,seq_find)
        print(ind)
