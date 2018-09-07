import types

import numpy as np

from ..dal import DataLoader
from .CommandSequence import Sequence
from .ImageCommand import DummyCommand
from .Image import Image


class ImageCollection:
    """ Classe conteneur d'une liste d'Image."""

    def __init__(self, directory, load_in_memory):
        self.observers = []
        self.current_image = None
        self.directory = directory
        if load_in_memory:
            self.list_images = [Image(im) for im in DataLoader.load_images_as_list(directory)]
            self.in_memory = True
        else:
            self.list_images = (Image(im) for im in DataLoader.load_images_as_generator(directory))
            self.in_memory = False
        
    def save(self, directory, name):
        DataLoader.save_image_collection(self, directory, name)

    def register_observer(self, obs):
        self.observers.append(obs)

    def unregister_observer(self, obs):
        self.observers.remove(obs)

    def unregister_all_observer(self):
        self.observers.clear()

    def _notify_observers(self, image, **kwargs):
        for obs in self.observers:
            obs.update(image, **kwargs)

    def __eq__(self, other):
        # L'ordre importe dans l'égalité ici
        for im, im_ref in zip(self.list_images, other.list_images):
            res = (im == im_ref)
            if not res:
                return False
        return True

    def __getitem__(self, key):
        if self.in_memory:
            return self.list_images[key]
        else:
            print("Impossible d'utiliser l'indexation quand les images ne sont\
                     pas en mémoire")


class ImageCollectionProcessed(ImageCollection):
    """ Classe conteneur d'une liste d'Image et d'une Sequence. """

    def __init__(self, directory, load_in_memory, sequence=None):
        super().__init__(directory, load_in_memory)
        self.sequence = sequence if sequence else Sequence([])

    def store(self, command):
        self.sequence.add_command(command)

    def store_and_execute(self, command, **kwargs):
        command.execute()
        self.sequence.add_command(command)
        self._notify_observers(self.current_image, **kwargs)

    def execute_last(self, **kwargs):
        self.sequence[-1].execute()
        self._notify_observers(self.current_image, **kwargs)

    def execute_all_command_one_image(self, **kwargs):
        for command in self.sequence:
            command.execute()
            self._notify_observers(self.current_image, **kwargs)
    
    def execute_all_command_all_images(self, **kwargs):
        for image in self.list_images:
            self.current_image = image
            for command in self.sequence:
                command.image = image
                command.execute()
                # Une seule méthode d'affichage ici pour toutes les commandes
                self._notify_observers(image, **kwargs)

    def undo_last(self, **kwargs):
        """ Méthode d'annulation de la dernière commande de la séquence. """
        if self.sequence.list_commands:
            self.sequence[-1].undo()
            self._notify_observers(self.current_image, **kwargs)

    def undo(self, idx, **kwargs):
        self.sequence[idx].undo()
        self._notify_observers(self.current_image, **kwargs)

    def redo(self):
        pass