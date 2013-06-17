#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.ioloop, tornado.web, tornado.autoreload, tornado.options
import session

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.sess = session.SessionManager.open("sessions")
    def get(self, *args):
        self.write("Hello World!<br />\n")
        self.write("{}<br />\n".format(session.SessionManager.genId(0, 6, 5)))
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
