from homework_18_1 import even_number_generator, fibonacci_generator
from homework_18_2 import ReverseNumListIterator, EvenNumbersIterator
from homework_18_3 import LogDecorator, ExceptionHandler
import pytest


@pytest.mark.check_generator
def test_even_number_generator_success():
    actual_result = list(even_number_generator(20))
    expected_result = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert actual_result == expected_result

@pytest.mark.check_generator
def fibonacci_generator_success():
    actual_result = list(fibonacci_generator(20))
    expected_result = [0, 1, 1, 2, 3, 5, 8, 13]
    assert actual_result == expected_result


@pytest.mark.check_iterator
def test_reverse_iterator_success():
    actual_result = list(ReverseNumListIterator([1, 2, 3, 4, 5]))
    expected_result = [5, 4, 3, 2, 1]
    assert actual_result == expected_result

@pytest.mark.check_iterator
def test_even_numbers_iterator_success():
    actual_result = list(EvenNumbersIterator(10))
    expected_result = [0, 2, 4, 6, 8, 10]
    assert actual_result == expected_result
