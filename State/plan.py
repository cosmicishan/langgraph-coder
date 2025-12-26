from pydantic import BaseModel, Field
from .file import File

class Plan(BaseModel):

    name: str = Field(
        description="The project or application name. This should be short, clear, and descriptive."
    )
    description: str = Field(
        description="A concise one-sentence summary that explains what the application does and its primary purpose."
    )
    techstack: str = Field(
        description="The technologies, programming languages, frameworks, and tools to be used in building the application."
    )
    features: list[str] = Field(
        description="A detailed list of core features or functionalities the application must provide, expressed in simple terms."
    )
    files: list[File] = Field(
        description="A structured list of all files to be created for the project. Each entry should include the file path and its intended purpose or role in the application."
    )