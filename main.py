#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web, tornado.websocket, tornado.ioloop 
import tornado.options, tornado.autoreload, tornado.template
import json
import session

class MainHandler(tornado.web.RequestHandler):
    sessions = {}

    @tornado.web.asynchronous
    def get(self, *args):
        content = open("tmpl/chat.json", "r").read()
        content = content.replace(",\n    ", ", ").replace("{\n    \"", "{\"").replace("\n}\n", "}").replace("\"\n", "\"").replace("\n    \"", "\"").replace("\n", "\\n")
        content = json.loads(content)

        page = open("tmpl/page.html", "rb").read()
        page = tornado.template.Template(page, compress_whitespace=False, autoescape=None)
        self.write(page.generate(**content))

        self.finish()

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def __sendToClients__(self, message):
        for client in WSHandler.clients:
            if client != self:
                client.write_message(message)
    def __sendLogins__(self):
        for client in WSHandler.clients:
            if client != self and client.nick != False:
                self.write_message(json.dumps({"action" : "login", "msg" : client.nick}))
    def __sendToAll__(self, message):
        self.__sendToClients__(message)
        self.write_message(message)
    def open(self):
        WSHandler.clients.append(self)
        self.nick = False
        self.__sendLogins__()
    def on_close(self):
        WSHandler.clients.remove(self)
        self.__sendToClients__(json.dumps({"action" : "logout", "msg" : self.nick}))
    def on_message(self, message):
        obj = json.loads(message)
        if obj["action"] == "msg":
            self.__sendToClients__(json.dumps({"action" : "msg", "user" : self.nick, "msg" : obj["msg"]}))
        elif obj["action"] == "login":
            self.nick = obj["msg"]
            self.__sendToClients__(message)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/assets/(.*)", tornado.web.StaticFileHandler, {'path': "tmpl/assets"}),
        (r"/ws", WSHandler)
    ])
    application.listen(8888)
    ioloop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(ioloop)
    ioloop.start()
