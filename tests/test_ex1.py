import pytest


# function          Run once per test.
# class             Run once per class of tests.
# module            Run once per module.
# session           Run once per session.


@pytest.fixture(scope="function")
def fixture1():
    print('run-fixture-1')
    return 1


@pytest.mark.skip
def test_skip():
    assert 1 == 1


def test_configuration_fail(fixture1):
    print('run-test-1')
    num = fixture1
    assert num == 1


def test_configuration(fixture1):
    print('run-test-2')
    num = fixture1
    assert num == 1
