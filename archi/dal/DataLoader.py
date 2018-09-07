import os
import skimage as sk; from skimage import io
import json

from ..im_proc.ImageCommand import setup_dict_ImageCommand_classes, ImageCommand
from ..im_proc.CommandSequence import Sequence

class CommandSequenceEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, ImageCommand):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class CommandSequenceDecoder(json.JSONDecoder):
    
    def decode(self, json_string):
        obj = super(CommandSequenceDecoder, self).decode(json_string)
        seq = Sequence([DataLoader.dict_commands[x["class_name"]].decode(x) 
                            for x in obj["list_commands"]])
        return seq


class DataLoader:
    """ Classe contenant toutes les méthodes d'accès aux données. """

    dict_commands = setup_dict_ImageCommand_classes() 

    @staticmethod
    def load_image(path, keep_alpha=False):
        try:
            im = sk.io.imread(path)
            if not keep_alpha and len(im.shape) == 3:
                im = im[:,:,:3]
            return im
        except OSError:
            pass

    @staticmethod
    def load_images_as_generator(directory, **kwargs):
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                image = DataLoader.load_image(path, **kwargs)
                yield image
                
    @staticmethod
    def load_images_as_list(directory, **kwargs):
        list_images = []
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                image = DataLoader.load_image(path, **kwargs)
                if image is not None:
                    list_images.append(image)
                    print("Loaded :", filename)
        return list_images

    @staticmethod
    def load_sequence(path):
        with open(path, "r") as jsonfile:
            res = json.load(jsonfile, cls=CommandSequenceDecoder)
        return res

    @staticmethod
    def save_images_list(images_list, directory, list_name):
        for j, image in enumerate(images_list):
            current_name = "".join((list_name, "_", str(j), ".png"))
            path = os.path.join(directory, current_name)
            sk.io.imsave(path, image)

    @staticmethod
    def save_image(pixels, directory, filename):
        path = os.path.join(directory, filename)
        sk.io.imsave(path, pixels)

    @staticmethod
    def save_sequence(directory, filename, sequence):
        path = os.path.join(directory, filename)
        with open(path, "w") as jsonfile:
            json.dump(sequence.__dict__, fp=jsonfile, indent=4, 
                            cls=CommandSequenceEncoder)
