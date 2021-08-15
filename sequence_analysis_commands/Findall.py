from DnaData import parser_seq, get_count_sub_str_in_seq, seq_to_find_or_count, get_index_sub_seq


class Findall:

    def execute(self,command_arg):
        dna_data = parser_seq(command_arg[0])
        seq = dna_data[1]
        seq_findall = seq_to_find_or_count(command_arg[1])
        count=get_count_sub_str_in_seq(seq, seq_findall)
        try:
            for i in range(count):
                ind=get_index_sub_seq(seq, seq_findall)
                seq=seq[:int(ind)-1]+"*"*len(seq_findall)+seq[int(ind) + len(seq_findall)-1:]
                print(ind ,end=" ")
            print("\n")
        except:
            print(count)

