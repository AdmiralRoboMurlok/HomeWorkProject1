import sqlite3
import tkinter as tk


logins = open("logins.txt", "r")
class Logowanie:
    def __init__(self):
        self._username = logins.readline(1)
        self._password = logins.readline(2)
        logins.close()
    def ButtonLogic(self, ToDestroy):
        pass
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

        LogInButton = tk.Button(text="Log in", height=3, width=14, command=lambda: self.ButtonLogic(root_login))
        LogInButton.place(x=30, y=400)


        root_login.mainloop()


App = Logowanie()
App.UILogin()