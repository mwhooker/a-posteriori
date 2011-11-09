import sys
import zmq


def push(msg):
    pass

def pull():
    pass

def dohelp():
    print "Usage: python client.py <addr> [pull | push <msg>]"
    sys.exit(-1)

def main(add):
    addr = sys.argv[1]
    action = sys.argv[2]
    
    if action == 'pull':
        return pull()
    elif action == 'push':
        return push(sys.argv[3])
    else:
        dohelp()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        dohelp()
