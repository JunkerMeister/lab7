import pytest
from zd_4 import *

@pytest.mark.parametrize('str1, str2, expected_result', [('лолкекчебурек', 'лолккчебурек', 1),
                                                ('pycharm', 'python', 4),
                                                ('football', 'basketball', 5)])
def test_min_edit_distance(str1, str2, expected_result):
    assert min_edit_distance(str1, str2) == expected_result
