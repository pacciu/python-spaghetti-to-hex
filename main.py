from adapters.postgres_user_repository import PostgresUserRepository
from adapters.external_email_service import ExternalEmailService
from application.services import UserRegistrationService

if __name__ == "__main__":
    user_repo = PostgresUserRepository()
    email_service = ExternalEmailService()
    registration_service = UserRegistrationService(user_repo, email_service)
    registration_service.register_user(1)