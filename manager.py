import os
import base64
import hashlib
from operator import itemgetter
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class P_Manager:
	# print(os.urandom(32))
	salt = b'\xa5h\xdd\xbd\xa3\xd9\x0c\xec0\xeb\xe4\xa5o\xc6c\xcd\xa3\x0b\x0cr\xee\xf5\xf1C\xfa\xe3j\x81\xa6\x98)\xc6'
	kdf = PBKDF2HMAC(
		algorithm = hashes.SHA512(),
		length = 32,
		salt = salt,
		iterations=100020,
		backend=default_backend()
		)
	
	labels = [
		'Rótulo',
		'Senha',
		'Login',
		'Email'
	]

	path = os.getcwd()
	dat_path = os.path.join(path,'dat')

	def __init__(self):
		self.lista = [[
		'Rótulo',
		'Login',
		'Email',
		'Senha'
		]]

	def load_senha(self, senha_save):
		self.senha_save = senha_save # senha_save eh a hash armazenada em .key

	def nova_senha(self, senha):
		s_hash = str.encode(self.hash_str(senha))
		with open(os.path.join(self.dat_path,'s_hash.key'),'wb') as file:
			file.write(s_hash)

	def kill(self):
		# del self.senha
		del self.lista
		del self.key
		del self.fernet

	def hash_str(self,string):
		return hashlib.sha512(string.encode('utf-8')).hexdigest()

	def checa_senha(self, senha):
		if self.hash_str(senha) == self.senha_save:
			return True
		else:
			return False

	def gerar_key(self,senha):
		self.key = base64.urlsafe_b64encode(self.kdf.derive(str.encode(senha)))
		self.gerar_Fernet()
		return self.key

	def gerar_Fernet(self):
		self.f = Fernet(self.key)

	def load(self):
		try:
			with open(os.path.join(self.dat_path,'dat.key'),'rb') as file:
				self.lista = []
				for entry in self.f.decrypt(file.read()).decode().split('\n'):
					self.lista.append(entry.split(','))
				del self.lista[-1]
				return True
		except:
			return False

	def add(self, entry):
		self.lista.append(entry)
		self.save()

	def save(self): # cuidado para nao reescrever
		with open(os.path.join(self.dat_path,'dat.key'),'wb') as file:

			FullFile = ''
			for entry in self.lista:
				linha = ''
				for elem in entry:
					linha += elem + ','

				linha = linha[:-1] + '\n'
				FullFile += linha
				# print(FullFile)

			file.write(self.f.encrypt(FullFile.encode()))

	def bsuca_rotulo(self,rotulo):
		c=0
		for rot in self.lista[1:]:
			c+=1
			if rot[0] == rotulo:
				return c
		return False

	def sort_alpha(self):
		a = [self.lista[0]]
		self.lista = a + sorted(self.lista[1:], key=itemgetter(1))

	def sort_data(self):
		a = [self.lista[0]]
		k = sorted(self.lista[1:])
		k.reverse()
		self.lista = a + k
