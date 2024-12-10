from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Database connection details
server = os.getenv('DB_HOST')  # Use a default value if the variable is not set
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')

def get_db_connection():
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str)
    return conn

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    cellphone = data.get('cellphone')

    if not username or not cellphone:
        return jsonify({'error': 'Missing data'}), 400

    conn = None  # Initialize conn to avoid UnboundLocalError
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, cellphone) VALUES (?, ?)", (username, cellphone))
        conn.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:  # Ensure conn is closed if it was opened
            conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    conn = None  # Initialize conn to avoid UnboundLocalError
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, cellphone FROM users")
        rows = cursor.fetchall()
        users = [{'username': row[0], 'cellphone': row[1]} for row in rows]
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:  # Ensure conn is closed if it was opened
            conn.close()

@app.route('/delete_users', methods=['DELETE'])
def delete_users():
    conn = None  # Initialize conn to avoid UnboundLocalError
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users")  # Delete all users
        conn.commit()
        return jsonify({'message': 'All users deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:  # Ensure conn is closed if it was opened
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
