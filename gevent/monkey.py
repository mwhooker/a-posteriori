import httplib2
import gevent
from gevent.pywsgi import WSGIServer
from gevent.monkey import patch_all
patch_all()


def application(env, start_response):
    if env['PATH_INFO'] == '/':
        gevent.sleep(2)
        start_response('200 OK', [('Content-Type', 'text/html')])
        return ["<b>hello world</b>"]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return ['<h1>Not Found</h1>']


def task1():
    while True:
        gevent.sleep(1)
        print "task1"


def task2():
    h = httplib2.Http()
    while True:
        code, resp = h.request('http://localhost:8088')
        print resp


if __name__ == '__main__':
    print 'Serving on 8088...'
    server_job = gevent.spawn(WSGIServer(('', 8088), application).serve_forever)
    print "xxx"

    job1 = gevent.spawn(task1)
    job2 = gevent.spawn(task2)
    gevent.joinall([server_job, job1, job2])
