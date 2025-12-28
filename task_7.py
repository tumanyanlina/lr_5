from tkinter import Tk, Frame, Menu


class Window(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_menu()

    def create_menu(self):
        self.master.title("Мое меню")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.on_exit)

        menubar.add_cascade(label="Файл", menu=file_menu)

    def on_exit(self):
        self.master.destroy()


def main():
        root = Tk()
        root.geometry("250x150+300+300")

        Window(root)

        root.mainloop()


if __name__ == "__main__":
    main()
