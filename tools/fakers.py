from faker import Faker


class Fake:
    """
    Class for generating random test data using the Faker library.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: An instance of the Faker class used to generate data.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Generates random text.

        :return: Random text.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generates a random UUID4.

        :return: A random UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Generates a random email.

        :param domain: Email domain (for example, "example.com").
        If not specified, a random domain will be used.
        :return: A random email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Generates a random sentence.

        :return: A random sentence.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates a random password.

        :return: A random password.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Generates a random last name.

        :return: A random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates a random first name.

        :return: A random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates a random middle name (patronymic).

        :return: A random middle name.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Generates a string with an estimated time (e.g., "2 weeks").

        :return: A string with the estimated time.
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Generates a random integer within the specified range.

        :param start: Start of the range (inclusive).
        :param end: End of the range (inclusive).
        :return: A random integer.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Generates a random maximum score in the range from 50 to 100.

        :return: A random score.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates a random minimum score in the range from 1 to 30.

        :return: A random score.
        """
        return self.integer(1, 30)



fake = Fake(faker=Faker())
