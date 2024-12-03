from homework_10 import log_event 
import pytest

LOG_FILE = 'login_system.log'

def read_last_log_line():
    with open(LOG_FILE, 'r') as log_file:
        lines = log_file.readlines()
    return lines[-1].strip()


@pytest.mark.log_status_check
@pytest.mark.positive
def test_log_event_success():
    username = "user1"
    status_test = "success"

    log_event(username, status_test)
    last_line = read_last_log_line()

    assert f"Login event - Username: {username}, Status: {status_test}" in last_line


@pytest.mark.log_status_check
@pytest.mark.positive
def test_log_event_expired():
    username = "user2"
    status_test = "expired"

    log_event(username, status_test)
    last_line = read_last_log_line()

    assert f"Login event - Username: {username}, Status: {status_test}" in last_line


@pytest.mark.log_status_check
@pytest.mark.positive
def test_log_event_failed():
    username = "user3"
    status_test = "failed"

    log_event(username, status_test)
    last_line = read_last_log_line()

    assert f"Login event - Username: {username}, Status: {status_test}" in last_line


@pytest.mark.log_status_check
@pytest.mark.negative
def test_log_event_invalid_status():
    username = "user4"
    status_test = "invalid_status"

    log_event(username, status_test)
    last_line = read_last_log_line()

    assert f"Login event - Username: {username}, Status: {status_test}" in last_line
