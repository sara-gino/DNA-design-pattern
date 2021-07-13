from DnaData import parser_seq, seq_to_find_or_count, get_count_sub_str_in_seq
class Count:
    def execute(self,command_arg):
        dna_data=parser_seq(command_arg[0])
        seq=dna_data[1]
        seq_to_count=seq_to_find_or_count(command_arg[1])
        print(get_count_sub_str_in_seq(seq,seq_to_count))


