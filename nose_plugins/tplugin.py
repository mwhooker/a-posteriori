from unittest import TestCase
from nose.core import TextTestRunner
from nose.plugins import Plugin

class TestPlugin(Plugin):
    name = 'tplugin'

    def wantMethod(self, method):
        if method.__name__ in ('pre', 'post'):
            return True

    def prepareTestRunner(self, runner):
        return TestTestRunner()

    def prepareTest(self, test):
        return MultiRunner(test)


class MultiRunner(wbject):
    def __init__(self, test):
        pass

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

class TestTestRunner(TextTestRunner):

    def run(self, test):
        return super(TestTestRunner, self).run(test)
