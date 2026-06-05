import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="#E3F2FD")
window.geometry("300x200")
window.resizable(False, False)
window.title("yo")
window.eval('tk::PlaceWindow . center')

# Variabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi
def tombol_click():
    depan = NAMA_DEPAN.get().strip()
    belakang = NAMA_BELAKANG.get().strip()

    if not depan or not belakang:
        showinfo("Warning", "Nama depan dan nama belakang harus diisi!")
        return

    pesan = f"yo {depan} {belakang}, don't forget to gayly dilly dallying, brother"
    showinfo("Hi", pesan)

# Frame
input_frame = ttk.Frame(window, padding=20)
input_frame.pack(fill="x", expand=True)

# Nama depan
ttk.Label(input_frame, text="Nama Depan:").pack(
    padx=10, fill="x", expand=True
)

ttk.Entry(
    input_frame,
    textvariable=NAMA_DEPAN
).pack(
    padx=10,
    fill="x",
    expand=True
)

# Nama belakang
ttk.Label(input_frame, text="Nama Belakang:").pack(
    padx=10,
    fill="x",
    expand=True
)

ttk.Entry(
    input_frame,
    textvariable=NAMA_BELAKANG
).pack(
    padx=10,
    fill="x",
    expand=True
)

# Tombol
ttk.Button(
    input_frame,
    text="Sapa!",
    command=tombol_click
).pack(
    fill="x",
    expand=True,
    padx=10,
    pady=10
)

window.mainloop()