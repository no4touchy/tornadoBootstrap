#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web, tornado.ioloop, tornado.options, tornado.autoreload, tornado.template
import session
import json

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.sess = session.SessionManager.open("data/sessions")
    def on_finish(self):
        self.sess.close()
    @tornado.web.asynchronous
    def get(self, *args):
        #self.write("Hello World!<br />\n")
        #self.write("{}<br />\n".format(session.SessionManager.genId(0, 6, 5)))
        #self.write("{}<br />\n".format(args))
        
        #self.write(tornado.template.Loader("tmpl").load("index.html").generate())
        string = open("tmpl/chat.json", "r").read()
        string = string.replace(",\n    ", ", ").replace("\n    ", "").replace("\n}\n", "}").replace("\n", "\\n")
        page = open("tmpl/page.html", "rb").read()
        tmpl = tornado.template.Template(page, compress_whitespace=False, autoescape=None)
        self.write(tmpl.generate(**json.loads(string)))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r'/assets/(.*)', tornado.web.StaticFileHandler, {'path': "tmpl/assets"})
    ])
    application.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
