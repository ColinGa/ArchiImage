""" Module contenant les classes gérant toutes les méthodes d'affichage. """

import matplotlib.pyplot as plt
import skimage as sk; from skimage import exposure
from cycler import cycler


class Displayer:
    """ 
        Classe contenant les méthodes d'affichage pour les données (images et
        autres). 
    """
    
    def __init__(self):
        self.figure = plt.figure()
        self.auto_close = True
        self.auto_close_delay = 0.5

    def update(self, image, **kwargs):
        self.display_image(image.pixels, **kwargs)
        if self.auto_close:
            plt.pause(self.auto_close_delay)
            plt.clf()
        else: 
            plt.show()

    def set_auto_close(self, ok, delay):
        self.auto_close = ok
        self.auto_close_delay = delay
        
    def display_image(self, image, **kwargs):
        """ 
            Affiche une image dans la figure courante.
            Paramètres :
            - image : numpy array, image à afficher
            - **kwargs : passés à plt.imshow 
            Return : matplotlib.pyplot.figure créée.
        """
        plt.imshow(image, **kwargs)
        
    def display_histogram(self, image, rgb=False, nbins=256):
        """ 
            Affiche l'histogramme par canal d'une image (un canal=une courbe).
            Paramètres :
            - image : numpy array, image dont l'histogramme va être calculé.
            - rgb : booleen, si True les couleurs utilisées pour afficher 
            l'histogramme seront rouge, vert et bleu. Sinon les couleurs par
            défaut de matplotlib sont utilisés. False par défaut.
            - nbins : nombre d'elements en abscisse utilisé pour calculer l'his
            togramme (passé à skimage.exposure.histogram). 256 par défaut.
            Return : matplotlib.pyplot.figure créée.
        """
        if rgb:
            color_cycle = cycler(color=["r", "g", "b"])
        else:
            color_cycle = plt.rcParams["axes.prop_cycle"]
        
        plt.figure()
        ax = plt.gca()
        ax.set_prop_cycle(color_cycle)
        ax.set_title("Histogramme")

        nb_canal = image.shape[-1] if len(image.shape) == 3 else 1
        for i in range(nb_canal):
            if nb_canal == 1:
                histo, bins = sk.exposure.histogram(image, nbins=nbins)    
            else:
                histo, bins = sk.exposure.histogram(image[:,:,i], nbins=nbins)
            lab = "".join(("Dim n°", str(i)))
            plt.plot(bins, histo, label=lab)
        ax.legend()
        plt.show()
