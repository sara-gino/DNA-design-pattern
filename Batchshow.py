from DnaData import get_db


class Batchshow:
    def __init__(self,name_batch):
        self.__name_batch=name_batch[0][1:]
    def execute(self):
        data = get_db()
        try:
            print(data["batch"][self.__name_batch])
        except:
            print("batch {} not exist".format(self.__name_batch))