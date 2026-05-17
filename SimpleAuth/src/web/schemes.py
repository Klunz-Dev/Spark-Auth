from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    first_name: str = Field(..., title="First name", min_length=1, max_length=16)
    username: str = Field(..., title="Username", min_length=1, max_length=16)
    password: str = Field(..., title="Password", min_length=8, max_length=32)

class Login(BaseModel):
    username: str = Field(..., title="Username", min_length=1, max_length=16)
    password: str = Field(..., title="Password", min_length=8, max_length=32)
