from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class ExerciseSchema(BaseModel):
    """
    Exercise schema returned by the API.

    Describes the exercise object returned by the server
    in responses from the /api/v1/exercises endpoints.
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
    Schema for query parameters used to retrieve the list of exercises.

    Used in GET /api/v1/exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")



class GetExercisesResponseSchema(BaseModel):
    """
    Response schema for retrieving the list of exercises.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Response schema for retrieving an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema



class CreateExerciseRequestSchema(BaseModel):
    """
    Structure of the request for creating a new exercise.
    Used in POST /api/v1/exercises.

    :param title: Exercise title.
    :param courseId: Identifier of the course to which the exercise belongs.
    :param maxScore: Maximum score.
    :param minScore: Minimum score.
    :param orderIndex: Order index of the exercise in the course.
    :param description: Exercise description.
    :param estimatedTime: Estimated time to complete the exercise.
    """
    model_config= ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateExerciseResponseSchema(BaseModel):
    """
    Response schema for creating an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Structure of the request for partially updating an exercise (PATCH).

    All fields are optional.

    :param title: Exercise title.
    :param maxScore: Maximum score.
    :param minScore: Minimum score.
    :param orderIndex: Order index of the exercise in the course.
    :param description: Exercise description.
    :param estimatedTime: Estimated time to complete the exercise.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseResponseSchema(BaseModel):
    """
    Response schema for updating an exercise.
    """
    model_config = ConfigDict(populate_by_name=True)
    exercise: ExerciseSchema