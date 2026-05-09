from datetime import timedelta
from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY='NzuEtJ8guZDieXp2wxd25SCrGybieHMV',
    JWT_TOKEN_LOCATION=['headers'],
    JWT_ALGORITHM='HS256',
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=15),
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=131400)
)

security = AuthX(config=config)

