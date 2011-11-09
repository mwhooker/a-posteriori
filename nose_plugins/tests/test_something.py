from unittest import TestCase

class TestT(TestCase):

    def testTrue(self):
        self.assertTrue(True)

    def pre(self):
        print "pre"

    def post(self):
        print "post"
