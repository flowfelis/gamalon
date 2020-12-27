from datetime import date

from flask import jsonify
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import app, db
from models import UniqueVisitor
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
        return jsonify(
            {'IntegrityError': "Make sure 'visit_id and visitor_id fields' are unique in 'unique_visitor table'"}), 500
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred'"})


@app.route('/unique_visitors/<string:date>')
def get_unique_visitors(date):
    """
    GET Daily visitors- how many unique visitors did the site see on a specific day.
    :param date: filter by date. Should be in ISO Format.
    """

    visitor_count = len(UniqueVisitor.query.filter_by(visit_date=date).all())
    visitors = {'date': date, 'result': visitor_count}

    return jsonify(visitors)


@app.route('/ask_for_demo/<int:visitor_id>', methods=['POST'])
def ask_for_demo(visitor_id):
    """Update a record in DB, that chatbot asked for a demo with the corresponding unique visitor ID
    :param visitor_id: Visitor ID for updating the visitor's "ask_for_demo" boolean.
    """

    visitor = UniqueVisitor.query.filter_by(visitor_id=visitor_id).first()
    try:
        visitor.ask_for_demo = True
    except AttributeError:
        return jsonify({'NotFoundError': f'Visitor with the visitor_id={visitor_id} not found'})

    try:
        db.session.add(visitor)
        db.session.commit()
        return unique_visitor_schema.jsonify(visitor)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred'"})


@app.route('/yes_for_demo/<int:visitor_id>', methods=['POST'])
def yes_for_demo(visitor_id):
    """Update a record in DB, that visitor answered yes for a demo.
    :param visitor_id: Visitor ID for updating the visitor's "yes_for_demo" boolean.
    """

    visitor = UniqueVisitor.query.filter_by(visitor_id=visitor_id).first()

    try:
        visitor.yes_for_demo = True
    except AttributeError:
        return jsonify({'NotFoundError': f'Visitor with the visitor_id={visitor_id} not found'})

    try:
        db.session.add(visitor)
        db.session.commit()
        return unique_visitor_schema.jsonify(visitor)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred'"})


@app.route('/start_scheduling/<int:visitor_id>', methods=['POST'])
def start_scheduling(visitor_id):
    """Update a record in DB, that visitor started scheduling a demo.
    :param visitor_id: Visitor ID for updating the visitor's "start_scheduling" boolean.
    """

    visitor = UniqueVisitor.query.filter_by(visitor_id=visitor_id).first()
    try:
        visitor.start_scheduling = True
    except AttributeError:
        return jsonify({'NotFoundError': f'Visitor with the visitor_id={visitor_id} not found'})

    try:
        db.session.add(visitor)
        db.session.commit()
        return unique_visitor_schema.jsonify(visitor)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred'"})


@app.route('/finish_scheduling/<int:visitor_id>', methods=['POST'])
def finish_scheduling(visitor_id):
    """Update a record in DB, that visitor finished scheduling a demo.
    :param visitor_id: Visitor ID for updating the visitor's "finish_scheduling" boolean.
    """

    visitor = UniqueVisitor.query.filter_by(visitor_id=visitor_id).first()
    try:
        visitor.finish_scheduling = True
    except AttributeError:
        return jsonify({'NotFoundError': f'Visitor with the visitor_id={visitor_id} not found'})

    try:
        db.session.add(visitor)
        db.session.commit()
        return unique_visitor_schema.jsonify(visitor)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'UnexpectedError': "Unexpected Error occurred'"})


@app.route('/funnel_reporting/<string:date>')
def funnel_reporting(date):
    """

    Demo funnel- for a specific day, report on four datapoints

    1) How many times did the chat bot ask a visitor if they’d like a demo
    2) How many times did a visitor say yes, they would like a demo
    3) How many times did the visitor click a link to start the scheduling process
    4) How many times did the visitor reach the end of the scheduling process
    :param date: date in ISO format to filter demo funnelling on a specific date.
    """
    ask_for_demo = db.session.query(func.count(UniqueVisitor.id)).filter(
        UniqueVisitor.ask_for_demo.is_(True), UniqueVisitor.visit_date == date).scalar()
    yes_for_demo = db.session.query(func.count(UniqueVisitor.id)).filter(
        UniqueVisitor.yes_for_demo.is_(True), UniqueVisitor.visit_date == date).scalar()
    start_scheduling = db.session.query(func.count(UniqueVisitor.id)).filter(
        UniqueVisitor.start_scheduling.is_(True), UniqueVisitor.visit_date == date).scalar()
    finish_scheduling = db.session.query(func.count(UniqueVisitor.id)).filter(
        UniqueVisitor.finish_scheduling.is_(True), UniqueVisitor.visit_date == date).scalar()

    return jsonify({
        'ask_for_demo': ask_for_demo,
        'yes_for_demo': yes_for_demo,
        'start_scheduling': start_scheduling,
        'finish_scheduling': finish_scheduling,
    })
