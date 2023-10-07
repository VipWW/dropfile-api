from flask import Blueprint
from app.schema.responses import ErrorMessage
from app.common.exceptions import BookNotFoundError
from app.services.book_service import BookService
from app.schema.book_schema import BookSchema
from webargs.flaskparser import use_args

api = Blueprint("book", __name__, url_prefix="/api/book")


@api.errorhandler(422)
def handle_422(error):
    return ErrorMessage(error.description), 422


@api.errorhandler(404)
def handle_404():
    return ErrorMessage("Not found"), 404


@api.errorhandler(BookNotFoundError)
def handle_book_not_found(error):
    return ErrorMessage(error), 404


@api.get("/all")
def get_all_books():
    """Gets all books

    Returns:
        List[Book]: List of books
    """
    books = BookService.get_all_books()
    return BookSchema(many=True).dump(books), 200


@api.get("/<book_id>")
def get_book_by_id(book_id: str):
    """Gets a book by ID

    Args:
        book_id (str): Book ID

    Returns:
        Book: Book with a particular ID
    """
    book = BookService.get_book_by_id(book_id)
    return BookSchema().dump(book), 200


@api.post("/new")
@use_args(BookSchema())
def new_book(args):
    book = BookService.new_book(**args)
    return BookSchema().dump(book), 201
