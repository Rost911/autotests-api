import allure
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.errors import assert_internal_error_response
from tools.assertions.base import assert_equal, assert_length
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                ExerciseSchema,
                                                GetExerciseResponseSchema,
                                                CreateExerciseResponseSchema, UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema, GetExercisesResponseSchema)

from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check create exercise response")
def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
) -> None:
    """
    Verifies that the exercise created by the API
    matches the data provided in the request.

    :param request: Exercise creation request.
    :param response: API response containing the created exercise.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check create exercise response")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Check exercise schema")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema) -> None:
    """
    Validation of the assignment model using ExercisesSchema.
    """
    logger.info("Check exercise schema")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema) -> None:
    """
    Validation of the response for retrieving assignment data.
    """
    logger.info("Check get exercise response")
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema,
                                    response: UpdateExerciseResponseSchema) -> None:
    """
    Verifies that the exercise update response matches the data from the request.

    :param request: Original exercise update request.
    :param response: API response containing the updated exercise data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check update exercise response")
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema) -> None:
    """
    Function to verify the error when an exercise is not found on the server.

    :param actual: Actual response.
    :raises AssertionError: If the actual response does not match the "Exercise not found" error.
    """
    logger.info("Check exercise not found response")
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response list")
def assert_get_exercises_response(
    get_exercises_response: GetExercisesResponseSchema,
    create_exercise_responses: list[CreateExerciseResponseSchema],
) -> None:
    """
    Verifies that the list of assignments contains the expected exercises.

    :param actual: API response containing the list of assignments.
    :param expected: List of expected assignments.
    """
    logger.info("Check get exercises response list")
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)

