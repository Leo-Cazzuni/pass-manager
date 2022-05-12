import os
from pw import *
import tkinter as tk
from manager import *
# from tkinter.ttk import *
from tkinter import messagebox

path = os.getcwd()
dat_path = os.path.join(path,'dat')

def main():
	window = tk.Tk()
	window.title('Password Manager')
	# window.iconbitmap('icon.ico')
	# window.geometry("400x500")	

	try:
		with open(os.path.join(dat_path,'s_hash.key'),'rb') as file:
			senha_hash = file.read().decode()
			if len(senha_hash) == 128 and set(senha_hash).issubset(set(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'])):
				manager = P_Manager()
				manager.load_senha(senha_hash)
				window1 = Pw_box(window,manager,mode=0)
			else:
				print('Arquivo senha Corropido/Invalido')

				# colocar pop up avisando
				# raise NameError('Arquivo senha Corropido/Invalido')

	except:
		manager = P_Manager()
		window1 =  Pw_box(window,manager,mode=1)
			

	# win_senha = tk.Toplevel()
	# win_senha.title('Senha')

	
	# window1.pack_grid()



	window.mainloop()


if __name__ == '__main__':
	main()