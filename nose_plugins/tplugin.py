from nose.core import TextTestRunner
from nose.plugins import Plugin

class TestPlugin(Plugin):
    name = 'tplugin'

    def wantMethod(self, method):
        if method.__name__ in ('pre', 'post'):
            return True

    def prepareTestRunner(self, runner):
        return TestTestRunner()

class TestTestRunner(TextTestRunner):

    def run(self, test):
        print test
        return super(TestTestRunner, self).run(test)
