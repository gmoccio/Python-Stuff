from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect('martyrology.db')
    db.row_factory = sqlite3.Row
    return db


@app.route('/martyrology/<int:month>/<int:day>')
def get_martyrology(month, day):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM martyrology WHERE month = ? AND day = ?', (month, day))
    row = cursor.fetchone()
    db.close()

    if row is None:
        return jsonify({'error': 'No martyrology found for this date'}), 404

    return jsonify({
        "Month": row['month'],
        "Day": row['day'],
        "Martyrology": row['content']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)