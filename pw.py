from theme import *
import tkinter as tk
from menu import *
from manager import *

class Pw_box(tk.Frame):
	def __init__(self,window,manager,mode):
		self.window = window
		self.manager = manager
		self.mode = mode

		self.frame = tk.LabelFrame(window)
		self.frame.pack()
		self.texto = tk.Label(self.frame,text='Senha:')
		self.entrada = tk.Entry(self.frame, width=30, show='*')
		# self.entrada.insert(0,'Senha')
		self.entrada.bind("<Return>", (lambda event: self.click_ok()) )
		self.b_ok = tk.Button(self.frame,text='Ok', width=10, command = self.click_ok)
		self.b_quit = tk.Button(self.frame,text='Quit', width=10, command = self.click_quit)

		if mode==1:
			self.texto = tk.Label(self.frame,text='Nova Senha:')
			self.texto2 = tk.Label(self.frame,text='Confirmar:')
			self.entrada2 = tk.Entry(self.frame, width=30, show='*')
			self.entrada2.bind("<Return>", (lambda event: self.click_ok()) )
		elif mode !=0:
			raise NameError('mode deve ser 0 ou 1')
		
		self.pack_grid()
		self.c = 0

	def pack_grid(self):
		theme_conf([self.window,self.frame,self.texto,self.entrada,self.b_ok,self.b_quit])
		self.texto.grid(row=0,column=0)
		self.entrada.grid(row=1, column=0, columnspan=2, padx=10)

		if self.mode==1:
			self.texto2.grid(row=2,column=0)
			self.entrada2.grid(row=3, column=0, columnspan=2, padx=10)
			theme_conf([self.texto2,self.entrada2])

		self.b_ok.grid(row = 2+2*self.mode, column=0, pady=5)
		self.b_quit.grid(row = 2+2*self.mode, column=1, pady=5)

	def kill(self):
		self.texto.destroy()
		self.entrada.destroy()
		self.b_ok.destroy()
		self.b_quit.destroy()

		if hasattr(self, 't_senha_errada'):
			self.t_senha_errada.destroy()

		if self.mode == 1:
			self.texto2.destroy()
			self.entrada2.destroy()

		self.frame.destroy()

	def click_ok(self):
		if self.mode == 0:
			if self.manager.checa_senha(self.entrada.get()):
				self.manager.gerar_key(self.entrada.get())
				self.kill()
				window1 = Menu(self.window,self.manager)
			else:
				if hasattr(self, 't_senha_errada'):
					self.t_senha_errada.destroy()

				self.t_senha_errada = tk.Label(self.window,text='Senha Incorreta',fg='red')
				theme_conf([self.t_senha_errada],f=False)
				if self.c == 14:
					self.t_senha_errada = tk.Label(self.window,text='R U rEtArDed?',fg='red')
					theme_conf([self.t_senha_errada],f=False)
				self.c+=1
				self.t_senha_errada.pack()

		elif self.mode == 1:
			if self.entrada.get() == self.entrada2.get():
				self.manager.nova_senha(self.entrada.get())
				self.manager.gerar_key(self.entrada.get())
				self.kill()
				window1 = Menu(self.window,self.manager)
			else:
				print('senhas diferentes')

	def click_quit(self):
		self.window.destroy()

	def info_pop(self):
		pass
