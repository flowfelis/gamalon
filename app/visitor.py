from datetime import date
from app import db
from models import UniqueVisitor
from app import app
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
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
        return unique_visitor_schema.jsonify(visitor), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'IntegrityError': "Make sure 'visit_id and visitor_id fields' are unique in 'unique_visitor table'"}), 500
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred while trying to insert into 'unique_visitor table'"})


@app.route('/unique_visitors/<string:date>')
def get_all_unique_visitors(date):
    """
    GET Daily visitors- how many unique visitors did the site see on a specific day.
    """
    visitors = UniqueVisitor.query.filter_by(visit_date=date).all()

    return unique_visitor_schema.jsonify(visitors, many=True)
