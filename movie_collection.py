from typing import Dict, List, Optional, Iterator

class Movie:
    def __init__(self, title: str, year: int, genre: str, director: str = "") -> None:
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}), жанр: {self.genre}, режиссер: {self.director}"

class MovieCollection:
    def __init__(self) -> None:
        self.movies: Dict[str, Movie] = {}
        self.collections: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie) -> None:
        """Добавляет фильм в коллекцию"""
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> bool:
        """Удаляет фильм из коллекции"""
        movie = self.movies.pop(title, None)
        if movie:
            # Удаляем фильм из всех коллекций
            for collection in self.collections.values():
                if movie in collection:
                    collection.remove(movie)
            return True
        return False

    def create_collection(self, name: str) -> None:
        """Создает новую коллекцию"""
        if name not in self.collections:
            self.collections[name] = []

    def add_to_collection(self, collection_name: str, movie_title: str) -> bool:
        """Добавляет фильм в указанную коллекцию"""
        if collection_name not in self.collections:
            return False
        movie = self.movies.get(movie_title)
        if movie and movie not in self.collections[collection_name]:
            self.collections[collection_name].append(movie)
            return True
        return False

    def remove_from_collection(self, collection_name: str, movie_title: str) -> bool:
        """Удаляет фильм из указанной коллекции"""
        if collection_name not in self.collections:
            return False
        movie = self.movies.get(movie_title)
        if movie and movie in self.collections[collection_name]:
            self.collections[collection_name].remove(movie)
            return True
        return False

    def search_by_title(self, title: str) -> Optional[Movie]:
        """Ищет фильм по названию"""
        return self.movies.get(title)

    def search_by_year(self, year: int) -> List[Movie]:
        """Ищет фильмы по году выпуска"""
        return [m for m in self.movies.values() if m.year == year]

    def search_by_genre(self, genre: str) -> List[Movie]:
        """Ищет фильмы по жанру"""
        return [m for m in self.movies.values() if m.genre.lower() == genre.lower()]

    def __iter__(self) -> Iterator[Movie]:
        """Итератор для перебора всех фильмов"""
        return iter(self.movies.values())

    def get_collection(self, name: str) -> Optional[List[Movie]]:
        """Возвращает фильмы из указанной коллекции"""
        return self.collections.get(name)
    

if __name__ == "__main__":
    # Создаем коллекцию
    collection = MovieCollection()
    
    # Добавляем фильмы
    collection.add_movie(Movie("Крестный отец", 1972, "Криминал", "Фрэнсис Форд Коппола"))
    collection.add_movie(Movie("Темный рыцарь", 2008, "Боевик", "Кристофер Нолан"))
    collection.add_movie(Movie("Побег из Шоушенка", 1994, "Драма", "Фрэнк Дарабонт"))
    
    # Создаем коллекцию "Лучшие"
    collection.create_collection("Лучшие")
    collection.add_to_collection("Лучшие", "Крестный отец")
    collection.add_to_collection("Лучшие", "Побег из Шоушенка")
    
    # Поиск фильмов
    print("Фильмы 1994 года:")
    for movie in collection.search_by_year(1994):
        print(movie)
    
    print("\nФильмы в коллекции 'Лучшие':")
    for movie in collection.get_collection("Лучшие") or []:
        print(movie)
    
    # Итерация по всем фильмам
    print("\nВсе фильмы в коллекции:")
    for movie in collection:
        print(movie)

    A = input()
    print(f'Название фильма {A}')