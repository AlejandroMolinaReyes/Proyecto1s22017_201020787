from .nodo import Nodo


class ListaDoble:

	def __init__(self):
		self.__primero = None
		self.__ultimo = None

	def vacio(self):
		if self.__primero == None:
			return True
		else:
			return False


	def agregar_final(self, dato):
		if self.vacio():
			self.__primero = self.__ultimo = Nodo(dato)
		else:
			nuevo = Nodo(dato)
			self.__ultimo.siguiente = nuevo
			nuevo.anterior = self.__ultimo
			self.__ultimo = nuevo
		self.__primero.anterior = self.__ultimo
		self.__ultimo.siguiente = self.__primero

	def recorrer_inicio_fin(self):
		aux = self.__primero
		auxPrint = "["
		while True:
			auxPrint = auxPrint+"("+aux.dato+","+aux.dato+") -> "
			aux = aux.siguiente
			if aux == self.__primero:
				auxPrint =auxPrint+"("+aux.dato+","+aux.dato+")]"
				break
		print(auxPrint)

	def recorrer_fin_inicio(self):
		aux = self.__ultimo
		auxPrint = "["
		while True:
			auxPrint = auxPrint+"("+aux.dato.nombre+","+aux.dato.contraseña+") -> "
			aux = aux.anterior
			if aux == self.__ultimo:
				auxPrint =auxPrint+"("+aux.dato.nombre+","+aux.dato.contraseña+")]"
				break
		print(auxPrint)

	def buscar_usuario(self,nombre):
		aux = self.__primero
		if self.__primero!=None:
			while aux:
				if aux.dato.nombre == nombre:
					return aux.dato
				aux = aux.siguiente
				if aux == self.__primero:
					return None

