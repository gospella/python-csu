import os
import mysql.connector

db_config = {
    'host': 'mysql_db',
    'port': 3306,
    'database': os.getenv('MYSQL_DATABASE'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD')
}


def save_result(comment: str, result: str):
    query = f"INSERT INTO sentiment_analysis (comment, result) VALUES ('{comment}', '{result}')"
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


def get_last_results(limit: int):
    query = f"SELECT * FROM sentiment_analysis ORDER BY created DESC LIMIT {limit}"
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
