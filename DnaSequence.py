def is_valid_dna(string):
    list = ["A", "G", "T", "C"]
    for c in string:
        if c not in list:
            return False
    return True

class DnaSequence:
    def __init__(self,string):
        if is_valid_dna(string):
            self.dna_sequence=string
        else:
            print("ValueError: not valid sequence")
            return

    def insert(self,value,index):
        self.dna_sequence=self.dna_sequence[:index]+value+self.dna_sequence[index:]

    def assignment(self,dna_sequence):
        if is_valid_dna(dna_sequence):
            self.dna_sequence=dna_sequence
        else:
            raise ValueError

    def __str__(self):
        if(len(self.dna_sequence)>40):
            print(self.dna_sequence)
            return str("{}...{}".format(self.dna_sequence[:32],self.dna_sequence[-3:]))
        return str(self.dna_sequence)

    def __eq__(self,dna_sequence):
        return self.dna_sequence==dna_sequence

    def __ne__(self,dna_sequence):
        return self.dna_sequence != dna_sequence

    def __len__(self):
        return len(self.dna_sequence)

    def __getitem__(self, index):
        return self.dna_sequence[index]

    def __setitem__(self, index,item):
        if(is_valid_dna(item)):
            self.dna_sequence=self.dna_sequence[:index]+self.dna_sequence[index+1:]
            self.insert(item,index)
        else:
            raise ValueError
