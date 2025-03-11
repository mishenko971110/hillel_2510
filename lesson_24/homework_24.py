'''
Є Flask app яке дозволяє робити аутентифiкацию i пiсля цього шукати автомобiлi через GET запрос. 
Потрiбно через Pytest органiзувати тестування даного app використовуючи параметризацiю ( 5-7 наборiв даних ) 
з рiзними параметрами GET запиту **sort_by** i **limit**. Тест повинен використовувати модуль **request**. 
Первинна аутентифiкация повинна бути органiзована у виглядi фiкстури **scope=’class’**. 
Сам тест повинен вмiти робити логування не тiльки в консоль але i в файл **test_search.log**
'''
import pytest
import requests
from requests.auth import HTTPBasicAuth
from app_logger import logger


@pytest.fixture(scope='class')
def authenticate():
    session = requests.Session()
    url = 'http://127.0.0.1:8080/auth'
    credentials = HTTPBasicAuth('test_user', 'test_pass')
    logger.info("Authenticating user...")
    response = session.post(url, auth=credentials)
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        session.headers.update({'Authorization': f'Bearer {token}'})
        logger.info("Authentication successful.")
        return session
    else:
        logger.error(f"Authentication failed with status code {response.status_code}")
        pytest.fail(f"Authentication failed with status code {response.status_code}")

@pytest.mark.parametrize("sort_by, limit", [
    ('price', 5),
    ('year', 10),
    ('engine_volume', 7),
    ('price', 3),
    ('year', 2)
])

def test_search_cars(authenticate, sort_by, limit):
    session = authenticate
    url = f'http://127.0.0.1:8080/cars?sort_by={sort_by}&limit={limit}'
    logger.info(f"Sending GET request to {url}")
    response = session.get(url)
    
    if response.status_code == 200:
        logger.info(f"Response received: {response.json()}")
    else:
        logger.error(f"Request failed with status code {response.status_code}")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= limit
