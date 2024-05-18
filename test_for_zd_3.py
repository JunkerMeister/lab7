import pytest
from zd_3 import *

@pytest.mark.parametrize('x, y, expected_result', [(4, 4, 20),
                                                (3, 3, 6),
                                                (20, 40, 947309492837400)])
def test_find_all_paths(x, y, expected_result):
    assert find_all_paths(x, y) == expected_result
