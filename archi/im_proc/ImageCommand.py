""" 
    Module contenant les classes CommandInterface (ImageCommand) et Concrete-
    Command du design pattern Command. Les classes héritant d'ImageCommand doi-
    vent être utilisées via la classe CommandInvoker.
"""

import os
import abc
import sys
import inspect

def setup_dict_ImageCommand_classes():
    dict_classes = {}
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for elem in clsmembers:
        dict_classes[elem[0]] = elem[1]
    return dict_classes


class ImageCommand(abc.ABC):
    """ Classe CommandInterface du design pattern Command. """

    def __init__(self, image=None):
        """ 
            Paramètres :
            - image : instance de la classe Image (de ce module)
        """
        self.image = image
        self.class_name = "ImageCommand"

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value
        self.previous_state = value.pixels if self.__image else None

    @abc.abstractmethod
    def execute(self):
        """ 
            Méthode d'exécution de la commande.
            A implémenter dans une classe fille.
        """
        pass

    @abc.abstractmethod
    def undo(self):
        """ 
            Méthode d'annulation la commande.
            A implémenter dans une classe fille.
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def decode(json_map):
        pass

    def __eq__(self, other):
        try:
            for key in self.__dict__.keys():
                if key != "_ImageCommand__image" and key != "previous_state":
                    if self.__dict__[key] != other.__dict__[key]:
                        return False
            return True
        except (AttributeError, KeyError):
            return False
            


class DummyCommand(ImageCommand):
    """ Classe command de test. """

    def __init__(self, image=None, param_test=None):
        super().__init__(image)
        self.param_test = param_test
        self.class_name = "DummyCommand"

    def execute(self):
        self.image.preuve_dummy_command = "J'existe !"

    def undo(self):
        self.image.preuve_dummy_command = "J'existe plus !"

    @staticmethod
    def decode(json_map):
        return DummyCommand()



class ConvertToGrayCommand(ImageCommand):
    """ Classe command de conversion image rgb vers image niveaux de gris. """

    def __init__(self, image=None):
        super().__init__(image)
        self.class_name = "ConvertToGrayCommand"

    def execute(self):
        self.image.convert_to_gray()

    def undo(self):
        self.image.pixels = self.previous_state

    @staticmethod
    def decode(json_map):
        return ConvertToGrayCommand()