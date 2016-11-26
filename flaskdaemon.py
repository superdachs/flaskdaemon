#!/usr/bin/env python3

from threading import Thread
from flask import Flask
import daemonize
from time import sleep
import json
import sys
import os

class FlaskDaemon:

    def __init__(self):
        self.data = ["Hallo Welt", "Feld 2"]

    def main(self):
        
        app = Flask(__name__)
        app.debug = False
        app.use_reloader=False
        
        @app.route("/data")
        def get_data():
            return json.dumps(self.data)

        Thread(target=app.run).start()

        self.loop()

    def loop(self):
        i = 0
        while True:
            
            self.data.append(i)
            i += 1
            sleep(1)

if __name__ == "__main__":
    
    def start():
        daemonize.Daemonize(app="flaskdaemon", pid="/tmp/flaskdaemon.pid", action=FlaskDaemon().main).start()

    def stop():
        if not os.path.exists("/tmp/flaskdaemon.pid"):
            sys.exit(0)
        with open("/tmp/flaskdaemon.pid", "r") as pidfile:
            pid = pidfile.read()
        os.system('kill -9 %s' % pid)

    def foreground():
        FlaskDaemon().main()

    def usage():
        print("usage: start|stop|restart|foreground")
        sys.exit(1)

    if not sys.argv[1]:
        usage()

    if sys.argv[1] == "start":
        start()
    elif sys.argv[1] == "stop":
        stop()
    elif sys.argv[1] == "restart":
        stop()
        start()
    elif sys.argv[1] == "foreground":
        foreground()
    else:
        sys.exit(1)
