#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(seconds)

try:
    gevent.spawn(wait).join()
except Timeout:
    print 'Could not complete'