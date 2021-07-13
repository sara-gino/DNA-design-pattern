from DnaData import get_db


class Batchlist:
    def __init__(self):
        self.__list_all_batch=[]
    def execute(self):
        data = get_db()
        try:
            for name in data["batch"]:
                self.__list_all_batch.append(name)
            print(self.__list_all_batch)
        except:
            print("no such batch")
