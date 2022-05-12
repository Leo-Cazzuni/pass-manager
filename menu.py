from ns import *
from theme import *
import tkinter as tk
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

class Menu(tk.Frame):
	def __init__(self,window,manager):
		window.geometry("400x350")
		self.window = window
		self.manager = manager
		self.sort = 'Alfabético'

		self.text = tk.Label(self.window,text='Password List',font=("Courier", 20), pady=10)

		self.frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)

		# self.entrada_busca = tk.Entry(self.frame, width=30)
		# self.entrada_busca.bind("<Return>", (lambda event: self.buscar_senha()) )
		# self.entrada_busca.insert(0,'Busca n funciona ainda kek')
		# self.b_buscar = tk.Button(self.frame,text='Buscar', width=10, command = self.buscar_senha)
		
		self.b_nova_senha = tk.Button(self.frame,text='Add', command = self.nova_senha)
		sort_entry = tk.StringVar()
		sort_entry.set('Ordem')
		self.sort_db = tk.OptionMenu(self.frame,sort_entry,'Última Modificação','Alfabético', command=self.sort_type)
		self.sort_db.config(width=10)
		self.sort_db["menu"].config(bg=background,fg=foreground)

		theme_conf([self.window,self.text,self.frame,self.b_nova_senha,self.sort_db])

		self.text.pack()
		self.pack1()
		self.faz_lista()

	def pack1(self):
		
		self.frame.pack()
		# self.entrada_busca.pack(side=tk.LEFT)
		# self.b_buscar.pack(side=tk.LEFT)

		self.b_nova_senha.grid(row=0,column=0,sticky="ew",padx=(0,105))
		self.sort_db.grid(row=0,column=1,sticky=tk.E,padx=(105,0))

	def sort_type(self,entry):
		self.sort = entry
		if self.sort == 'Alfabético':
			self.manager.sort_alpha()
		if self.sort == 'Última Modificação':
			self.manager.sort_data()
		self.faz_lista(noload=True)

	def faz_lista(self, noload=False):
		self.pack1()
		if hasattr(self, 'frame2'):
			self.frame2.destroy()

		self.frame2 = tk.LabelFrame(self.window)
		self.frame2.pack()

		if (noload==True or self.manager.load()) and len(self.manager.lista)!=1:
			self.frame2.configure(borderwidth=0, highlightthickness=0,bg=background)

			scroll = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
			self.listbox = tk.Listbox(self.frame2,  width=27,  bg='#F0F0F0', font=("Courier", 15), yscrollcommand=scroll.set)
			scroll.config(command = self.listbox.yview)
			scroll.pack(side=tk.RIGHT, fill=tk.Y,pady=5)

			self.listbox.pack(fill=tk.BOTH, expand=1,pady=5)
			self.listbox.bind("<Double-Button-1>", (lambda event: self.show_entry()))
			self.listbox.bind("<Delete>", (lambda event: self.deletar(self.listbox.index(tk.ANCHOR)+1)))

			theme_conf([self.listbox,scroll])

			# for entry in self.manager.lista[1:]:
			# for entry in sorted(self.manager.lista[1:], key=itemgetter(1)):
			
			for entry in self.manager.lista[1:]:

				# e = entry[0].split('-')
				# e = "("+e[0]+")"
				# e = entry[0]
				# self.listbox.insert(tk.END, e+entry[1])
				
				self.listbox.insert(tk.END, entry[1])
				# tk.Label(self.frame2, text=entry[0], width=45).pack(fill=tk.BOTH)
		else:
			self.t_sem_senhas = tk.Label(self.frame2,text='Não há Senhas',width=45)
			self.t_sem_senhas.pack()

		if hasattr(self, 'frame3'):
			self.frame3.destroy()

	def nova_senha(self):
		nova_senha_box = NS_box(self.manager, self)

	def show_entry(self, N = None):

		if hasattr(self, 'frame'):
			self.frame.pack_forget()

		if N == None:
			N_lista = self.listbox.index(tk.ANCHOR) + 1
		else:
			N_lista = N

		if hasattr(self, 'frame2'):
			self.frame2.destroy()
		
		self.frame2 = tk.LabelFrame(self.window, padx=10, pady=10)
		self.frame2.pack()
		theme_conf([self.frame2])
		
		c=0
		for item in self.manager.lista[N_lista][1:]:
			if item == '':
				continue

			tk.Label(self.frame2, font=("Courier", 15), text=self.manager.lista[0][c] + ':',bg=background,fg=foreground).grid(row=0+2*c,column=0)
			# tk.Label(self.frame2, width=22, font=("Courier", 15), text=item).grid(row=0+2*c,column=1)

			w = tk.Text(self.frame2, height=1, borderwidth=0, width=30)
			w.insert(1.0, item)
			w.configure(state="disabled",bg=background,fg=foreground)
			w.grid(row=0+2*c,column=1)

			c+=1


		if hasattr(self, 'frame3'):
			self.frame3.destroy()

		self.frame3 = tk.LabelFrame(self.window, borderwidth=0, highlightthickness=0, padx=10, pady=10,bg=background,fg=foreground)
		self.frame3.pack()
		tk.Button(self.frame3,text='Editar', width=10, command = lambda: self.editar(N_lista),bg=background,fg=foreground).grid(row=0,column=0)
		tk.Button(self.frame3,text='Voltar', width=10, command = self.faz_lista,bg=background,fg=foreground).grid(row=0,column=1)

	def editar(self,N_lista):
		if hasattr(self, 'frame2'):
			self.frame2.destroy()
		if hasattr(self, 'frame3'):
			self.frame3.destroy()

		self.frame2 = tk.LabelFrame(self.window, borderwidth=0, highlightthickness=0, padx=10,bg=background,fg=foreground)
		self.frame2.pack()

		

		self.entradas = []
		c=0
		for item in self.manager.lista[N_lista][1:]:
			tk.Label(self.frame2,text=self.manager.lista[0][c],bg=background,fg=foreground).grid(row=0+2*c,column=0)
			self.entradas.append(tk.Entry(self.frame2, width=30,bg=background,fg=foreground))
			self.entradas[c].grid(row=0+2*c,column=1)
			self.entradas[c].insert(0,item)
			c+=1

		self.frame3 = tk.LabelFrame(self.window, borderwidth=0, highlightthickness=0, padx=10, pady=10,bg=background,fg=foreground)
		self.frame3.pack()
		tk.Button(self.frame3,text='Salvar', width=10, command = lambda: self.salvar(N_lista),bg=background,fg=foreground).grid(row=0,column=0)
		tk.Button(self.frame3,text='Voltar', width=10, command = self.faz_lista,bg=background,fg=foreground).grid(row=0,column=1)
		tk.Button(self.frame3,text='Deletar', width=10, command = lambda: self.deletar(N_lista),bg=background,fg=foreground).grid(row=0,column=2)

	def salvar(self,N_lista):		

		self.manager.lista[N_lista] = []
		self.manager.lista[N_lista].append(datetime.now().strftime("%Y/%m/%d-%H:%M:%S"))
		for item in self.entradas:
			self.manager.lista[N_lista].append(item.get())
		self.manager.save()
		self.show_entry(N_lista)

	def deletar(self,N_lista):
		alerta = tk.messagebox.askquestion('Atenção',f'Deseja deletar {self.manager.lista[N_lista][1]}?')
		if alerta == 'no':
			self.faz_lista()
			return

		# print(self.manager.lista[N_lista])

		# for elem in self.manager.lista:
		# 	if self.manager.lista[1:] == self.manager.lista[N_lista]:
		# 		del self.manager.lista[N_lista]
		# 		break
		del self.manager.lista[N_lista]
		self.manager.save()
		self.faz_lista()

	def buscar_senha(self):
		pass
