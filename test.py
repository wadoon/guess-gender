__author__ = 'weigl'

from unittest import TestCase

import gender_guess as gg
import sys

sys.path.insert(0, "/home/weigl/workspace/gender-guess/build/lib.linux-x86_64-2.7")

class GenderGuessTest(TestCase):
    def gender_guess_test(self, name):
        return
    def test_gender_guess(self):
        self.assertEqual(gg.guess_gender("Alexander") ,'M')
        self.assertEqual(gg.guess_gender("Eicke") ,'F')

        self.assertEqual(gg.guess_gender("Alexander") ,'M')
        self.assertEqual(gg.guess_gender("Eicke") ,'F')
