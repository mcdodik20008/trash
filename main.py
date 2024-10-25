import pytest


def get_baza(arr):
    lng = 0
    sm = 0
    for a in arr:
        if int(a) % 2 == 0 and int(a) > 0:
            lng += 1
            sm += int(a)
    return lng, sm

@pytest.mark.parametrize("length, summ", [(2, 6)])
def test_test(length, summ):
    arr = [-1, 2, 4, 5]
    ln, sm = get_baza(arr)
    assert ln == length
    assert sm == summ
