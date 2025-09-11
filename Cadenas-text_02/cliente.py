#!/usr/bin/env python3
# autor: Brayan Ronaldo
# Fecha: 10/09/25
# enenciado : Implementa un servidor RPC que permita convertir cadenas de texto en 
# mayúsculas o minúsculas según la elección del cliente. 
# Cliente XML-RPC para cadenas: mayus/minus

import xmlrpc.client

IP_SRV = "192.168.100.37"
PORT = 9200
def servidor_cadenas():
	url = f"http://{IP_SRV}:{PORT}/"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)

	print(f"[CLIENTE] conectado a {url}")
	mensaje = input("Ingrese texto: ")
	mode = input("Elija modo ('mayus' o 'minus'): ").strip().lower()

	if mode == "mayus":
		print(proxy.func_mayusculas(mensaje))
	elif mode == "minus":
		print(proxy.func_minusculas(mensaje))
	else:
		print("Modo no válido. Use 'mayus' o 'minus'.")

if __name__ == "__main__":
	servidor_cadenas()
