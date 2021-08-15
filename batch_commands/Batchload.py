from DnaData import get_db, write_db

class Batchload:
    def __init__(self, arg_command):
        self.__name_file = arg_command[0]
        try:
            self.__name_batch = arg_command[2][1:]
        except:
            ind=self.__name_file.index(".")
            self.__name_batch = self.__name_file[:ind]

    def execute(self):
        try:
            with open(self.__name_file, 'r') as f:
                batch =  f.read().splitlines()
                data = get_db()
                data["batch"][self.__name_batch]=batch
                write_db(data)
        except:
            print("file not exist")

