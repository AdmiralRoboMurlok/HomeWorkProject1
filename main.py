import sqlite3
import tkinter as tk

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE posts (date TEXT, about TEXT, postID INTEGER)")

class StronaGlowna:
    def __init__(self):
        pass
    def UIMain(self):
        root_main = tk.Tk()
        root_main.geometry("800x800")
        root_main.title("Strona Główna")

        ToDoScrollBar = tk.Scrollbar(root_main, width=30)

        ToDoListbox = tk.Listbox(root_main, yscrollcommand=ToDoScrollBar.set, width=70, height=40)
        ToDoListbox.place(x=30, y=30)



        root_main.mainloop()

class Logowanie:
    def __init__(self):
        logins = open("logins.txt", "r")
        self._username = ' '.join(logins.readlines(1)).strip()
        self._password = ' '.join(logins.readlines(2)).strip()
        self._message = ""
        logins.close()

    def ButtonLogic(self, EntryUserVar, EntryPassVar, ToDestroy, ToConfig):
        if EntryUserVar == self._username and EntryPassVar == self._password:
            ToDestroy.destroy()
            Main = StronaGlowna()
            Main.UIMain()
        else:
            ToConfig.config(text="Błąd, przy logowaniu")

    def UILogin(self):
        root_login = tk.Tk()
        root_login.geometry("500x600")
        root_login.title("Login Screen")

        Banner = tk.Label(root_login, text="Zaloguj się", font=("Courier", 36))
        Banner.place(x=30, y=50)

        UserEntryLabel = tk.Label(root_login, text="Nazwa użytkownika", font=("Courier", 18))
        UserEntryLabel.place(x=30, y=130)

        UserEntry = tk.Entry(root_login, width=40)
        UserEntry.place(x=30, y=150)

        PassEntryLabel = tk.Label(root_login, text="Hasło", font=("Courier", 18))
        PassEntryLabel.place(x=30, y=180)

        PassEntry = tk.Entry(root_login, width=40)
        PassEntry.place(x=30, y=200)

        ErrorLabel = tk.Label(root_login, text="", font=("Courier", 18))
        ErrorLabel.place(x=30, y=240)

        LogInButton = tk.Button(text="Log in", height=3, width=14, command=lambda: self.ButtonLogic(UserEntry.get(), PassEntry.get(), root_login, ErrorLabel))
        LogInButton.place(x=30, y=400)

        root_login.mainloop()


App = Logowanie()
App.UILogin()