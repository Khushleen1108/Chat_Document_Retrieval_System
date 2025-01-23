from config import get_db_connection

def update_chat_history(user_id, user_message, ai_response):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_messages (user_id, position, user_query, ai) VALUES (%s, %s, %s, %s)",
        (user_id, get_next_position(user_id), user_message, ai_response)
    )

    cursor.execute(
        "DELETE FROM chat_messages WHERE user_id = %s AND message_id NOT IN (SELECT message_id FROM chat_messages WHERE user_id = %s ORDER BY position DESC LIMIT 5)",
        (user_id, user_id)
    )

    conn.commit()
    conn.close()

def get_next_position(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(position) FROM chat_messages WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] + 1 if result[0] else 1

def get_chat_history(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_query, ai FROM chat_messages WHERE user_id = %s ORDER BY position ASC LIMIT 5", (user_id,))
    messages = cursor.fetchall()
    conn.close()
    return [{"user": msg[0], "ai": msg[1]} for msg in messages]