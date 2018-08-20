""" Module composée de classes implémentant le design pattern Command pour
    structurer une chaine de traitement dans un projet d'analyse d'image.
    Ce module a pour but d'être étendu pour que chaque projet puisse implé-
    menter uniquement ses traitements nécessaires.
"""

import os
import abc
import skimage as sk; from skimage import io


class Image(abc.ABC):
    """ Classe Receiver du design pattern Command """

    def __init__(self, image):
        """ Paramètres :
            - image : numpy array (n*m) ou (n*m*k) représentant une image 
        """
        self.image = image

    def save(self, directory, name):
        """ Méthode de sauvegarde l'image.
            Paramètres :
            - directory : chemin relatif au répertoire cible
            - name : nom du fichier voulu (avec l'extension)
        """
        try:
            path = os.path.join(directory, name)
            sk.io.imsave(path, self.image)
        except Exception as e:
            print(e)

    @abc.abstractmethod
    def label(self):
        """ Méthode pour affecter un label/une classe de référence à une image.
            A implémenter dans une classe fille.
        """
        pass
    
    @abc.abstractmethod
    def display(self):
        """ Méthode d'affichage de l'image.
            A implémenter dans une classe fille.
        """
        pass


class ImageCommand(abc.ABC):
    """ Classe CommandInterface du design pattern Command """

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
    """ Classe ConcreteCommand du design pattern Command.
        Encapsule la méthode save de la classe Image
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


class ImageInvoker:
    """ Classe Invoker du design pattern Command """

    def __init__(self):
        self.history = []

    def store_and_execute(self, command):
        """ Méthode d'historisation et d'exécution des différentes commandes.
            Paramètres :
            - command : instance d'une des classes filles de la classe ImageCommand
        """
        command.execute()
        self.history.append(command)

    def undo_last(self):
        """ Méthode d'annulation de la dernière commande (le dernier traitement)
            effectuée sur l'Image
        """
        if self.history:
            self.history.pop().undo()