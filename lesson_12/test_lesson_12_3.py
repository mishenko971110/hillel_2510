from lesson_12_3 import get_success_student
import pytest

@pytest.mark.students_mark_test
def test_get_success_student_success():
  test_list = [
      {"name": "John", "grades": [85, 90, 92]},
      {"name": "Jane", "grades": [78, 80, 85]},
      {"name": "Doe", "grades": [100, 100, 100]},
      {"name": "Smith", "grades": [65, 75, 70]}
  ]
  actual_result = get_success_student(test_list, 88)
  expected_result = ['John', 'Doe']
  assert actual_result == expected_result


@pytest.mark.parametrize('expected_result, test_list', [
  (ZeroDivisionError, [{"name": "John", "grades": []},{"name": "Jane", "grades": [85]},{"name": "Doe", "grades": [100, 100, 100]}]),
  (KeyError, [{"name": "John"},{"name": "Jane"}])
])
@pytest.mark.students_mark_test
def test_get_success_student_error_check(expected_result, test_list):
  with pytest.raises(expected_result):
    get_success_student(test_list, 88)
