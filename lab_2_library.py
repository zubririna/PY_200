from typing import Union

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: идентификатор книги
        :param name: наименование книги
        :param pages: количество страниц в книге
        """

        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть больше нуля")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Наименование книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть больше нуля")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:

    def __init__(self, books=None) -> None:
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        return len(self.books) + 1

    def get_index_by_book_id(self, id_: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index
            raise ValueError("Книги с запрашиваемым id не существует")

        

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
