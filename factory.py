from batch_commands.Batchload import Batchload
from batch_commands.Batchsave import Batchsave
from batch_commands.Batchshow import Batchshow
from batch_commands.batchlist import Batchlist
from management_commands.Save import Save
from management_commands.Del import Del
from creation_commands.Dup import Dup
from creation_commands.Load import Load
from creation_commands.New import New
from manipulation_commands.Replace import Replace
from manipulation_commands.Slice import Slice
from sequence_analysis_commands.Find import Find
from sequence_analysis_commands.Findall import Findall
from sequence_analysis_commands.Len import Len
from sequence_analysis_commands.Count import Count

class Commands():
    def __init__(self):
        self. creation_commands = {
            "new": New,
            "load": Load,
            "dup": Dup,
        }
        self.manipulation_commands = {
            "slice": Slice,
            "replace":Replace
        }
        self.management_commands={
            "del":Del,
            "save":Save
        }

        self.sequence_analysis_commands= {
            "len": Len,
            "find":Find,
            "count":Count,
            "findall":Findall
        }

        self.batch_commands={
            "batchlist":Batchlist,
            "batchshow":Batchshow,
            "batchsave":Batchsave,
            "batchload":Batchload
        }
    def get_creation_command(self, command):
        return self.creation_commands[command]()

    def get_manipulation_command(self, command):
        return self.manipulation_commands[command]()

    def get_management_command(self, command):
        return self.management_commands[command]()
    def get_sequence_analysis_commands(self,command):
        return self.sequence_analysis_commands[command]()

    def get_batch_commands(self,command,name_batch=None):
        if name_batch:
            return self.batch_commands[command](name_batch)
        else:
            return self.batch_commands[command]()