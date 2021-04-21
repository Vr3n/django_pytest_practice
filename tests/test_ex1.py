import pytest


@pytest.mark.skip
def test_skip():
    assert 1 == 1


@pytest.mark.xfail
def test_configuration_fail():
    assert 1 == 4


def test_configuration():
    assert 1 == 1
