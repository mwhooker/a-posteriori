from nose.plugins import Plugin

class TestPlugin(Plugin):
    name = 'tplugin'

    def wantMethod(self, method):
        if method.__name__ in ('pre', 'post'):
            return True
