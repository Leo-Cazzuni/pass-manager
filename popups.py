import tkinter as tk

def pop_erro(win, texto):
	msg = messagebox.showerror('Erro', texto)
	tk.Label(win, text=msg).pack()
