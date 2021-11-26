import sqlite3


class Actor:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Actor: {self.name} ({self.date_of_birth})\n"

    def __repr__(self):
        return self.__str__()


class ActorDAO:
    def __init__(self):
        self.conn = sqlite3.connect("video_library.db")
        self.cursor = self.conn.cursor()

    def get_actors_in_movie(self, movie_name: str):
        self.cursor.execute(f" SELECT C.MovieId, P.FullName, P.DateOfBirth FROM CAST AS C"
                            f" JOIN Person AS P ON C.PersonId = P.Id"
                            f" JOIN Movie AS M ON C.MovieId = M.MovieId"
                            f" WHERE C.RoleId = 2 AND M.name = '{movie_name}'")
        result_list = self.cursor.fetchall()
        actor_list = list()
        for res in result_list:
            actor_list.append(Actor(res[1], res[2]))
        return actor_list

    def get_actors_in_min_N_movies(self, movie_quantity: int):
        self.cursor.execute(f" SELECT * FROM Person"
                            f" WHERE Id IN ("
                            f" SELECT PersonId FROM CAST"
                            f" WHERE RoleId = 2"
                            f" GROUP BY PersonId"
                            f" HAVING COUNT(*) >= {movie_quantity})")
        result_list = self.cursor.fetchall()
        actor_list = list()
        for res in result_list:
            actor_list.append(Actor(res[1], res[2]))
        return actor_list

    def get_directors_and_actors_simultaneously(self):
        self.cursor.execute(f" SELECT P.FullName, P.DateOfBirth FROM CAST AS C"
                            f" JOIN Cast AS C2 ON C.PersonId = C2.PersonId AND C2.RoleId = 2"
                            f" JOIN Person AS P ON C.PersonId = P.Id"
                            f" WHERE C.RoleId = 1"
                            f" GROUP BY C.PersonId")
        result_list = self.cursor.fetchall()
        actor_list = list()
        for res in result_list:
            actor_list.append(Actor(res[0], res[1]))
        return actor_list

    def close(self):
        self.conn.close()
