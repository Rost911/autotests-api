from http import HTTPStatus

import pytest
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                CreateExerciseResponseSchema, GetExerciseResponseSchema)
from fixtures.courses import CourseFixture
from clients.exercises.exercises_client import ExercisesClient
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
from tools.assertions.schema import validate_json_schema
from fixtures.exercises import function_exercise, ExerciseFixture


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, function_course: CourseFixture, exercises_client: ExercisesClient):
        """
        Проверяет создание упражнения через POST /api/v1/exercises.

        Шаги:
        - отправляет запрос на создание упражнения
        - проверяет статус-код 200
        - проверяет тело ответа на соответствие запросу
        - валидирует JSON schema ответа
        """
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    def test_get_exercise(self, function_exercise: ExerciseFixture,
                          exercises_client: ExercisesClient):
        """
        Проверяет выполнения GET-запроса на эндпоинт /api/v1/exercises/{exercise_id}.
        Шаги:
        - отправляет запрос на создание упражнения
        - проверяет статус-код 200
        - проверяет тело ответа на соответствие запросу
        - валидирует JSON schema ответа
        """

        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(get_exercise_response=response_data,
                                     create_exercise_response=function_exercise.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

