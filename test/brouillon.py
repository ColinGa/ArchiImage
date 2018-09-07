import itertools as it
import types
import json
import inspect
import sys

def setup_dict_ImageCommand_classes():
    dict_classes = {}
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for elem in clsmembers:
        dict_classes[elem[0]] = elem[1]
    return dict_classes

class B:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.class_name = "B"

    @staticmethod
    def decode(json_map):
        return B(json_map["a"], json_map["b"], json_map["c"])

    def __str__(self):
        return " : ".join([str(self.a), str(self.b), str(self.c)])

    def __repr__(self):
        return " : ".join([str(self.a), str(self.b), str(self.c)])


class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.class_name = "A"

    def coucou(self):
        print("coucou")
    
    @staticmethod
    def decode(json_map):
        return A(json_map["a"], json_map["b"])

    def __str__(self):
        return " : ".join([str(self.a), str(self.b)])

    def __repr__(self):
        return " : ".join([str(self.a), str(self.b)])

dict_test = setup_dict_ImageCommand_classes()
dict_classes = dict_test#{"B": B, "A": A}

class ABList:

    def __init__(self, liste):
        self.liste = liste
        self.coucou = "COUCOUCOUCOU"
        self.test = A(444, 666)
        self.test2 = B("sup", 32, 8)
        self.class_name = "ABList"

    def __str__(self):
        return " ; ".join([str(self.liste), str(self.coucou), 
                            str(self.test), str(self.test2)])


class AlistEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (A, B)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class ABlistDecoder(json.JSONDecoder):
    
    def decode(self, json_string):
        obj = super(ABlistDecoder, self).decode(json_string)
        ABlist_obj = ABList([dict_classes[x["class_name"]].decode(x) for x in obj["liste"]])
        return ABlist_obj

AListinst = ABList([A(42, 42), B(2, 4, "cc"), B(4, 2, "Plop"), A(42, 2)])
with open("test_json.json", "w", newline="\n") as jsonfile:
    json.dump(AListinst.__dict__, fp=jsonfile, indent=4, cls=AlistEncoder)

with open("test_json.json", "r") as jsonfile:
    res = json.load(jsonfile, cls=ABlistDecoder)

print(type(res))
print(res)
