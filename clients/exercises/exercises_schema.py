from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Схема упражнения, возвращаемого API.

    Описывает объект упражнения, который приходит от сервера
    в ответах эндпоинтов /api/v1/exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """
    Схема query-параметров запроса для получения списка упражнений.

    Используется в GET /api/v1/exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")



class GetExercisesResponseSchema(BaseModel):
    """
    Схема ответа для получения списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]



class CreateExerciseRequestSchema(BaseModel):
    """
    Структура запроса для создания нового упражнения.
    Используется в POST /api/v1/exercises.

    :param title: Название упражнения.
    :param courseId: Идентификатор курса, которому принадлежит упражнение.
    :param maxScore: Максимальная оценка.
    :param minScore: Минимальная оценка.
    :param orderIndex: Порядковый номер упражнения в курсе.
    :param description: Описание упражнения.
    :param estimatedTime: Примерное время выполнения упражнения.
    """
    model_config= ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    """
    Схема ответа при создании упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
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
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    order_index: int | None = Field(default=None, alias="orderIndex")
    description: str | None = None
    estimated_time: str | None = Field(default=None, alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Схема ответа при обновлении упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema