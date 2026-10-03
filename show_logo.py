import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Snake Game - Logo")
root.resizable(False, False)

img = Image.open("logo.png")
photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=img.width, height=img.height, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

tk.Label(
    root, text="Snake Game Logo", font=("Consolas", 14, "bold"),
    bg="#111", fg="#0f0", pady=6,
).pack(fill=tk.X)

root.mainloop()