import os
import numpy as np
import skimage as sk; from skimage import io, color

from ..dal.DataLoader import DataLoader

class Image():
    """ 
        Classe conteneur des valeurs des pixels et définissant les traitements
        à effectuer sur ceux-ci. 
    """

    def __init__(self, image):
        """ 
            Paramètres :
            - image : numpy array (n*m) ou (n*m*k) représentant une image 
        """
        self.pixels = image

    def save(self, directory, name):
        """ Méthode de sauvegarde l'image. """
        DataLoader.save_image(self.pixels, directory, name)

    def set_label(self, label):
        """ Méthode pour affecter un label de référence à une image. """
        self.label = label
    
    def convert_to_gray(self):
        self.pixels = sk.color.rgb2gray(self.pixels)

    def __eq__(self, other):
        if np.all(self.pixels == other.pixels):
            return True
        else:
            return False