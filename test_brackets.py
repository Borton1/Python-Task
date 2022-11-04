import unittest
from brackets import is_valid_brackets

class TestIsValidBrackets(unittest.TestCase):
    # тест на правильность возвращаемого значения
    def test_area(self):
        self.assertEqual(is_valid_brackets("]["), False)
        self.assertEqual(is_valid_brackets("()"), True)
        self.assertEqual(is_valid_brackets("{}"), True)
        self.assertEqual(is_valid_brackets("{)"), False)
        self.assertEqual(is_valid_brackets("{}[([()])[]]"), True)
        self.assertEqual(is_valid_brackets("{}[]"), True)
        self.assertEqual(is_valid_brackets("{((}"), False)
        self.assertEqual(is_valid_brackets("[{()}]"), True)
        self.assertEqual(is_valid_brackets("[[]}"), False)
        self.assertEqual(is_valid_brackets("[{)}]"), False)


    # тест на корректность введенных символов
    def test_values(self):
        self.assertRaises(ValueError, is_valid_brackets, "df")
        self.assertRaises(ValueError, is_valid_brackets, "sg")


    # тест на корректность типа данных
    def test_types(self):
        self.assertRaises(TypeError, is_valid_brackets, 5)
        self.assertRaises(TypeError, is_valid_brackets, [2, 5])
        self.assertRaises(TypeError, is_valid_brackets, { 'fe':4 })
        self.assertRaises(TypeError, is_valid_brackets, (3 ,))
        self.assertRaises(TypeError, is_valid_brackets, True)


