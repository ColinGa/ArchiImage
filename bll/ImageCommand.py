""" 
    Module contenant les classes CommandInterface (ImageCommand) et Concrete-
    Command du design pattern Command. Les classes héritant d'ImageCommand doi-
    vent être utilisées via la classe CommandInvoker.
"""

import os
import abc


class ImageCommand(abc.ABC):
    """ Classe CommandInterface du design pattern Command. """

    def __init__(self, image):
        """ Paramètres :
            - image : instance de la classe Image (de ce module)
        """
        self.image = image
        self.previous_state = image.image

    @abc.abstractmethod
    def execute(self):
        """ Méthode d'exécution de la commande.
            A implémenter dans une classe fille.
        """
        pass

    @abc.abstractmethod
    def undo(self):
        """ Méthode d'annulation la commande.
            A implémenter dans une classe fille.
        """
        pass


class SaveCommand(ImageCommand):
    """ Exemple d'implémentation de la classe ConcreteCommand du design pattern 
        Command. Encapsule la méthode save de la classe Image.
    """

    def __init__(self, image, directory, name):
        """ Paramètres :
            - image : instance de la classe Image (de ce module)
            - directory : chemin relatif au répertoire cible
            - name : nom du fichier voulu (avec l'extension)
        """
        super().__init__(image)
        self.directory = directory
        self.name = name

    def execute(self):
        """ Méthode d'exécution de la commande.
            Sauvegarde l'image dans le dossier voulu.
        """
        self.image.save(directory=self.directory, name=self.name)

    def undo(self):
        """ Méthode d'annulation la commande.
            Supprime l'image sauvegardée précédemment.
        """
        os.remove(os.path.join(self.directory, self.name))