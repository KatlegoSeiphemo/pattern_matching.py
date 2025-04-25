import unittest
from src.matcher import isMatch

class TestRegexMatcher(unittest.TestCase):
    def test_examples(self):
        self.assertFalse(isMatch("aa", "a"))
        self.assertTrue(isMatch("aa", "a*"))
        self.assertTrue(isMatch("ab", ".*"))
        self.assertFalse(isMatch("mississippi", "mis*is*p*."))
        self.assertTrue(isMatch("mississippi", "mis*is*ip*."))

if __name__ == "__main__":
    unittest.main()
