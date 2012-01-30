from twisted.internet.protocol import Protocol, ReconnectingClientFactory
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.internet import task
from twisted.internet import reactor
from twisted.internet import defer
import curses
import curses.panel
import time
from sys import stdout, stdin, exit



class Echo(Protocol):
    
    def __init__(self, chatbox):
        self.chatbox = chatbox

    def dataReceived(self, data):
        self.chatbox.add_message(data)
        #stdout.write(data)

    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)

class EchoClientFactory(ReconnectingClientFactory):
    def __init__(self, chatbox):
        self.chatbox = chatbox
        #self.d = defer.Deferred()

    def sendMessage(self, msg):
        pass

    def startedConnecting(self, connector):
        pass
        #print 'Started to connect.'

    def buildProtocol(self, addr):
        #print 'Connected.'
        #print 'Resetting reconnection delay'
        self.resetDelay()
        return Echo(self.chatbox)

    def clientConnectionLost(self, connector, reason):
        #print 'Lost connection.  Reason:', reason
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        #print 'Connection failed. Reason:', reason
        ReconnectingClientFactory.clientConnectionFailed(
            self, connector, reason)




class ChatBox(object):

    def __init__(self, panel, hlines, vlines):
        self.panel = panel
        self.hlines = hlines - 2
        self.vlines = vlines - 2
        self.window = panel.window()

        self.panel.show()
        self.window.border(0)
        self.messages = []

    def add_message(self, msg):
        self.messages.append(msg)
        self.refresh()

    def refresh(self):
        for i, msg in enumerate(self.messages[-self.hlines:]):
            self.window.addnstr(i + 1, 1,
                                msg.ljust(self.vlines, ' '),
                                self.vlines)

        self.window.refresh()

def main(window):

    curses.curs_set(0)
    curses.cbreak()
    curses.use_default_colors()
    window.nodelay(1)
    window.border(0)
    display_win = window.subwin(45, 100, 0, 0)

    chat_win = window.subwin(20, 80, 0, 101)
    chat_panel = curses.panel.new_panel(chat_win)
    chatbox = ChatBox(chat_panel, 20, 80)

    cl = EchoClientFactory(chatbox) 

    def mainloop():
        ch = window.getch()
        curses.flushinp()
        if ch > 0:
            chatbox.add_message(chr(ch))
            cl.sendMessage(chr(ch))
        display_win.refresh()


    point = TCP4ClientEndpoint(reactor, "localhost", 8123)

    d = point.connect(cl)
    d.addCallback(lambda data: chatbox.add_message('p'))

    l = task.LoopingCall(mainloop)
    l.start(0.1)
    #reactor.connectTCP('localhost', 8123, cl)
    
    reactor.run()


if False:
    reactor.connectTCP('localhost', 8123, EchoClientFactory())
    reactor.run()

if True:
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        exit(0)
