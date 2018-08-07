import unittest
import cap


class TestCap(unittest.TestCase):

    def test_word(self):
        text = "python"
        result = cap.capitalize_text(text)
        self.assertEqual(result, "Python")

    def test_multi_words(self):
        text = "multi python"
        result = cap.capitalize_text(text)
        self.assertEqual(result, "Multi python")


if __name__ == "__main__":
    unittest.main()
