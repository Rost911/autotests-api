import allure
from clients.files.files_schema import (CreateFileResponseSchema, CreateFileRequestSchema,
                                        FileSchema, GetFileResponseSchema)
from tools.assertions.base import assert_equal
from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema,  InternalErrorResponseSchema
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from config import settings
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")

@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Verifies that the file creation response matches the original request.

    :param request: Original file creation request.
    :param response: API response containing file data.
    :raises AssertionError: If at least one field does not match.
    """
    # Build the expected URL for the uploaded file
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")

@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Verifies that the actual file data matches the expected data.

    :param actual: Actual file data.
    :param expected: Expected file data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check file")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


@allure.step("Check get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Verifies that the get file response matches the create file response.

    :param get_file_response: API response when requesting file data.
    :param create_file_response: API response when creating the file.
    :raises AssertionError: If the file data does not match.
    """
    logger.info("Check get file response")
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the response for creating a file with an empty filename
    matches the expected validation error.

    :param actual: API response containing the validation error to be verified.
    :raises AssertionError: If the actual response does not match the expected one.
    """
    logger.info("Check create file with empty filename response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the response for creating a file with an empty directory value
    matches the expected validation error.

    :param actual: API response containing the validation error to be verified.
    :raises AssertionError: If the actual response does not match the expected one.
    """
    logger.info("Check create file with empty directory response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Function to verify the error when a file is not found on the server.

    :param actual: Actual response.
    :raises AssertionError: If the actual response does not match the "File not found" error.
    """
    logger.info("Check file not found response")
    # Expected error message if the file is not found
    expected = InternalErrorResponseSchema(details="File not found")
    # Use the previously created function to validate the internal error
    assert_internal_error_response(actual, expected)

@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Verifies that the API returns a validation error
    when an invalid UUID is passed in the `file_id` path parameter.

    :param actual: Actual API response containing the validation error.
    :raises AssertionError: If the error structure or values differ from the expected ones.
    """
    logger.info("Check get file with incorrect file id response")
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"},
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path","file_id"]
            )
        ]
    )

    assert_validation_error_response(actual, expected)
