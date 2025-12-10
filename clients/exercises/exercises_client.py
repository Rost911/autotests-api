from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class GetExercisesRequestDict(TypedDict):
    """
    Структура запроса для получения списка упражнений.

    :param courseId: Идентификатор курса, к которому относятся упражнения.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Структура запроса для создания нового упражнения.

    :param title: Название упражнения.
    :param courseId: Идентификатор курса, которому принадлежит упражнение.
    :param maxScore: Максимальная оценка.
    :param minScore: Минимальная оценка.
    :param orderIndex: Порядковый номер упражнения в курсе.
    :param description: Описание упражнения.
    :param estimatedTime: Примерное время выполнения упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict, total=False):
    """
    Структура запроса для частичного обновления упражнения (PATCH).

    Все поля являются необязательными.

    :param title: Название упражнения.
    :param maxScore: Максимальная оценка.
    :param minScore: Минимальная оценка.
    :param orderIndex: Порядковый номер упражнения в курсе.
    :param description: Описание упражнения.
    :param estimatedTime: Примерное время выполнения упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с упражнениями по эндпоинту /api/v1/exercises.

    Наследуется от APIClient и использует методы HTTP-запросов:
    GET, POST, PATCH, DELETE.
    """

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Получает список упражнений для указанного курса.

        :param query: Словарь вида {"courseId": <UUID курса>}.
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает упражнение по его идентификатору.

        :param exercise_id: Уникальный UUID упражнения.
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создаёт новое упражнение.

        :param request: Словарь с параметрами нового упражнения.
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет существующее упражнение (частично, PATCH).

        :param exercise_id: UUID упражнения, которое нужно обновить.
        :param request: Словарь с изменяемыми данными.
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет упражнение по его идентификатору.

        :param exercise_id: UUID упражнения, которое нужно удалить.
        :return: Объект httpx.Response с данными ответа сервера.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
