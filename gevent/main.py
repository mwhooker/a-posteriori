import gevent
import random
from collections import defaultdict, namedtuple
import topsort
import itertools
import functools

"""
def job(wait=0):
    gevent.sleep(wait)
    print "waited %d seconds" % wait

waits = [random.randint(0, 5) for i in xrange(10)]

jobs = [gevent.spawn(job, wait) for wait in waits]

gevent.joinall(jobs)

print "done"
"""


Foo = namedtuple('Foo', ('obj', 'pre', 'post'))


#total run time should be ~2 seconds.
# D & B & C are paralellizable
class Base(object):
    depends = []

    def pre(self, parents):
        self.klass = self.__class__.__name__
        print "pre ", self.klass

    def post(self):
        print "post ", self.__class__.__name__

class B(Base):

    def pre(self, parents):
        gevent.sleep(1)
        super(B, self).pre(parents)

    def post(self):
        gevent.sleep(1)
        super(B, self).post()

class C(Base):

    def pre(self, parents):
        gevent.sleep(1)
        super(C, self).pre(parents)

    def post(self):
        gevent.sleep(1)
        super(C, self).post()

class A(Base):

    depends = [B, C]

class D(Base):

    def pre(self, parents):
        gevent.sleep(1)
        super(D, self).pre(parents)


def run_pre(klass, state):
    obj = klass()
    parents = []
    if hasattr(klass, 'depends'):
        for key in klass.depends:
            parents.append(state[key])
    try:
        obj.pre(parents)
    except Exception as e:
        print "caught exception."
        return None
    return obj

def run_post(obj):
    try:
        obj.post()
    except Exception as e:
        print "caught post exception"

def check_pass(klass, state):
    """True if `klass` has a greenlet in `state`."""
    return bool(state[klass])

def all_passed(iterable, state):
    """True if all members of `iterable` have a greenlet in `state`."""

    return all([check_pass(klass, state) for klass in iterable])


if __name__ == '__main__':
        dependency_pairs = []

        for klass in [A, B, C, D]:
            if not len(klass.depends):
                dependency_pairs.append((None, klass))
                continue
            for dep in klass.depends:
                dependency_pairs.append((dep, klass))

        levels = filter(all, topsort.topsort_levels(dependency_pairs))
        print list(topsort.topsort_levels(dependency_pairs))

        seen = {}
        for level in levels:
            jobs = {}
            for klass in level:
                if all_passed(klass.depends, seen):
                    jobs[klass] = gevent.spawn(run_pre, klass, seen)
            gevent.joinall(jobs.values())
            for klass in level:
                if klass in jobs:
                    seen[klass] = jobs[klass].value
                else:
                    seen[klass] = None

            # seen[klass] should never raise a KeyError
            assert all([klass in seen for klass in level])

        for level in reversed(levels):
            eligible = [klass for klass in level if check_pass(klass, seen)]
            #eligible = filter(functools.partial(check_pass, state=seen), level)
            jobs = [gevent.spawn(run_post, seen[klass]) for klass in eligible]
            gevent.joinall(jobs)
