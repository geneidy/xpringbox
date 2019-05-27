#!/usr/bin/env python

import sys
import random
import string
import socket
import argparse

from cmd2 import Cmd

class TrustLine(Cmd):
    """ Simple trustline demo """

    def __init__(self, 
                host_ip,
                host_port,
                host_name,
                remote_ip,
                remote_port):

        super().__init__()
        self.allow_cli_args = False

        if (valid_ip(host_ip)):
            self._host_ip = host_ip
        else:
            print('Invalid IP address. Exitting.')
            sys.exit(0)

        if (valid_port(host_port)):
            self._host_port = host_port
        else:
            print('Invalid port. Exitting.')
            sys.exit(0)
        
        if host_name:
            self._host_name = host_name
        else:
            self._host_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        
        if (valid_ip(remote_ip)):
            self._remote_ip = remote_ip
        else:
            print('Invalid IP address. Exitting.')

        if(valid_port(remote_port)):
            self._remote_host = remote_port
        else:
            print('Invalid port. Exitting.')
            sys.exit(0)

        print('Welcome to your trustline,', self._host_name, ':)')

        self.balance = 0

    def do_balance(self, args):
        """ Query your trustline balance """
        print(self.balance)

    def do_pay(self, args):
        """ Pay your trustline counterparty """
        print(args)

    def do_exit(self, args):
        """ Quits the program. """
        print("Goodbye,", self._host_name, ":(")
        return True

def valid_ip(addr):
    try:
        socket.inet_aton(addr)
        return True
    except:
        return False

def valid_port(port):
    if(1024 <= int(port) <= 65535):
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description='Simple trustline demo')
    parser.add_argument('--host_ip', help='IP address trustline counterparty to use.', required=True)
    parser.add_argument('--host_port', help='Port trustline counterparty to use', required=True)
    parser.add_argument('--host_name', help='Optional host name', required=False)
    parser.add_argument('--remote_ip', help='The remote trustline counterparty IP', required=True)
    parser.add_argument('--remote_port', help='The remote trustline counterparty port', required=True)
    
    args = vars(parser.parse_args())
    
    prompt = TrustLine(args['host_ip'],
                        args['host_port'],
                        args['host_name'],
                        args['remote_ip'],
                        args['remote_port'])
    prompt.prompt = '> '
    prompt.cmdloop()

if __name__ == '__main__':
    main()