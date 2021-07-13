from DnaData import parser_seq, delete_seq_by_name

class Del:
    def execute(self,command_arg):
        try:
            dna_data = parser_seq(command_arg[0])
            name = dna_data[0]
            sequence = dna_data[1]
            print("Do you really want to delete {}: {}? Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.".format(name,sequence))
            res=input(str("confirm >>>"))
            while res not in ["y","Y","n","N"]:
                print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
                res = input(str("confirm >>>"))
            if(res=="y" or res=="Y"):
                delete_seq_by_name(name)
        except:
            print("input not valid")
