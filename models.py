from app import db


class UniqueVisitor(db.Model):
    __tablename__ = 'unique_visitor'

    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.Integer)
    visit_date = db.Column(db.Date)

    __table_args__ = (
        db.UniqueConstraint('visitor_id', 'visit_date'),
    )


class ChatSession(db.Model):
    __tablename__ = 'chat_session'

    id = db.Column(db.Integer, primary_key=True)
    chat_session_id = db.Column(db.Integer)
    chat_session_date = db.Column(db.Date)
