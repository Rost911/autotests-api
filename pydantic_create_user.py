from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Схема описания пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Схема описания полей запроса на создание пользователя
    """
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания пользователя,
    содержащая данные пользователя
    """
    user: UserSchema

