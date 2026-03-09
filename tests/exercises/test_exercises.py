from http import HTTPStatus
import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                CreateExerciseResponseSchema, GetExerciseResponseSchema,
                                                UpdateExerciseRequestSchema, UpdateExerciseResponseSchema,
                                                GetExercisesResponseSchema,
                                                GetExercisesQuerySchema)
from fixtures.courses import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (assert_create_exercise_response,
                                        assert_get_exercise_response,
                                        assert_update_exercise_response,
                                        assert_exercise_not_found_response,
                                        assert_get_exercises_response)
from tools.assertions.schema import validate_json_schema
from fixtures.exercises import function_exercise, ExerciseFixture


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(self, function_course: CourseFixture, exercises_client: ExercisesClient):
        """
        Verifies exercise creation via POST /api/v1/exercises.

        Steps:
        - sends a request to create an exercise
        - verifies the status code is 200
        - verifies the response body matches the request
        - validates the response JSON schema
        """
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(self, function_exercise: ExerciseFixture,
                          exercises_client: ExercisesClient):
        """
        Verifies execution of a GET request to the /api/v1/exercises/{exercise_id} endpoint.

        Steps:
        - sends a request to create an exercise
        - verifies the status code is 200
        - verifies the response body matches the request
        - validates the response JSON schema
        """

        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_exercise_response=response_data,
                                     create_exercise_response=function_exercise.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(self, function_exercise: ExerciseFixture, exercises_client: ExercisesClient):
        """
        Verifies updating an exercise via PATCH /api/v1/exercises/{exercise_id}.

        Steps:
        - builds a request to update the exercise
        - sends a PATCH request using ExercisesClient
        - verifies that the response status code is 200 OK
        - verifies that the data in the response matches the data sent in the request
        - validates the response JSON schema
        """
        request = UpdateExerciseRequestSchema()

        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    def test_delete_exercise(self, function_exercise: ExerciseFixture,
                             exercises_client: ExercisesClient):
        """
        Verifies deletion of an exercise via DELETE /api/v1/exercises/{exercise_id}.

        Steps:
        1. Deletes a previously created exercise.
        2. Verifies that the response status code is 200 OK.
        3. Sends a GET request to retrieve the deleted exercise.
        4. Verifies that the status code is 404 Not Found.
        5. Verifies that the response body contains the error "Exercise not found".
        6. Validates the error response JSON schema.
        """
        delete_response = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(self,
                           function_exercise: ExerciseFixture,
                           function_course: CourseFixture,
                           exercises_client: ExercisesClient):
        """
        Verifies retrieving the list of exercises for a course via GET /api/v1/exercises.

        Precondition:
        - At least one exercise exists (function_exercise).

        Steps:
        1) Send a request with the query parameter course_id.
        2) Verify the status code is 200.
        3) Verify that the created exercise is present in the list and matches the fields.
        4) Validate the response JSON schema.
        """

        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])
        validate_json_schema(response.json(), response_data.model_json_schema())






