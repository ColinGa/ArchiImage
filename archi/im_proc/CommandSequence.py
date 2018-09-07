from ..dal import DataLoader

class Sequence:
    """ Classe conteneur d'une liste de commandes. """

    def __init__(self, list_commands):
        self.list_commands = list_commands

    def add_command(self, command):
        self.list_commands.append(command)
    
    def add_command_at(self, command, idx):
        self.list_commands.insert(idx, command)

    def remove_command(self, command):
        self.list_commands.remove(command)

    def remove_command_at(self, idx):
        return self.list_commands.pop(idx)

    def remove_last(self):
        return self.list_commands.pop()

    def save(self, directory, filename):
        DataLoader.save_sequence(directory, filename, self)

    def __eq__(self, other):
        try:
            for command, other_command in zip(self.list_commands, other.list_commands):
                if command != other_command:
                    return False
            return True
        except AttributeError:
            return False

    def __getitem__(self, key):
        if self.list_commands:
            return self.list_commands[key]
        else:
            print("Impossible d'utiliser l'indexation quand les images ne sont\
                     pas en mémoire")