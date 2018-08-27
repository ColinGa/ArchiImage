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
        except FileNotFoundError:
            os.makedirs(directory)
            sk.io.imsave(path, self.image)

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