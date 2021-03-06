#!/usr/bin/python2.7

import sys
from noolite_serial import NooLiteSerial

noo_serial = NooLiteSerial('/dev/ttyS0')

if len(sys.argv) < 2:
    raise Exception('Not Enough params')

noo_serial.send_command(int(sys.argv[1]), 0, mode=1, ctr=3)
print noo_serial.receive()
