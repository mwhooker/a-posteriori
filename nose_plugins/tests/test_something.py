from unittest2 import TestCase

class TestT(TestCase):

    def testTrue(self):
        self.assertTrue(true)

    def pre(self):
        print "pre"

    def post(self):
        print "post"
