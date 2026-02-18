from passlib.context import CryptContext

# Utiliser argon2 à la place de bcrypt (pas de limite de 72 bytes)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class HashPassword:
    def create_hash(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_hash(self, plain_password: str, hashed_password: str) :
        return pwd_context.verify(plain_password, hashed_password)
    
