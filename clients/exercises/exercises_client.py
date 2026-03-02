from httpx import Response
import allure

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
from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Client for working with the /api/v1/exercises API.

    Used for retrieving, creating, updating, and deleting exercises.
    All methods require authorization.
    """

    @allure.step("Get list of exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Performs a GET request to retrieve the list of course exercises.

        :param query: Query parameters of the request (courseId).
        :return: An httpx.Response object.
        """
        return self.get(
            APIRoutes.EXERCISES,
            params=query.model_dump(by_alias=True, exclude_none=True),
        )

    @allure.step("Get exercise by exercise_id: {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Performs a GET request to retrieve an exercise by its identifier.

        :param exercise_id: Exercise UUID.
        :return: An httpx.Response object.
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create new exercise")
    def create_exercise_api(
        self,
        request: CreateExerciseRequestSchema,
    ) -> Response:
        """
        Performs a POST request to create a new exercise.

        :param request: Data for creating the exercise.
        :return: An httpx.Response object.
        """
        return self.post(
            APIRoutes.EXERCISES,
            json=request.model_dump(by_alias=True),
        )

    @allure.step("Update particular exercise : {exercise_id}")
    def update_exercise_api(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestSchema,
    ) -> Response:
        """
        Performs a PATCH request to update an exercise.

        :param exercise_id: Exercise UUID.
        :param request: Data for updating the exercise.
        :return: An httpx.Response object.
        """
        return self.patch(
            f"{APIRoutes.EXERCISES}/{exercise_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

    @allure.step("Delete particular exercise : {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Performs a DELETE request to delete an exercise.

        :param exercise_id: Exercise UUID.
        :return: An httpx.Response object.
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> CreateExerciseResponseSchema:
        """
        Returns an exercise by its identifier as a Pydantic model.

        :param exercise_id: Exercise UUID.
        :return: A CreateExerciseResponseSchema object.
        """
        response = self.get_exercise_api(exercise_id)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(
        self,
        query: GetExercisesQuerySchema,
    ) -> GetExercisesResponseSchema:
        """
        Returns the list of course exercises.

        :param query: Query parameters of the request (courseId).
        :return: A GetExercisesResponseSchema object.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(
        self,
        request: CreateExerciseRequestSchema,
    ) -> CreateExerciseResponseSchema:
        """
        Creates an exercise and returns the result as a model.

        :param request: Data for creating the exercise.
        :return: A CreateExerciseResponseSchema object.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
        self,
        exercise_id: str,
        request: UpdateExerciseRequestSchema,
    ) -> UpdateExerciseResponseSchema:
        """
        Updates an exercise and returns the updated data.

        :param exercise_id: Exercise UUID.
        :param request: Data for updating.
        :return: An UpdateExerciseResponseSchema object.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Creates an instance of ExercisesClient with an authorized HTTP client.

    :param user: User data for authentication.
    :return: A ready-to-use ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
