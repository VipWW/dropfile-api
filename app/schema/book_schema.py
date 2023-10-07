from marshmallow import pre_load
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.book import Book


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        ordered = True

    id = auto_field(dump_only=True)

    title = auto_field(required=True)
    length = auto_field(required=True)

    @pre_load
    def strip_strings(self, data, **kwargs):
        for key, item in data.items():
            if isinstance(item, str):
                data[key] = item.strip()
