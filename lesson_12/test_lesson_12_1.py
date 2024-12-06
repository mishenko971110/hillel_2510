from lesson_12_1 import is_palindrome
import pytest

@pytest.mark.parametrize('expected_result, text_line', [
  (True, 'ab c ba'),
  (False, 'abc de')
])
@pytest.mark.is_palindrome
def test_is_palindrome_positive(expected_result, text_line):
  actual_result = is_palindrome(text_line)
  assert actual_result == expected_result

@pytest.mark.is_palindrome
def test_is_palindrome_incorrect_data():
  text_line = 5
  with pytest.raises(AttributeError):
    is_palindrome(text_line)
