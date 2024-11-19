from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Підключення до бази даних
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='admin',
        password='admin',
        db='raccoon',
        cursorclass=pymysql.cursors.DictCursor
    )

# Маршрут для отримання подій
@app.route('/events', methods=['GET'])
def get_events():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        events = cursor.fetchall()
    connection.close()
    return jsonify(events)

# Маршрут для створення нового події
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO events (title, start, end) VALUES (%s, %s, %s)"
        cursor.execute(sql, (data['title'], data['start'], data['end']))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Event created'}), 201

if __name__ == '__main__':
    app.run(debug=True)
