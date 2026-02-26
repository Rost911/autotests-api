import allure

from clients.errors_schema import (
    ValidationErrorSchema,
    ValidationErrorResponseSchema,
    InternalErrorResponseSchema,
)
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Verifies that the validation error object matches the expected value.

    :param actual: Actual validation error.
    :param expected: Expected validation error.
    :raises AssertionError: If any field values do not match.
    """
    logger.info("Check validation error")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Check validation error response")
def assert_validation_error_response(
    actual: ValidationErrorResponseSchema,
    expected: ValidationErrorResponseSchema,
):
    """
    Verifies that the API response object containing validation errors
    (`ValidationErrorResponseSchema`) matches the expected value.

    :param actual: Actual API response.
    :param expected: Expected API response.
    :raises AssertionError: If any field values do not match.
    """
    logger.info("Check validation error response")
    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
    actual: InternalErrorResponseSchema,
    expected: InternalErrorResponseSchema,
):
    """
    Function to verify an internal error response.
    For example, a 404 error (File not found).

    :param actual: Actual API response.
    :param expected: Expected API response.
    :raises AssertionError: If any field values do not match.
    """
    logger.info("Check internal error response")
    assert_equal(actual.details, expected.details, "details")


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Function to verify the error when a file is not found on the server.

    :param actual: Actual response.
    :raises AssertionError: If the actual response does not match the "File not found" error.
    """
    # Expected error message if the file is not found
    expected = InternalErrorResponseSchema(details="File not found")
    # Use the previously created function to validate the internal error
    assert_internal_error_response(actual, expected)