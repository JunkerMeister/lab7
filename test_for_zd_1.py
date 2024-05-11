import pytest
from zd_1 import count_ways_to_climb

@pytest.mark.parametrize('x, expected_result', [(5, 8),
                                                (10,89)])
def test_count_ways_to_climb(x, expected_result):
    assert count_ways_to_climb(x) == expected_result
