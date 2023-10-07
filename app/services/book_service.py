from typing import List

from app.extensions import db
from app.models.book import Book


class BookService:
    @staticmethod
    def get_all_books() -> List[Book]:
        """Gets all books

        Returns:
            List[Book]: List of books
        """
        return Book.query.all()

    @staticmethod
    def get_book_by_id(book_id: str) -> Book:
        """Gets a book by ID

        Args:
            book_id (str): Book ID

        Returns:
            Book: Book with a particular ID
        """
        return Book.query.filter_by(id=book_id).first()

    @staticmethod
    def new_book(title: str, length: int) -> Book:
        """Creates a new book

        Args:
            title (str): book title
            length (str): book length

        Returns:
            User: Newly created book
        """
        user = Book(title, length)

        db.session.add(user)
        db.session.commit()

        return user
