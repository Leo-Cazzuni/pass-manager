from theme import *
import tkinter as tk
from datetime import datetime

def is_enter(key):
	if key=='\n' or key==',':
		return False
	return True

class NS_box(tk.Frame):
	def __init__(self,manager,menu):
		self.manager = manager
		self.menu = menu
		self.sort = 0

		self.window2 = tk.Toplevel()
		self.window2.title('Nova Senha')
		# self.window2.iconbitmap('icon.ico')

		self.text = tk.Label(self.window2,text='Nova Senha', font=("Courier", 10), pady=10)

		self.frame = tk.LabelFrame(self.window2, borderwidth=0, highlightthickness=0, padx=10)
		validation = self.frame.register(is_enter)
		self.t_rotulo = tk.Label(self.frame,text='Nome*:')
		self.e_rotulo = tk.Entry(self.frame, width=30, validate="key", validatecommand=(validation, '%S'))
		self.e_rotulo.bind("<Return>", (lambda event: self.add()) )
		self.t_login = tk.Label(self.frame,text='Login:')
		self.e_login = tk.Entry(self.frame, width=30, validate="key", validatecommand=(validation, '%S'))
		self.e_login.bind("<Return>", (lambda event: self.add()) )
		self.t_email = tk.Label(self.frame,text='Email:')
		self.e_email = tk.Entry(self.frame, width=30, validate="key", validatecommand=(validation, '%S'))
		self.e_email.bind("<Return>", (lambda event: self.add()) )
		self.t_senha = tk.Label(self.frame,text='Senha*:')
		self.e_senha = tk.Entry(self.frame, width=30, validate="key", validatecommand=(validation, '%S'))
		self.e_senha.bind("<Return>", (lambda event: self.add()) )

		self.b_add = tk.Button(self.frame,text='Ok', width=10, command = self.add)
		self.b_cancel = tk.Button(self.frame,text='Cancelar', width=10, command = self.quit)

		theme_conf([self.window2,
					self.text,
					self.frame,
					self.t_rotulo,
					self.e_rotulo,
					self.t_login,
					self.e_login,
					self.t_email,
					self.e_email,
					self.t_senha,
					self.e_senha,
					self.b_add,
					self.b_cancel])

		self.text.pack()

		self.frame.pack()
		self.t_rotulo.grid(row=0,column=0, pady=10)
		self.e_rotulo.grid(row=0,column=1, pady=10, columnspan=2)
		self.t_login.grid(row=1,column=0, pady=10)
		self.e_login.grid(row=1,column=1, pady=10, columnspan=2)
		self.t_email.grid(row=2,column=0, pady=10)
		self.e_email.grid(row=2,column=1, pady=10, columnspan=2)
		self.t_senha.grid(row=3,column=0, pady=10)
		self.e_senha.grid(row=3,column=1, pady=10, columnspan=2)

		self.b_add.grid(row=4,column=1, pady=10)
		self.b_cancel.grid(row=4,column=2, pady=10)

	def quit(self):
		self.window2.destroy()

	def add(self):
		rotulo = self.e_rotulo.get()
		login = self.e_login.get()
		senha = self.e_senha.get()
		email = self.e_email.get()

		if rotulo == '' or senha == '':
			if hasattr(self, 'erro_preenchimento'):
				self.erro_preenchimento.destroy()
			self.erro_preenchimento = tk.Label(self.window2,text='* Preencher áreas obrigatórias',fg='red',bg=background)
			self.erro_preenchimento.pack()
			return

		data = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

		self.manager.add([data,rotulo,login,email,senha])
		self.window2.destroy()
		self.menu.faz_lista()
