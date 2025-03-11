import pytest
import track_test_vars
from homework_27 import check_post_status

post_URL = track_test_vars.post_URL

@pytest.mark.post_test
@pytest.mark.parametrize("post_id, expected_result", [
    (track_test_vars.post_id_fail, track_test_vars.msg_fail),
    (track_test_vars.post_id_success_received, track_test_vars.msg_success_received),
    (track_test_vars.post_id_success_in_post, track_test_vars.msg_success_in_post),
    (track_test_vars.post_id_success_not_send, track_test_vars.msg_success_not_send),
])
def test_post_status(post_id, expected_result):
    actual_result = check_post_status(post_URL, post_id)
    assert actual_result == expected_result
