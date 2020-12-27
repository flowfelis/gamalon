from flask import Flask, jsonify
from sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gamalon_user:1@localhost/gamalon_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/unique_visitor', methods=['POST'])
def add_unique_visitor():
    """Add a visitor"""
    pass
