from datetime import date

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

from app import app, db
from models import ChatSession
from schemas import chat_session_schema


@app.route('/chat_session/<int:chat_session_id>', methods=['POST'])
def add_chat_session(chat_session_id):
    """
    Add a chat session record to chat_session table with unique ID and today's date.
    :param chat_session_id: ID of the created chat session.
    """

    chat_session = ChatSession(
        chat_session_id=chat_session_id,
        chat_session_date=date.today()
    )

    try:
        db.session.add(chat_session)
        db.session.commit()
        return chat_session_schema.jsonify(chat_session), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred while trying to insert into 'chat_session table'"})


@app.route('/chat_sessions/<string:date>')
def get_chat_sessions(date):
    """
    GET Daily chats- how many chat sessions were started
    :param date: filter by date. Should be in ISO Format.
    """

    chat_session_count = len(
        ChatSession.query.filter_by(chat_session_date=date).all())
    chat_sessions = {'date': date, 'result': chat_session_count}

    return jsonify(chat_sessions)
