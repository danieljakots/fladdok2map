#!/usr/bin/env python3.4

from flask import Flask
from fladdok2map import fladdok2map

def create_app():
    app = Flask(__name__)
    app.config['SERVER_NAME'] = 'chown.me'
    app.register_blueprint(fladdok2map, url_prefix='/addok2map')
    app.config.update(dict(DEBUG=False))
    return app

app = create_app()

if __name__ == '__main__':
  app.run(port=8999) 
