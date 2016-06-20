# -*- coding: utf-8 -*-

import os
import json

import tornado.ioloop
import tornado.web


settings = {'static_path': os.path.join(os.path.dirname(__file__), "static")}


class EpitetHandler(tornado.web.RequestHandler):

    epithets = None

    def get(self):
        print('GET')
        if self.epithets is None:
            epithets = open('epithets.txt', 'r').read()
            epithets = epithets.split(' ')
            self.epithets = json.dumps(epithets)
        self.set_status(200)
        self.write(self.epithets)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/task2.html')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'^/epithets/$', EpitetHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler,
             {"path": settings['static_path']})
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
