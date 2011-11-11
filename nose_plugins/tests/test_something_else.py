from unittest import TestCase

class TestT2(TestCase):

    def testTrue(self):
        self.assertTrue(True)

    def pre(self):
        print "pre 2"

    def post(self):
        print "post 2"
