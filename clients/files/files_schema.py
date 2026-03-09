from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake

class FileSchema(BaseModel):
    """
    Description of the file structure.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Description of the structure of the request for creating a file.
    """

    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")

    directory: str = Field(default="tests")
    upload_file: FilePath

class CreateFileResponseSchema(BaseModel):
    """
    Description of the structure of the file creation response.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Description of the structure of the request for retrieving a file.
    """
    file: FileSchema

