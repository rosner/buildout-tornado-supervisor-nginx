import logging
import logging.config

from tornado.options import define, options, parse_command_line
from tornado.web import Application
from tornado.ioloop import IOLoop

from .handlers import MainHandler

define('port', default=8000, help='run on the given port', type=int)
define('host', default='127.0.0.1', help='The host')
define('debug', default=False, type=bool)

def log_request(handler):
    if handler.get_status() < 400:
        log_method = logging.info
    elif handler.get_status() < 500:
        log_method = logging.warning
    else:
        log_method = logging.error
    request_time = 1000.0 * handler.request.request_time()
    log_method("%d %s %.2fms", handler.get_status(),
               handler._request_summary(), request_time)

def start_service():
    parse_command_line()
    logging.info('Starting Tornado web server on http://localhost:%s', 
            options.port)

    settings = {
        'debug': options.debug,
        'log_function': log_request,
        'address': options.host,
    }

    application = Application([
        (r"/", MainHandler),
    ], **settings)

    server_settings = {
        'xheaders' : True,
    }
    application.listen(options.port, **server_settings)
    IOLoop.instance().start()

