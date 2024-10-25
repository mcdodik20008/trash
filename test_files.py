import pytest
from main import get_baza


@pytest.mark.parametrize("length, summ", [(2, 6)])
def test_test(length, summ):
    arr = [-1, 2, 4, 5]
    ln, sm = get_baza(arr)
    assert ln == length
    assert sm == summ
