# -*- coding: utf-8 -*-

import sys

sys.path.append('../')

from tornado import ioloop
from example_utils import log_initialize

from torpc import RPCClient

if __name__ == '__main__':
    log_initialize()

    rc = RPCClient(('127.0.0.1', 5000), 'client1')


    @rc.service.register()
    def ping():
        return 'pong from rpc client1'


    io_loop = ioloop.IOLoop.instance().start()
