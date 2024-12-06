from lesson_12_4 import get_level_access
import pytest

@pytest.mark.parametrize('expected_result, test_list', [
  ('full', {"id": 1, "name": "John", "second_name": "Doe", "age": 30}),
  ('read-only', {"id": 1, "name": "John", "second_name": "Joi", "age": 30}),
  ('forbidden', {"id": 1, "name": "John", "second_name": "Joi", "age": 25})
])
@pytest.mark.get_level_access
def test_get_level_access_success(expected_result, test_list):
  actual_result = get_level_access(test_list)
  assert actual_result == expected_result

@pytest.mark.get_level_access
def test_get_level_access_error_check():
  with pytest.raises(TypeError):
    get_level_access(88)
