import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for better image handling


def choose_element_visual():
    """Presents a GUI with images for user selection of the checkpoint to find."""
    root = tk.Tk()
    root.title("Checkpoint Selection")

    # Optional: Set window size
    root.geometry("600x300")

    user_choice = [None]

    def on_click(selection):
        user_choice[0] = selection
        messagebox.showinfo("Selection", f"You chose {selection}!")
        root.destroy()  # Close window

    def load_icon(filename):
        try:
            # 1. Open the image
            img = Image.open(filename)
            # 2. Resize it to fit on a button (e.g., 150x150 pixels)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            # 3. Convert to a format Tkinter understands
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"Error: Could not find {filename}")
            return None

    # Load images
    icon_a = load_icon("utils/A.jpg")
    icon_b = load_icon("utils/B.jpg")
    icon_c = load_icon("utils/C.jpg")

    # --- CREATE BUTTONS ---
    btn1 = tk.Button(root, image=icon_a, text="A", compound="top",
                     command=lambda: on_click("A"))

    btn2 = tk.Button(root, image=icon_b, text="B", compound="top",
                     command=lambda: on_click("B"))

    btn3 = tk.Button(root, image=icon_c, text="C", compound="top",
                     command=lambda: on_click("C"))

    # --- LAYOUT (GRID) ---
    # Using grid is often better than pack for side-by-side images
    label = tk.Label(root, text="Click the desired checkpoint to find:", font=("Arial", 16))
    label.grid(row=0, column=0, columnspan=3, pady=20)

    btn1.grid(row=1, column=0, padx=20)
    btn2.grid(row=1, column=1, padx=20)
    btn3.grid(row=1, column=2, padx=20)

    root.mainloop()
    return user_choice[0]
