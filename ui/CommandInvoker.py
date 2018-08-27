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
