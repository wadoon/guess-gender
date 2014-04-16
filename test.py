__author__ = 'weigl'

from unittest import TestCase

import sys
sys.path.insert(0, "/home/weigl/workspace/gender-guess/build/lib.linux-x86_64-2.7")
print sys.path


import gender_guess as gg

class GenderGuessTest(TestCase):
    def test_gender_guess(self):
        self.assertEqual('M', gg.guess_gender("Alexander"))
        self.assertEqual('?', gg.guess_gender("Eicke"))
        self.assertEqual('?', gg.guess_gender("Eicke", country= gg.Country.GERMANY))
