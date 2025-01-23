import hashlib
import re
from config import get_db_connection

def is_valid_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

def check_if_email_exists(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email_id = %s", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def add_user_to_db(email, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email_id, password) VALUES (%s, %s)", (email, hashed_password))
    conn.commit()
    conn.close()

def verify_user_credentials(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email_id = %s", (email,))
    result = cursor.fetchone()
    conn.close()
    if result:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return result[0] == hashed_password
    return False

def get_user_id_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE email_id = %s", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
