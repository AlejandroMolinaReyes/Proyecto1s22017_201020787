from nodo import Pagina, Clave

class ArbolB:

	def __init__(self):
		self.raiz = None

########################### insertar ##########################################

#-------------------------------- insertar --------------------------------
	
	def __insertar(self,raiz,valor,dato):
		if raiz==None:
			return __insertar(Pagina(),valor,dato)
		else:
			if raiz.nodo1 == None:
				raiz.nodo1 = Clave(valor,dato)
			elif raiz.nodo1 != None:
				if raiz.nodo1.valor < valor:
					pass


		


	def insertar(self,valor,dato):
		self.__raiz = self.__insertar(self.__raiz,valor,dato)


#--------------------------------------------------------------------------

################################################################################

################################## imprimir ###################################

	def __imprimir(self,raiz):
		if raiz!=None:
			pass

	def imprimir(self):
		self.__imprimir(self.__raiz)


############################################################################



