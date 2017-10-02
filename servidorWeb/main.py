from flask import Flask , request
from estructuras import ListaDoble
from usuario import Usuario

listaUsuarios = ListaDoble()
servidor = Flask(__name__)


@servidor.route("/registrar",methods=['POST'])
def registrarUsuario():# registra a los usuarios
	print("-----Registro Usuario-----")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	global listaUsuarios
	if listaUsuarios.buscar_usuario(user)==None:
		listaUsuarios.agregar_final(Usuario(user,password))
		print("Registro exitoso")
		listaUsuarios.recorrer_fin_inicio()
		print("--------------------------")
		return "True"
	else:
		listaUsuarios.recorrer_fin_inicio()
		print("Registro fallido")
		print("--------------------------")
		return "False"
	
	

@servidor.route("/auntenticar",methods=['POST'])
def autenticarUsuario():# ver si existe el usuario
	print("-----------Login----------")
	user = str(request.form['user'])
	password = str(request.form['pass'])
	global listaUsuarios
	auxUser = listaUsuarios.buscar_usuario(user)
	if auxUser==None:
		print("No existe Usuario")
		print("--------------------------")
		return "False"
	elif auxUser.nombre == user and auxUser.contraseña == password:
		listaUsuarios.recorrer_fin_inicio()
		print("Exitoso login")
		print("--------------------------")
		return "True"
	else:
		print("usuario o contraseña mala")
		print("--------------------------")
		return "False"

"""
@servidor.route("/listaUsuarios",methods=['POST'])
def listaUsuarios():
	global listaUser
	cadena =""
	for item in listaUser:
		cadena = item+","+cadena
	return cadena

@servidor.route("/EliminarUsuario",methods=['POST'])
def eliminarUser():
	print("-----------Eliminar usuario----------")
	eliminar = str(request.form['delete'])
	global usuarios
	global listaUser
	if usuarios.buscar(eliminar)!=None:
		listaUser.remove(eliminar)
		usuarios.eliminar(eliminar)
		usuarios.imprimir()
		print("----------------------------------")
		return "True"
	usuarios.imprimir()
	print("----------------------------------")
	return "False"

@servidor.route("/imgArbol",methods=['POST'])
def imgArbol():
	print("-----------img Arbol----------")
	global usuarios
	usuarios.imagen()
	print("exitoso")
	print("---------------------")
	return usuarios.texto

"""

if __name__ == "__main__":
	servidor.run(debug=True, host='127.0.0.1', port=9090)