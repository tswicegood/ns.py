import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
sys.path[0:0] = [os.path.join(os.path.dirname(__file__), a) \
        for a in ["a", "b", "y", "z"]]

import unittest


class BasicTestCase(unittest.TestCase):
    def test_bar_is_imported_from_b(self):
        from foo import bar
        self.assertEqual("a", bar.__file__.split("/")[-3])

    def test_baz_is_imported_from_b(self):
        from foo import baz
        self.assertEqual("b", baz.__file__.split("/")[-3])


class NestedTestCase(unittest.TestCase):
    def test_baz_is_imported_from_y(self):
        from xyz.biz import baz
        self.assertEqual("y", baz.__file__.split("/")[-4])

    def test_biz_is_imported_from_z(self):
        from xyz.biz import biz
        self.assertEqual("z", biz.__file__.split("/")[-4])

if __name__ == "__main__":
    unittest.main()
