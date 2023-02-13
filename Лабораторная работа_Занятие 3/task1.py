class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги"""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги, бумажная """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц книги"""
        return self._pages

    @pages.setter
    def pages(self, pages_: int) -> None:
        """Устанавливает количество страниц книги"""
        if not isinstance(pages_, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages_ <= 0:
            raise ValueError("Количество страниц в книге должно быть больше нуля")
        self._pages = pages_

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги, аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> int:
        """Возвращает длительность книги"""
        return self._duration

    @duration.setter
    def duration(self, duration_: int) -> None:
        """Устанавливает длительность книги"""
        if not isinstance(duration_, int):
            raise TypeError("Длительность книги должна быть типа int")
        if duration__ <= 0:
            raise ValueError("Длительность книги должна быть больше нуля")
        self._duration = duration_

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность книги {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


