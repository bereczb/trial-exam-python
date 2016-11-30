import unittest
file_to_test = __import__('4')

class trial_exam_python(unittest.TestCase):

    def test_empty_string_parameter(self):
        self.assertEqual(file_to_test.greeter(''), 'Hello, Mr Nobody!')

    def test_not_empty_string_parameter(self):
        self.assertEqual(file_to_test.greeter('a'), 'Hello, a!')

    def test_wo_parameter(self):
        self.assertRaises(TypeError, file_to_test.greeter)


if __name__ == '__main__':
    unittest.main()
