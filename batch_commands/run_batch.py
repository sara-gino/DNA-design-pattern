from factory import Commands

commands = Commands()
creation_commands = [i for i in commands.creation_commands]
manipulation_commands = [i for i in commands.manipulation_commands]
management_commands = [i for i in commands.management_commands]
sequence_analysis_commands = [i for i in commands.sequence_analysis_commands]
batch_commands=[i for i in commands.batch_commands]
def run_command(command, arg_command):
    if command in creation_commands:
        invoker = commands.get_creation_command(command)
        invoker.execute(arg_command)
    elif command in manipulation_commands:
        invoker = commands.get_manipulation_command(command)
        invoker.execute(arg_command)
    elif command in management_commands:
        invoker = commands.get_management_command(command)
        invoker.execute(arg_command)
    elif command in sequence_analysis_commands:
        invoker = commands.get_sequence_analysis_commands(command)
        invoker.execute(arg_command)
    elif command in batch_commands:
        try:
            invoker = commands.get_batch_commands(command, arg_command)
        except:
            invoker = commands.get_batch_commands(command)
        invoker.execute()
    else:
        print("this command not exist")
