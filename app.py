from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="frontend/dist/assets")

DB = "db.json"


def load_db():
    """
    This function is used to get the rows of the DB.
    Used when getting all the DB rows or a specific one.
    """
    if not os.path.exists(DB):
        return []

    with open(DB, "r") as db_file:
        return json.load(db_file)


def save_db(db):
    """
    This function is used to save a row to the DB.
    Used when adding a row or updating a project's status.
    """
    with open(DB, "w") as db_file:
        json.dump(db, db_file, indent=4)


@app.route("/")
def home():
    return send_from_directory("frontend/dist", "index.html")


@app.route("/rows", methods=["GET"])
def get_rows():
    """
    Endpoint for getting all the rows from the DB.
    """
    rows = load_db()

    return jsonify(rows)


@app.route("/rows/<int:index>", methods=["GET"])
def get_row(index):
    """
    Endpoint for getting a specific row from the DB.
    """
    db = load_db()

    if index >= len(db) or index < 0:
        error_json = {
            "error": "index out of range",
        }

        return jsonify(error_json)

    return jsonify(db[index])


@app.route("/rows", methods=['POST'])
def add_row():
    """
    Endpoint for adding a new row to the DB.
    """
    new_row = request.json
    db = load_db()

    db.append(new_row)
    save_db(db)

    return jsonify(new_row)


@app.route("/rows/<int:index>", methods=["PATCH"])
def update_project_status(index):
    """
    Endpoint for updating a project's status.
    """
    updated_status = request.json.get("status")

    if updated_status is None:
        error_json = {
            "error": "no status provided"
        }

        return jsonify(error_json)

    db = load_db()

    if index >= len(db) or index < 0:
        error_json = {
            "error": "index out of range",
        }

        return jsonify(error_json)

    db[index]["status"] = updated_status
    save_db(db)

    return jsonify(db[index])


if __name__ == '__main__':
    app.run(debug=True)
