import allure
from httpx import Response
from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.courses.courses_schema import (CreateCourseRequestSchema, GetCoursesQuerySchema,
                                            UpdateCourseRequestSchema, CreateCourseResponseSchema)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes


class CoursesClient(APIClient):
    """
    Client for working with /api/v1/courses.
    """

    @allure.step("Get courses")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Method for retrieving the list of courses.

        :param query: Dictionary containing userId.
        :return: Server response as an httpx.Response object.
        """
        return self.get(APIRoutes.COURSES,
                        params=query.model_dump(by_alias=True,exclude_none=True))

    @allure.step("Get course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def get_course_api(self, course_id: str) -> Response:
        """
        Method for retrieving a course.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object.
        """
        return self.get(f"{APIRoutes.COURSES}/{course_id}")

    @allure.step("Create course")
    @tracker.track_coverage_httpx(APIRoutes.COURSES)
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Method for creating a course.

        :param request: Dictionary containing title, maxScore, minScore, description,
                        estimatedTime, previewFileId, createdByUserId.
        :return: Server response as an httpx.Response object.
        """
        return self.post(APIRoutes.COURSES,
                         json=request.model_dump(by_alias=True, exclude_none=True))

    @allure.step("Update course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Method for updating a course.

        :param course_id: Course identifier.
        :param request: Dictionary containing title, maxScore, minScore, description,
                        estimatedTime.
        :return: Server response as an httpx.Response object.
        """
        return self.patch(f"{APIRoutes.COURSES}/{course_id}",
                          json=request.model_dump(by_alias=True,exclude_none=True))

    @allure.step("Delete course by id {course_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.COURSES}/{{course_id}}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        Method for deleting a course.

        :param course_id: Course identifier.
        :return: Server response as an httpx.Response object.
        """
        return self.delete(f"{APIRoutes.COURSES}/{course_id}")


    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    The function creates an instance of CoursesClient with a preconfigured HTTP client.

    :return: A ready-to-use CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user))
