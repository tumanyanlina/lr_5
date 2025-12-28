import tkinter as tk
import random

def generate_random_color() -> str:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"#{red:02x}{green:02x}{blue:02x}"

def change_color():
    new_color = generate_random_color()
    color_panel.config(bg=new_color)

def main():
    global color_panel

    root = tk.Tk()
    root.title("Цветная панель")
    root.geometry("500x350")
    root.configure(bg="linen")

    color_panel = tk.Label(root,text="Цветная панель",bg="white",font=("Arial", 16),width=30,height=8)
    color_panel.pack(pady=20)

    tk.Button(root,text="Сменить цвет",font=("Arial", 14),width=20,height=2,command=change_color).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
