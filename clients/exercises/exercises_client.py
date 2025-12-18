from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Структура упражнения, возвращаемого API.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры формата упражнения
    """
    exercise_id: str

class GetExercisesRequestDict(TypedDict):
    """
    Структура запроса для получения списка упражнений.

    :param courseId: Идентификатор курса, к которому относятся упражнения.
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры получения ответа списка упражнений
    """
    exercises: list[Exercise]



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

    def get_exercise(self, query: GetExercisesRequestDict):
        """
        Возвращает упражнение по ID в виде JSON.

        :param exercise_id: Идентификатор упражнения.
        :return: JSON-ответ сервера.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercises(self,query: GetExercisesQueryDict ):
        """
        Возвращает список упражнений в виде JSON.

        :param query: Query-параметры запроса.
        :return: JSON-ответ сервера.
        """
        response = self.get_exercise_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict):
        """
        Создаёт упражнение и возвращает JSON-ответ.

        :param request: Данные нового упражнения.
        :return: JSON-ответ сервера.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, query: GetExercisesQueryDict, request: UpdateExerciseRequestDict ):
        """
        Обновляет упражнение и возвращает JSON-ответ.

        :param GetExercisesQueryDict: Идентификатор упражнения.
        :param request: Обновляемые данные.
        :return: JSON-ответ сервера.
        """
        response = self.update_exercise_api(query, request)
        return response.json()



def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))