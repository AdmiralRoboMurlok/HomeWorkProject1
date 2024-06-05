import sqlite3
import tkinter as tk
from tkinter import END

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
#cursor.execute("CREATE TABLE posts (date TEXT, about TEXT, postID INTEGER)")

class StronaGlowna:
    def __init__(self):
        self.DataList = []
    def UIMain(self):
        def AddToView():
            if len(self.DataList) > 0:
                for i in self.DataList:
                    row = cursor.execute("SELECT date, about FROM posts WHERE postID = ?", (i,), ).fetchall()
                    row = str(row).strip()
                    ToDoListbox.insert(row)

        root_main = tk.Tk()
        root_main.geometry("800x800")
        root_main.title("Strona Główna")

        ToDoScrollBar = tk.Scrollbar(root_main, width=30)

        ToDoListbox = tk.Listbox(root_main, yscrollcommand=ToDoScrollBar.set, width=70, height=40)
        ToDoListbox.place(x=30, y=30)

        if len(self.DataList) > 0:
            for i in range(1, len(self.DataList)+1):
                row = cursor.execute("SELECT date, about, postID FROM posts WHERE postID = ?", (i,),).fetchall()
                row = str(row).lstrip('[(').rstrip(')]')
                ToDoListbox.insert(END, row)

        AddToDatabaseButton = tk.Button(root_main, text="Dodaj", width=16, command=lambda: self.UIAddToDatabse(root_main))
        AddToDatabaseButton.place(x=590, y=60)

        EditInDatabaseButton = tk.Button(root_main, text="Edytuj", width=16, command=lambda: self.EditInDB(root_main))
        EditInDatabaseButton.place(x=590, y=90)

        root_main.mainloop()

    def UIAddToDatabse(self, ToDestroy):
        ToDestroy.destroy()

        def AddDatatoDatabase(ADate, about, ToDestroy):
            CurrentID = len(self.DataList) + 1
            cursor.execute("INSERT INTO posts VALUES (? , ?, ?)", (ADate, about, CurrentID))
            self.DataList.append(CurrentID)
            ToDestroy.destroy()
            self.UIMain()

        ADDtoDB = tk.Tk()
        ADDtoDB.geometry("300x600")
        ADDtoDB.title("Add to list")

        DateLabel = tk.Label(ADDtoDB, text="Poddaj date:", font=("Courier", 14))
        DateLabel.place(x=30, y=30)

        DateEntry = tk.Entry(ADDtoDB, width=30)
        DateEntry.place(x=30, y=50)

        AboutLabel = tk.Label(ADDtoDB, text="Poddaj treść:", font=("Courier", 14))
        AboutLabel.place(x=30, y=100)

        AboutEntry = tk.Entry(ADDtoDB, width=30)
        AboutEntry.place(x=30, y=120)

        SendButton = tk.Button(ADDtoDB, text="Wyślij", height=3, width=12, command=lambda: AddDatatoDatabase(DateEntry.get(), AboutEntry.get(), ADDtoDB))
        SendButton.place(x=30, y=480)

        ADDtoDB.mainloop()

    def EditInDB(self, ToDestroy):
        ToDestroy.destroy()
        def EditRecord(NewDate, NewAbout, NewID, ToDestroy, ToConfig):
            if NewID in self.DataList:
                ToDestroy.destroy()

            else:
                ToConfig.config(text="Błędne ID")


        EditDB_root = tk.Tk()
        EditDB_root.geometry("300x600")
        EditDB_root.title("Edytuj")

        DateLabel = tk.Label(EditDB_root, text="Poddaj date:", font=("Courier", 14))
        DateLabel.place(x=30, y=30)

        DateEntry = tk.Entry(EditDB_root, width=30)
        DateEntry.place(x=30, y=50)

        AboutLabel = tk.Label(EditDB_root, text="Poddaj treść:", font=("Courier", 14))
        AboutLabel.place(x=30, y=100)

        AboutEntry = tk.Entry(EditDB_root, width=30)
        AboutEntry.place(x=30, y=120)

        IDLabel = tk.Label(EditDB_root, text="ID wpisu:", font=("Courier", 14))
        IDLabel.place(x=30, y=170)

        IDEntry = tk.Entry(EditDB_root, width=30)
        IDEntry.place(x=30, y=190)

        ErrorLabel = tk.Label(EditDB_root, text="", font=("Courier", 14))
        ErrorLabel.place(x=30, y=250)

        SendButton = tk.Button(EditDB_root, text="Wyślij", height=3, width=12, command=lambda: EditRecord(DateEntry.get(), AboutEntry.get(), IDEntry.get(), EditDB_root, ErrorLabel))
        SendButton.place(x=30, y=480)

        EditDB_root.mainloop()


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