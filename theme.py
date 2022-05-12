amarelo = '#e7db74'
amarelo2 = '#ffff00'
verde = '#a6e22b'
roxo = '#ac80ff'
rosa = '#f92472'
cinza = '#282923'
cinza = '#303030'
cinza_e = '#181915' 
laranja = '#fd9622' 
azul_c = '#67d8ef'

background = cinza
foreground = verde

def theme_conf(widgets, b=True, f=True):
	for widget in widgets:
		if b:
			try:
				widget.config(bg=background)
			except:
				pass
		if f:
			try:
				widget.config(fg=foreground)
			except:
				pass
