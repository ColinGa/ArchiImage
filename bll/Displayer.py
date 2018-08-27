import matplotlib.pyplot as plt


class Displayer:
    """ Com """
    
    __instance = None

    def __new__(cls):
        """ Implémentation simple d'un Singleton """
        if Displayer.__instance is None:
            Displayer.__instance = object.__new__(cls)
        return Displayer.__instance

