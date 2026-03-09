import pytest


@pytest.mark.xfail(reason='A bug was found in the application, causing the test to fail with an error.')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='The bug has already been fixed, but the test is still marked with xfail.')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='The external service is temporarily unavailable.')
def test_external_services_is_unavailable():
    assert 1 == 2