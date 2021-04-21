import pytest


@pytest.fixture
def yied_fixture():
    print("Start test phase")
    yield 6
    print("End test phase")


def test_example3(yied_fixture):
    print('run-example-1')
    assert yied_fixture == 6
