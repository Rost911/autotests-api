import allure
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    UserSchema,
    GetUserResponseSchema,
)
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


@allure.step("Check create user response")
def assert_create_user_response(
    request: CreateUserRequestSchema,
    response: CreateUserResponseSchema,
):
    """
    Verifies that the create user response matches the original request.

    :param request: Original create user request.
    :param response: API response containing user data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check create user response")
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Compares id, email, last_name, first_name, and middle_name.
    Uses assert_equal to compare values.

    :param actual: Actual user object.
    :param expected: Expected user object.
    """
    logger.info("Check user")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


@allure.step("Check get user response")
def assert_get_user_response(
    get_user_response: GetUserResponseSchema,
    create_user_response: CreateUserResponseSchema,
):
    """
    Verifies that the user data returned by the get user request
    matches the data returned during user creation.

    :param get_user_response: Response from the get user request.
    :param create_user_response: Response from the create user request.
    """
    logger.info("Check get user response")
    assert_user(create_user_response.user, get_user_response.user)