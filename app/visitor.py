from datetime import date
from app import db
from models import UniqueVisitor
from app import app
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify
from schemas import unique_visitor_schema


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
        # return jsonify(), 201
        return unique_visitor_schema.jsonify(visitor), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/unique_visitors/<string:date>')
def get_all_unique_visitors(date):
    """
    GET Daily visitors- how many unique visitors did the site see on a specific day.
    """
    visitors = UniqueVisitor.query.filter_by(visit_date=date).all()
    # import pdb
    # pdb.set_trace()

    return unique_visitor_schema.jsonify(visitors, many=True)
