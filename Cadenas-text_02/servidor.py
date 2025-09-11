#!/usr/bin/env python3

# Autor: Brayan Sanchez
# Enunciado : Implementa un servidor RPC que permita convertir cadenas de texto en 
# mayúsculas o minusculas según la elección del cliente. 

# Servidor XML-RPC para transformacion de cadenas


from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import time

IP_SERVER = "192.168.100.37"
PORT = 9200

def func_mayusculas(s: str) -> str:
	return str(s).upper()

def func_minusculas(s: str) -> str:
	return str(s).lower()

def run_server():
	print("[SERVIDOR] Procesando...")
	time.sleep(0.5)

	with SimpleXMLRPCServer((IP_SERVER, PORT), allow_none=True, logRequests=True) as server:
		server.register_introspection_functions()
		server.register_function(func_mayusculas, 'func_mayusculas')
		server.register_function(func_minusculas, 'func_minusculas')
		print(f"[SERVIDOR] escuchando en http://{IP_SERVER}:{PORT}/")
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			print("\nDetenido.")

if __name__ == "__main__":
	run_server()