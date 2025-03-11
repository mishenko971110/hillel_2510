import pytest
import track_test_vars
from homework_27 import check_post_status

post_URL = track_test_vars.post_URL

@pytest.mark.post_test
def test_fail_msg():
    actual_result = check_post_status(post_URL, track_test_vars.post_id_fail)
    expected_result = track_test_vars.msg_fail
    assert actual_result == expected_result

@pytest.mark.post_test
def test_received_msg():
    actual_result = check_post_status(post_URL, track_test_vars.post_id_success_received)
    expected_result = track_test_vars.msg_success_received
    assert actual_result == expected_result

@pytest.mark.post_test
def test_in_post_msg():
    actual_result = check_post_status(post_URL, track_test_vars.post_id_success_in_post)
    expected_result = track_test_vars.msg_success_in_post
    assert actual_result == expected_result

@pytest.mark.post_test
def test_not_send_msg():
    actual_result = check_post_status(post_URL, track_test_vars.post_id_success_not_send)
    expected_result = track_test_vars.msg_success_not_send
    assert actual_result == expected_result
