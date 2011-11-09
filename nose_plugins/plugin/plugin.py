from nose.plugin import Plugin

class TestPlugin(Plugin):
    name = 'test'

    def options(self, parser, env):
        print "options"

    def configure(self, options, conf):
        pass
