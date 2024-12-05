from homework_10 import log_event 
import pytest

LOG_FILE = 'login_system.log'

def read_last_log_line():
    with open(LOG_FILE, 'r') as log_file:
        lines = log_file.readlines()
    return lines[-1].strip()

@pytest.mark.parametrize('username, status_test', [
  ('user1', 'success'),
  ('user2', 'expired'),
  ('user3', 'failed'),
  ('user4', 'invalid_status'),
])
@pytest.mark.log_status_check
@pytest.mark.positive
def test_log_event_success(username, status_test):
    log_event(username, status_test)
    last_line = read_last_log_line()
    assert f"Login event - Username: {username}, Status: {status_test}" in last_line
