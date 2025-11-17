import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG


def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Erro de conexão: {e}")
        return None


def execute_query(query, params=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            conn.commit()
            return (
                cursor.lastrowid
                if query.strip().lower().startswith("insert")
                else cursor.fetchall()
            )
        except Error as e:
            print(f"Erro na query: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    return None


def fetch_one(query, params=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            return cursor.fetchone()
        except Error as e:
            print(f"Erro na query: {e}")
        finally:
            cursor.close()
            conn.close()
    return None
