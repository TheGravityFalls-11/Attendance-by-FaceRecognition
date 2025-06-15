from flask import Flask, jsonify, send_from_directory
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/attendance')
def attendance():
    with open('../attendance.csv', newline='') as f:
        reader = csv.reader(f)
        return jsonify(list(reader))

if __name__ == '__main__':
    app.run(debug=True)
