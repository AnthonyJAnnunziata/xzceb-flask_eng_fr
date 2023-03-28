import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None),"Error: Input parameter is null") # test null input
        self.assertEqual(english_to_french('Hello'),'Bonjour') # test 'Hello' input
  

class Testfrench_to_englsh(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None),"Error: Input parameter is null") # test null input
        self.assertEqual(french_to_english('Bonjour'),'Hello') # test 'Bonjour' input

unittest.main()