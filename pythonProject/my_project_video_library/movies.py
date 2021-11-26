import sqlite3


class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self):
        return f"Movie: {self.name} ({self.release_year})\n"

    def __repr__(self):
        return self.__str__()


class MovieDAO:
    def __init__(self):
        self.conn = sqlite3.connect("video_library.db")
        self.cursor = self.conn.cursor()

    def get_movies_in_range(self, start_year: int, end_year: int):
        self.cursor.execute(f"SELECT * FROM Movie WHERE Movie.ReleaseYear BETWEEN {start_year} AND {end_year}")
        result_list = self.cursor.fetchall()
        movie_list = list()
        for res in result_list:
            movie_list.append(Movie(res[1], res[2]))
        return movie_list

    def del_old_movies(self, years_ago: int):
        try:
            self.cursor.execute(f"DELETE FROM Movie WHERE ReleaseYear < strftime('%Y','now') - {years_ago}")
            #self.conn.commit() temporary commented for test
            return f"Success deleted rows: {self.cursor.rowcount}"
        except sqlite3.Error as error:
            return f"Failed to delete record from sqlite table {error}"

    def close(self):
        self.conn.close()
