from pydantic import BaseModel, Field

class File(BaseModel):
    path: str = Field(
        description="Full location of the file, including its name and extension (e.g., 'src/app/main.py')."
    )
    purpose: str = Field(
        description="A short explanation of what this file is meant to do (for example: 'handles user login', 'stores configuration settings', or 'processes data')."
    )