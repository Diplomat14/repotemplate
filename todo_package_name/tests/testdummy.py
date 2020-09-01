from unittest import TestCase

from todo_package_name import dummy

class TestDummyFunc(TestCase):
    def test_is_string(selfself):
        s = dummy.testfunc()
        selfself.assertTrue(isinstance(s,str))