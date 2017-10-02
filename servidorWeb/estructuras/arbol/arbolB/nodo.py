class Pagina:

	def __init__(self):
		self.nodo1 = None # posicion 1
		self.nodo2 = None # posicion 2
		self.nodo3 = None # posicion 3
		self.nodo4 = None # posicion 4
		self.nodo5 = None # posicion 5

class Clave:

	def __init__(self,valor,dato):
		self.bajo = None # puntero bajo
		self.valor = valor # valor equilibrio
		self.dato = dato # dato a guardar
		self.alto = None # puntero alto

