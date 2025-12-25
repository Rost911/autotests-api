from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
    GetExercisesQuerySchema,
    GetExercisesResponseSchema,
)
from clients.private_http_builder import (
    AuthenticationUserSchema,
    get_private_http_client,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с API /api/v1/exercises.

    Используется для получения, создания, обновления и удаления упражнений.
    Все методы требуют авторизации.
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения списка упражнений курса.

        :param query: Query-параметры запроса (courseId).
        :return: Объект httpx.Response.
        """
        return self.get(
            "/api/v1/exercises",
            params=query.model_dump(by_alias=True, exclude_none=True),
        )

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет GET-запрос для получения упражнения по идентификатору.

        :param exercise_id: UUID упражнения.
        :return: Объект httpx.Response.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(
        self,
        request: CreateExerciseRequestSchema,
    ) -> Response:
        """
        Выполняет POST-запрос для создания нового упражнения.

        :param request: Данные для создания упражнения.
        :return: Объект httpx.Response.
        """
        return self.post(
            "/api/v1/exercises",
            json=request.model_dump(by_alias=True),
        )

    def update_exercise_api(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestSchema,
    ) -> Response:
        """
        Выполняет PATCH-запрос для обновления упражнения.

        :param exercise_id: UUID упражнения.
        :param request: Данные для обновления упражнения.
        :return: Объект httpx.Response.
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет DELETE-запрос для удаления упражнения.

        :param exercise_id: UUID упражнения.
        :return: Объект httpx.Response.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseSchema:
        """
        Возвращает упражнение по идентификатору в виде Pydantic-модели.

        :param exercise_id: UUID упражнения.
        :return: Объект CreateExerciseResponseSchema.
        """
        response = self.get_exercise_api(exercise_id)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self,
        query: GetExercisesQuerySchema,
    ) -> GetExercisesResponseSchema:
        """
        Возвращает список упражнений курса.

        :param query: Query-параметры запроса (courseId).
        :return: Объект GetExercisesResponseSchema.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self,
        request: CreateExerciseRequestSchema,
    ) -> CreateExerciseResponseSchema:
        """
        Создаёт упражнение и возвращает результат в виде модели.

        :param request: Данные для создания упражнения.
        :return: Объект CreateExerciseResponseSchema.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestSchema,
    ) -> UpdateExerciseResponseSchema:
        """
        Обновляет упражнение и возвращает обновлённые данные.

        :param exercise_id: UUID упражнения.
        :param request: Данные для обновления.
        :return: Объект UpdateExerciseResponseSchema.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создаёт экземпляр ExercisesClient с авторизованным HTTP-клиентом.

    :param user: Данные пользователя для аутентификации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
