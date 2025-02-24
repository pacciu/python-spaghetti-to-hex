from application.ports import UserRepository, EmailService

class UserRegistrationService:
    def __init__(self, user_repo: UserRepository, email_service: EmailService):
        self.user_repo = user_repo
        self.email_service = email_service

    def register_user(self, user_id: int):
        user = self.user_repo.get_user(user_id)
        if user:
            success = self.email_service.send_email(user.email, "Welcome!", "Thanks for joining!")
            if success:
                print(f"Welcome email sent to {user.name}")
            else:
                print("Failed to send email")
        else:
            print("User not found")