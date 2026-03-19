from pydantic import BaseModel, Field, ConfigDict, EmailStr
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Description of the user structure.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Description of the POST request structure
    for creating a new user.
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    """
    Description of the user creation response structure.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Description of the user update request structure.
    """
    model_config = ConfigDict(populate_by_name=True)
    # Added random email generation
    email: EmailStr | None = Field(default_factory=fake.email)
    # Added random last name generation
    last_name: str | None = Field(alias="lastName", default_factory=fake.last_name)
    # Added random first name generation
    first_name: str | None = Field(alias="firstName", default_factory=fake.first_name)
    # Added random middle name generation
    middle_name: str | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Description of the user update response structure.
    """
    user: UserSchema

class GetUserResponseSchema(BaseModel):
    """
    Description of the user retrieval response structure.
    """
    user: UserSchema