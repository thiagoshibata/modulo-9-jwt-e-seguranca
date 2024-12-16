from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos
import jwt

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str: 
        token = jwt.encode(
        payload={
            'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos["JWT_HOURS"])),
            **body
        },
        key=jwt_infos["KEY"],
        algorithm=jwt_infos["ALGORITHM"]
    )
        return token
    
    def decode_jwt_token(self, token:str) -> dict:
        token_information = jwt.decode(
                token,
                key=jwt_infos["KEY"],
                algorithms=jwt_infos["ALGORITHM"]
            )
        return token_information