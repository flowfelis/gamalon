from app import ma
from models import UniqueVisitor


class UniqueVisitorSchema(ma.SQLAlchemyAutoSchema):
    """Schema for Distribution Policy table"""

    class Meta:
        model = UniqueVisitor


unique_visitor_schema = UniqueVisitorSchema()
