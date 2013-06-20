# -*- coding: UTF-8 -*-

import random, shelve

class Session:
    def __init__(self, id):
        self.__id = id
        self.data = {}
    def getId():
        return self.__id
    def __getattr__(self, name):
        if(name in self.data):
            return self.data[name]
        raise AttributeError("Invalid key!")
    def __setattr__(self, name, value):
        self.data[name] = key
    def __delattr(self, name):
        if(name in self.data):
            del self.data[name]
            return
        raise AttributeError("Invalid key!")

class SessionManager:
    def __init__(self, fname):
        self.fname = fname
        self.shelf = shelve.open(fname, writeback=True)
    def open(fname):
        return SessionManager(fname)
    def close(self):
        self.shelf.close()
        #os.remove(self.fname)
    def new(self):
        id = SessionManager.genId(6, 5)
        self.shelf[id] = Session(id)
        return id
    def genId(self, size, blocks):
        alphabet = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP0123456789"
        return "-".join("".join(random.choice(alphabet) for i in range(size)) for j in range(blocks))
