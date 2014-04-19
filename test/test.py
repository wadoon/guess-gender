__author__ = 'weigl'

import sys
print sys.path

from unittest import TestCase
import gender_guess as gg

class GenderGuessTest(TestCase):
    def test_gender_guess(self):
        self.assertEqual('M', gg.guess_gender("Alexander", country = gg.Country.GERMANY))
        self.assertEqual('?', gg.guess_gender("Eicke"))
        self.assertEqual('?', gg.guess_gender("Eicke", country= gg.Country.GERMANY))

    def test_gender_guess_unicode(self):
        self.assertEqual('?', gg.guess_gender(u"Eicke"))
        self.assertEqual('?', gg.guess_gender(u"Eicke", country= gg.Country.GERMANY))



if __name__ == "__main__":
	import nose
	nose.main()
