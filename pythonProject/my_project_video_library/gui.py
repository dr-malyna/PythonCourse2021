from tkinter import Tk, Button, StringVar, Entry, Menu, Listbox, END, messagebox, Toplevel

from my_project_video_library.actors import ActorDAO
from my_project_video_library.movies import MovieDAO


class Win_Movie1:
    def __init__(self, win_class):
        self.win_class = win_class
        self.win_movies = Toplevel(win_class.win)
        self.win_movies.title("Select years range...")
        self.win_movies.geometry("250x140+300+150")
        self.message_text1 = StringVar()
        self.message_text1.set(2020)
        self.message_text2 = StringVar()
        self.message_text2.set(2021)
        btn1 = Button(self.win_movies, text="show", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry1 = Entry(self.win_movies, textvariable=self.message_text1)
        message_entry1.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry2 = Entry(self.win_movies, textvariable=self.message_text2)
        message_entry2.grid(row=2, column=2, ipadx=10, ipady=6, padx=10, pady=10)

    def btn_click(self):
        text_year1 = self.message_text1.get()
        text_year2 = self.message_text2.get()
        year1 = int(text_year1)
        year2 = int(text_year2)
        movie_dao = MovieDAO()
        res_movies = movie_dao.get_movies_in_range(year1, year2)
        self.win_class.languages_listbox.delete(0, END)
        for movie in res_movies:
            self.win_class.languages_listbox.insert(END, movie)


class Win_Movie2:
    def __init__(self, win_class):
        self.win_class = win_class
        self.win_movies = Toplevel(win_class.win)
        self.win_movies.title("Select movie name...")
        self.win_movies.geometry("250x140+300+150")
        self.message_text1 = StringVar()
        self.message_text1.set("Don't Look Up")
        btn1 = Button(self.win_movies, text="show", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry1 = Entry(self.win_movies, textvariable=self.message_text1)
        message_entry1.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)

    def btn_click(self):
        actor_dao = ActorDAO()
        movie_name = self.message_text1.get()
        movie_name = movie_name.replace("'","''")
        res_actors = actor_dao.get_actors_in_movie(movie_name)
        self.win_class.languages_listbox.delete(0, END)
        for actor in res_actors:
            self.win_class.languages_listbox.insert(END, actor)


class Win_Movie3:
    def __init__(self, win_class):
        self.win_class = win_class
        self.win_movies = Toplevel(win_class.win)
        self.win_movies.title("Select movie quantity...")
        self.win_movies.geometry("250x140+300+150")
        self.message_text1 = StringVar()
        self.message_text1.set(2)
        btn1 = Button(self.win_movies, text="show", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry1 = Entry(self.win_movies, textvariable=self.message_text1)
        message_entry1.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)

    def btn_click(self):
        actor_dao = ActorDAO()
        qty_text = self.message_text1.get()
        res_actors = actor_dao.get_actors_in_min_N_movies(int(qty_text))
        self.win_class.languages_listbox.delete(0, END)
        for actor in res_actors:
            self.win_class.languages_listbox.insert(END, actor)


class Win_Movie4:
    def __init__(self, win_class):
        self.win_class = win_class
        self.win_movies = Toplevel(win_class.win)
        self.win_movies.title("Select an actor who was co-director at least in 1 movie")
        self.win_movies.geometry("250x140+300+150")
        btn1 = Button(self.win_movies, text="show", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)

    def btn_click(self):
        actor_dao = ActorDAO()
        res_actors = actor_dao.get_directors_and_actors_simultaneously()
        self.win_class.languages_listbox.delete(0, END)
        for actor in res_actors:
            self.win_class.languages_listbox.insert(END, actor)


class Win_Movie5:
    def __init__(self, win_class):
        self.win_class = win_class
        self.win_movies = Toplevel(win_class.win)
        self.win_movies.title("Delete all movies which release date more than a given number of years...")
        self.win_movies.geometry("250x140+300+150")
        self.message_text1 = StringVar()
        self.message_text1.set(25)
        btn1 = Button(self.win_movies, text="run", command=self.btn_click)
        btn1.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)
        message_entry1 = Entry(self.win_movies, textvariable=self.message_text1)
        message_entry1.grid(row=1, column=2, ipadx=10, ipady=6, padx=10, pady=10)

    def btn_click(self):
        movie_dao = MovieDAO()
        qty_years = self.message_text1.get()
        res = movie_dao.del_old_movies(qty_years)
        self.win_class.languages_listbox.delete(0, END)
        self.win_class.languages_listbox.insert(END, res)

class WinClass:
    def __init__(self):
        self.win = Tk()
        self.win.title("")
        self.win.geometry("300x270+100+100")
        self.message_text1 = StringVar()
        self.message_text1.set("enter value")
        self.message_text2 = StringVar()
        self.message_text2.set("enter value")
        self.message_text3 = StringVar()
        self.message_text3.set("enter op")
        self.message_text4 = StringVar()
        self.message_text4.set("result")

        self.languages_listbox = Listbox()
        self.languages_listbox.grid(row=1, rowspan=5, column=1, columnspan=4, ipadx=10, ipady=6, padx=10, pady=10)

        db_menu = Menu()
        db_menu.add_command(label='Task 1 (select all movies in range)',command=self.run_task1)
        db_menu.add_command(label='Task 2 (select actors who starred in that movie)',command=self.run_task2)
        db_menu.add_command(label='Task 3 (select actors who starred in N movies)',command=self.run_task3)
        db_menu.add_command(label='Task 4 (select actors who were director in min 1 movie)', command=self.run_task4)
        db_menu.add_command(label='Task 5 (delete movies with a release date older than a N of years ago)',
                            command=self.run_task5)

        main_menu = Menu()
        main_menu.add_cascade(label='Database', menu=db_menu)
        self.win.config(menu=main_menu)
        self.win.mainloop()

    def run_task1(self):
        win_movie = Win_Movie1(self)

    def run_task2(self):
        win_movie = Win_Movie2(self)

    def run_task3(self):
        win_movie = Win_Movie3(self)

    def run_task4(self):
        win_movie = Win_Movie4(self)

    def run_task5(self):
        win_movie = Win_Movie5(self)

