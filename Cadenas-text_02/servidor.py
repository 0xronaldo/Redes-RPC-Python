#!/usr/bin/env python3

# Autor: Brayan Sanchez
# Enunciado : Implementa un servidor RPC que permita convertir cadenas de texto en 
# mayúsculas o minusculas según la elección del cliente. 

# Servidor XML-RPC para transformacion de cadenas


from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler


IP_SERVER = "192.168.100.37"
PORT = 9200

def func_mayusculas(s: str) -> str:
	return str(s).upper()

def func_minusculas(s: str) -> str:
	return str(s).lower()

def main():

	with SimpleXMLRPCServer((IP_SERVER, PORT), requestHandler=RequestHandler, allow_none=True, logRequests=True) as server:
		server.register_introspection_functions()
		server.register_function(func_mayusculas, "mayus")
		server.register_function(func_minusculas, "minus")
        print(f'[SERVIDOR] Procesando....')
        sleep(0.5)
		print(f"[SERVIDOR] escuchando en http://{IP_SERVER}:{PORT}/")
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			print("\nDetenido.")

if __name__ == "__main__":
	main()