from datetime import date
from app import db
from models import UniqueVisitor
from app import app
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify


@app.route('/unique_visitor/<int:visitor_id>', methods=['POST'])
def add_unique_visitor(visitor_id):
    """
   Add a unique visitor record to unique_visitor table,
   with unique ID and today's date.
    :param visitor_id: unique ID of the website visitor
    """
    visitor = UniqueVisitor(
        visitor_id=visitor_id,
        visit_date=date.today(),
    )

    try:
        db.session.add(visitor)
        db.session.commit()
        return jsonify(), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify(), 500


@app.route('/unique_visitors')
def get_all_unique_visitors():
    """
    GET Daily visitors- how many unique visitors did the site see on a specific day.
    """
    visitors = UniqueVisitor.query.all()

    return jsonify()
