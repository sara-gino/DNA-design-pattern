from DnaData import get_db, save_seq_or_batch_in_file


class Batchsave:
    def __init__(self,arg_command):
        self.__name_batch = arg_command[0][1:]
        try:
            self.__name_file=arg_command[1]
        except:
            self.__name_file=self.__name_batch+".dnabatch"+".txt"
    def execute(self):
        data = get_db()
        try:
            for command in data["batch"][self.__name_batch]:
                save_seq_or_batch_in_file(self.__name_file, command)
        except:
            print("batch {} not exist".format(self.__name_batch))

