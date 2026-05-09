from pydantic import BaseModel, Field, field_validator
import emoji

class CreateUser(BaseModel):
    first_name: str = Field(..., title="First name", min_length=1, max_length=16)
    username: str = Field(..., title="Username", min_length=1, max_length=16)
    # Увеличиваем max_length, иначе сложные эмодзи не пройдут проверку Pydantic
    emoji_avatar: str = Field(..., title="Emoji avatar", min_length=1, max_length=20)
    password: str = Field(..., title="Password", min_length=8, max_length=32)

    @field_validator('emoji_avatar')
    @classmethod
    def validate_emoji(cls, v: str) -> str:
        # Проверка на наличие emoji
        if not emoji.is_emoji(v):
            raise ValueError('Must be a valid emoji')

        # Проверка, что это ровно ОДИН эмодзи (без текста и не два сразу)
        emoji_data = emoji.emoji_list(v)
        if len(emoji_data) != 1 or emoji_data[0]['emoji'] != v:
            raise ValueError('Only a single emoji is allowed')

        return v

class Login(BaseModel):
    username: str = Field(..., title="Username", min_length=1, max_length=16)
    password: str = Field(..., title="Password", min_length=8, max_length=32)
