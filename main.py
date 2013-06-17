#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.ioloop, tornado.web, tornado.autoreload, tornado.options
import random, shelve, os

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
    def open(self, fname):
        self.fname = fname
        self.shelf = shelve.open(fname, writeback=True)
    def close(self):
        self.shelf.close()
        os.remove(self.fname)
    def genId(self, size, blocks):
        alphabet = "qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP0123456789"
        return "-".join("".join(random.choice(alphabet) for i in range(size)) for j in range(blocks))

class MainHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.write("Hello World!<br />\n")
        self.write("{}<br />\n".format(SessionManager.genId(0, 6, 5)))
        self.write("{}<br />\n".format(args))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler)
    ])
    application.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
