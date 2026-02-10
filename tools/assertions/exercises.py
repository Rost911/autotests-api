from tools.assertions.base import assert_equal
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema,
                                                ExerciseSchema,
                                                GetExerciseResponseSchema,
                                                CreateExerciseResponseSchema)


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет, что упражнение, созданное API, соответствует данным запроса.

    :param request: Запрос на создание упражнения.
    :param response: Ответ API с созданным упражнением.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверка модели задания с использованием ExercisesSchema

    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    """
    Проверка  ответа получения данных задания

    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

