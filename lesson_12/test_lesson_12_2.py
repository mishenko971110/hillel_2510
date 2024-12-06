from lesson_12_2 import avg_price_of_filtered_cars
import pytest

@pytest.mark.parametrize('expected_result, expected_price, car_dict', [
  (True, 142500, {"Mersedes": [120, 120000],"Audi": [100, 165000],"VW": [75, 88000]}),
  (False, 165500, {"Mersedes": [120, 120000],"Audi": [100, 165000],"VW": [75, 88000]})
])
@pytest.mark.dict_test
def test_avg_price_of_filtered_cars(expected_result, expected_price, car_dict):
  actual_price = avg_price_of_filtered_cars(car_dict)
  actual_result = (expected_price == actual_price)
  assert actual_result == expected_result


@pytest.mark.dict_test
def test_avg_price_of_filtered_cars_incorrect_dict():
  incorrect_dict = {
    "Mersedes": [120000],
    "Audi": [100, ],
    "VW": [75, 88000, 7000]
  }
  with pytest.raises(IndexError):
    avg_price_of_filtered_cars(incorrect_dict)
