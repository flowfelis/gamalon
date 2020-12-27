from app import ma
from models import ChatSession, UniqueVisitor


class UniqueVisitorSchema(ma.SQLAlchemyAutoSchema):
    """Schema for UniqueVisitor table"""

    class Meta:
        model = UniqueVisitor


class ChatSessionSchema(ma.SQLAlchemyAutoSchema):
    """Schema for ChatSession table"""

    class Meta:
        model = ChatSession


chat_session_schema = ChatSessionSchema()
unique_visitor_schema = UniqueVisitorSchema()
