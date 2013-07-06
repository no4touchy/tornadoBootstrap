# -*- coding: UTF-8 -*-

import shelve

class StorageManager:
    def __init__(self, fname):
        self.fname = fname
        self.shelf = shelve.open(fname, writeback=True)
    def open(fname):
        return SessionManager(fname)
    def close(self):
        self.shelf.close()
        #os.remove(self.fname)
    def __getitem__(self, name):
        return self.shelf[name]
    def __setitem__(self, name, value):
        self.shelf[name] = value
    def __delitem__(self, name):
        del self.shelf[name]
