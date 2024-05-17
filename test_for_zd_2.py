import pytest
from zd_2 import *

@pytest.mark.parametrize('word, expected_result', [('nnnfffn', 'n'),
                                                ('кокошанель', 'ко'),
                                                ('nhgabdabdn', 'abd')])
def test_find_max_substring(word, expected_result):
    assert find_max_substring(word) == expected_result


@pytest.mark.parametrize('sl, ans', [('nnnffnnnnnnnnfn', 8),
                                    ('кокошанель', 2),
                                    ('nhgabdabdabdn', 3)])
def test_find_end_count(sl, ans):
    assert find_end_count(sl) == ans