from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

class EmailService(ABC):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        pass