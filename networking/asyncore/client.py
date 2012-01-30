import asyncore, socket
import json
import sys


class ChatClient(asyncore.dispatcher):

    def __init__(self, host, port, username="Matt"):
        asyncore.dispatcher.__init__(self)
        self.username = username
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, port) )
        self.buf = ""

    def handle_connect(self):
        print "Now chatting"
        self.send(json.dumps({
            "type": "connect",
            "username": self.username
        }))

    def handle_close(self):
        print "goodbye"
        self.close()
        sys.exit(0)

    def handle_read(self):
        msg = json.loads(self.recv(8192))
        print "[%s] %s" % (msg['from'], msg['body'])

    def handle_write(self):
        sent = self.send(self.buf)
        self.buf = self.buf[sent:]

    def send_msg(self, msg):
        if len(self.buf):
            print "Can't sennd right now!"
            return

        self.buf = json.dumps({
            "type": "msg",
            "body": msg
        })

class Input(asyncore.file_dispatcher):

    def __init__(self, client):
        asyncore.file_dispatcher.__init__(self, sys.stdin)
        self.client = client

    def handle_read(self):
        self.client.send_msg(self.recv(1024))


client = ChatClient('localhost', 51234, sys.argv[1])
inp_dispatcher = Input(client)

asyncore.loop()
