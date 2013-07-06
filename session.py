# -*- coding: UTF-8 -*-

import random

class Session:
    def __init__(self):
        self.__id = self.genId(6, 5)
        self.data = {}
    def genId(self, size, blocks):
        alphabet = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP0123456789"
        return "-".join("".join(random.choice(alphabet) for i in range(size)) for j in range(blocks))
    def getId():
        return self.__id
    def __getitem__(self, name):
        if(name in self.data):
            return self.data[name]
        raise AttributeError("Invalid key!")
    def __setitem__(self, name, value):
        self.data[name] = key
    def __delitem(self, name):
        if(name in self.data):
            del self.data[name]
            return
        raise AttributeError("Invalid key!")
