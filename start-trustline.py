#!/usr/bin/env python

import sys
import random
import string
import threading
import socket
import socketserver
import argparse

from cmd2 import Cmd


BALANCE = 0

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        response = bytes('Thank you for your trust.', 'ascii')
        global BALANCE
        BALANCE += int(data)
        print('You were paid ' + data + '!')
        #cur_thread = threading.current_thread()
        #response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        #print(response)
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TrustLine(Cmd):
    """ Simple trustline demo """

    def __init__(self, 
                host_addr,
                host_port,
                host_name,
                remote_addr,
                remote_port):

        super().__init__()
        self.allow_cli_args = False

        if (valid_ip_addr(host_addr)):
            self._host_addr = host_addr
        else:
            print('Invalid IP address. Exitting.')
            sys.exit(0)

        if (valid_port(host_port)):
            self._host_port = int(host_port)
        else:
            print('Invalid port. Exitting.')
            sys.exit(0)
        
        if host_name:
            self._host_name = host_name
        else:
            self._host_name = ''.join([random.choice(string.ascii_letters + string.digits) 
                                for n in range(32)])
        
        if (valid_ip_addr(remote_addr)):
            self._remote_addr = remote_addr
        else:
            print('Invalid IP address. Exitting.')

        if(valid_port(remote_port)):
            self._remote_port = int(remote_port)
        else:
            print('Invalid port. Exitting.')
            sys.exit(0)

        print('Welcome to your trustline, ' + self._host_name + '! ' +  ':)')

        self.server_start()

    def server_start(self):
        self.server = ThreadedTCPServer((self._host_addr, self._host_port), 
                                        ThreadedTCPRequestHandler)
        #print(self.server.server_address)
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

    def client(self, ip_addr, port, message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip_addr, port))
        try: 
            self.sock.sendall(bytes(message, 'ascii'))
            print('Sent')
            #response = str(self.sock.recv(1024), 'ascii')
            #print("Received: {}".format(response))
        finally:
            self.sock.close()

    def do_balance(self, args):
        """ Query your trustline balance """
        print(BALANCE)

    def do_pay(self, args):
        """ Pay your trustline counterparty """
        self.client(self._remote_addr, self._remote_port, args)
        global BALANCE
        BALANCE -= int(args)

    def do_exit(self, args):
        """ Quits the program. """
        print('Goodbye,', self._host_name, ":(")
        self.server.shutdown()
        self.server.server_close()
        return True

    # NOTE: Nested classes are not pythonic. Refactor out.



def valid_ip_addr(addr):
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple trustline demo.')
    parser.add_argument('--host_addr', help='IP address trustline counterparty to use.', required=True)
    parser.add_argument('--host_port', help='Port trustline counterparty to use.', required=True)
    parser.add_argument('--host_name', help='Optional host name.', required=False)
    parser.add_argument('--remote_addr', help='Remote trustline counterparty IP address.', required=True)
    parser.add_argument('--remote_port', help='Remote trustline counterparty port.', required=True)
    
    args = vars(parser.parse_args())
    
    prompt = TrustLine(args['host_addr'],
                        args['host_port'],
                        args['host_name'],
                        args['remote_addr'],
                        args['remote_port'])
    prompt.prompt = '> '
    prompt.cmdloop()