#!/usr/bin/python

import os
from requests import get
print '\n'
print 'Your Private IP Address is '
priv8 = 'hostname -I'
os.system(priv8)

print '\n'

ip = get('https://api.ipify.org').text
print 'Your public IP address is \n', ip
print '\n'
