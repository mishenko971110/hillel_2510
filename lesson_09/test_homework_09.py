import unittest
from homework_09 import check_count_unique_symbols, sum_even_numbers, find_substring

class TestTask1(unittest.TestCase):
    def test_count_symbols_more_than_10(self):
        test_str = 'aAbCcdef gRrtttuoty'
        result = check_count_unique_symbols(test_str)
        self.assertTrue(result)
    
    def test_count_symbols_less_than_10(self):
        test_str = 'test'
        result = check_count_unique_symbols(test_str)
        self.assertTrue(not result)

    def test_empty_entered_string(self):
        test_str = ''
        result = check_count_unique_symbols(test_str)
        self.assertTrue(not result)

    def test_incorrect_input_data(self):
        test_str = ['1', '2', '3', '4']
        with self.assertRaises(AttributeError):
            result = check_count_unique_symbols(test_str)


class TestTask2(unittest.TestCase):
    def test_sum_even_numbers(self):
        test_list = [1, 2, 3, 4, 5, 10]
        result = sum_even_numbers(test_list)
        self.assertEqual(result, 16)

    def test_sum_only_even_numbers(self):
        test_list = [0, 2, 7, 4, 5, 13]
        result = (sum_even_numbers(test_list) % 2 == 0)
        self.assertTrue(result)

    def test_incorrect_input_data(self):
        test_list = ['1', '2', '3', '4']
        with self.assertRaises(TypeError):
            result = sum_even_numbers(test_list)


class TestTask3(unittest.TestCase):
    def test_string_is_found(self):
        str1 = "Hello, world!"
        str2 = "world"
        result = find_substring(str1, str2)
        self.assertEqual(result, 7)
    
    def test_string_is_not_found(self):
        str1 = "The quick brown fox jumps over the lazy dog"
        str2 = "cat"
        result = find_substring(str1, str2)
        self.assertEqual(result, -1)
    
    def test_incorrect_input_data(self):
        str1 = "Hello, world!"
        str2 = 5
        with self.assertRaises(TypeError):
            result = find_substring(str1, str2)
    

if __name__ == '__main__':
    unittest.main()
