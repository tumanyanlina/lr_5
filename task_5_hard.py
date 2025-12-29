import tkinter as tk

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Секундомер")
        self.master.geometry("300x200")

        self.running = False
        self.seconds = 0

        self.label = tk.Label(master, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=30)

        frame = tk.Frame(master)
        frame.pack()

        tk.Button(frame, text="Старт", width=10, command=self.start).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Стоп", width=10, command=self.stop).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Сброс", width=10, command=self.reset).grid(row=0, column=2, padx=5)

    def update_timer(self):
        if self.running:
            self.seconds += 1
            self.label.config(text=self.format_time(self.seconds))
            self.master.after(1000, self.update_timer) 

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 0
        self.label.config(text="00:00:00")

    @staticmethod
    def format_time(seconds):
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hrs:02}:{mins:02}:{secs:02}"

def main():
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
