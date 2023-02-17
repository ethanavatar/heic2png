import pytest

def inc(x):
    return x + 1

@pytest.mark.xfail(reason = "Bug with arithmetic")
def test_answer():
    assert inc(3) == 5
