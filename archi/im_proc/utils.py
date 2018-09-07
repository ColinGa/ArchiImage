import skimage as sk; from skimage import util
from functools import wraps


def choose_image_type(image_type):
    """ 
        Fonction renvoyant la fonction de conversion de type de données 
        demandées.
        Paramètres :
        - image_type : option parmi ["ubyte", "float", "uint", "int", "bool"], 
        par défaut "ubyte" est utilisé.
    """
    dict_types = {
        "ubyte": sk.util.img_as_ubyte,  # [0-255]
        "float": sk.util.img_as_float,  # [0-1]
        "uint": sk.util.img_as_uint,    # [0-65535]
        "int": sk.util.img_as_int,      # [-255-255]
        "bool": sk.util.img_as_bool    # [False, True]
    }  
    return dict_types[image_type, "ubyte"]

def convert_image_type(imtype="ubyte"):
    """ 
        Décorateur de conversion du type de données d'une image.
        Paramètres :
        - imtype : option parmi ["ubyte", "float", "uint", "int", "bool"]
    """
    def wrapper(func):
        def wrapped(image, **kwargs):
            converter = choose_image_type(imtype)
            image = converter(image)
            return func(image, **kwargs)
        return wrapped
    return wrapper