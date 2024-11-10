from flask import Flask, jsonify, request
from flask_cors import CORS  
import sqlite3

app = Flask(__name__)


CORS(app)


def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, content TEXT)')
    conn.commit()
    conn.close()


@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)


@app.route('/data', methods=['POST'])
def add_data():
    content = request.json['content']
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Data added"}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
