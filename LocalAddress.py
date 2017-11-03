# -*- coding: utf-8 -*-
#!/usr/bin/env python
''''
wlanのipを探るためのプログラム
'''
import socket
import fcntl
import sys

def ifconfig(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        result = fcntl.ioctl(s.fileno(), 0x8915 ,(ifname+'\0'*32)[:32])
    except IOError:
        return None

    return socket.inet_ntoa(result[20:24])

if __name__ == '__main__':
    print (ifconfig(sys.argv[1]))
