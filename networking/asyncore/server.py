import asyncore
import json
import socket



class Clients(object):

    def __init__(self):
        self.clients = {}

    def add_client(self, username, client):
        self.clients[username] = client

class ChatHandler(asyncore.dispatcher_with_send):

    def __init__(self, socket, server):
        asyncore.dispatcher_with_send.__init__(self, socket)
        self.server = server
        self.outgoing = []

    def handle_read(self):
        data = self.recv(8192)
        if data:
            msg = json.loads(data)
            print "got ", data
            if msg["type"] == "connect":
                self.username = msg["username"]
                self.server.register(self)
            elif msg["type"] == "msg":
                self.server.message(self, msg["body"])
    
    def send_message(self, from_, message):
        msg = json.dumps({
            "from": from_,
            "body": message
        })
        self.send(msg)


class ChatServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

        self.clients = {}
        self.connections = set([])

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            self.connections.add(ChatHandler(sock, self))

    def handle_write(self):
        print "server ready to write"

    def register(self, client):
        self.clients[client.username] = client
    
    def message(self, from_, message):
        for username in self.clients:
            if username != from_.username:
                self.clients[username].send_message(from_.username, message)


server = ChatServer('localhost', 51234)
asyncore.loop()
