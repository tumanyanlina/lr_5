import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3


class DatabaseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("SQLite GUI")
        self.master.geometry("400x400")

        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        self.listbox = tk.Listbox(master, width=50)
        self.listbox.pack(pady=20)

        frame = tk.Frame(master)
        frame.pack()

        tk.Button(frame, text="Добавить запись", width=15, command=self.add_record).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Удалить запись", width=15, command=self.delete_record).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Обновить список", width=15, command=self.load_records).grid(row=0, column=2, padx=5)

        self.load_records()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def load_records(self):
        self.listbox.delete(0, tk.END)
        self.cursor.execute("SELECT id, name FROM records")
        for row in self.cursor.fetchall():
            self.listbox.insert(tk.END, f"{row[0]}: {row[1]}")

    def add_record(self):
        name = simpledialog.askstring("Добавить запись", "Введите имя:")
        if name:
            self.cursor.execute("INSERT INTO records (name) VALUES (?)", (name,))
            self.conn.commit()
            self.load_records()

    def delete_record(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Удаление", "Выберите запись для удаления")
            return
        record = self.listbox.get(selected[0])
        record_id = int(record.split(":")[0])
        self.cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
        self.conn.commit()
        self.load_records()

def main():
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
