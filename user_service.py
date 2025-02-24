import psycopg2
import requests

def get_user_from_db(user_id):
    conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword host=localhost")
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def send_welcome_email(user_email):
    response = requests.post("https://api.emailservice.com/send", json={"to": user_email, "subject": "Welcome!", "body": "Thanks for joining!"})
    return response.status_code == 200

def register_user(user_id):
    user = get_user_from_db(user_id)
    if user:
        success = send_welcome_email(user[2])
        if success:
            print(f"Welcome email sent to {user[1]}")
        else:
            print("Failed to send email")
    else:
        print("User not found")

register_user(1)