import psycopg2
from domain.user import User
from application.ports import UserRepository

class PostgresUserRepository(UserRepository):
    def get_user(self, user_id: int) -> User:
        conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword host=localhost")
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        if user_data:
            return User(*user_data)
        return None