from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notes = []
current_id = 1

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    global current_id
    data = request.get_json()

    note = {
        "id": current_id,
        "text": data.get("text", "")
    }

    notes.append(note)
    current_id += 1

    return jsonify(note), 201

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)